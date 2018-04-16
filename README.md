# Thermod DB-Stats monitor
Collects statistics on Thermod operation.

It records status changes in order to track switch ON and OFF of the heating
along with timestamp.

## License
Thermod DB-Stats monitor v1.0.0 \
Copyright (C) 2018 Simone Rossetto <simros85@gmail.com> \
GNU General Public License v3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


## How to install

### Requirements
*Thermod DB-Stats monitor* requires [Python3](https://www.python.org/)
(at least version 3.5) and the packages:

 - [thermod](https://github.com/droscy/thermod) (>=1.0.0)
 - [requests](http://docs.python-requests.org/) (>=2.4.3)

### Installation
To install the *DB-Stats monitor* first uncompress the tarball and run

```bash
python3 setup.py install
```

### Building and installing on Debian-based system
A Debian package can be build using
[git-buildpackage](https://honk.sigxcpu.org/piki/projects/git-buildpackage/).

Assuming you have already configured your system to use git-buildpackage
(if not see Debian Wiki for [git-pbuilder](https://wiki.debian.org/git-pbuilder),
[cowbuilder](https://wiki.debian.org/cowbuilder) and
[Packaging with Git](https://wiki.debian.org/PackagingWithGit)) then these are
the basic steps:

```bash
git clone https://github.com/droscy/thermod-monitor-dbstats.git
cd thermod-monitor-dbstats
git checkout -b debian/master origin/debian/master
gbp buildpackage
```

The package can then be installed as usual:

```bash
dpkg -i thermod-monitor-dbstats_{version}_all.deb
```


## Starting/Stopping the monitor
To start *DB-Stats monitor* from the same system where Thermod is
running simply execute

```bash
thermod-monitor-dbstats --dbfile {file-path}
```

where `{file-path}` must be set to a file-path where to store all the
information get from Thermod.

If Thermod is running on a *different* system, the option `--host` can be set
to the hostname of that system.

To have the full list of available options run `thermod-monitor-dbstats`
with `--help` option.

### Systemd
If *systemd* is in use, copy the file `thermod-monitor-dbstats.service`
to folder `/lib/systemd/system`, change it to meet your requirements (i.e.
the path where you want to save the file) then execute

```bash
systemctl daemon-reload
systemctl enable thermod-monitor-dbstats.service
```

to automatically start the monitor at system startup.


## The database file
The file created by *DB-Stats monitor* is a standard
[sqlite3](https://www.sqlite.org/) file that can be opened with any
sqlite3 client. For example, to open a file in read-only mode using the
official command line client, execute:

```bash
sqlite3 'file:{file-path}?mode=ro'
```

If the prompt `sqlite>` appears, the database is opened and ready to process
queries. Type `.quit` to close the file and exit sqlite.

### Database schema
The database file is very simple, it contains only the table `thermod_stats`
with the following fields:

 - `hostname`
 - `switchon_time`
 - `switchon_temp`
 - `switchon_status`
 - `switchoff_time`
 - `switchoff_temp`
 - `switchoff_status`

where every time is saved as a timestamp (seconds since the unix epoch)
while every temperature is saved as a float number in celsius or farenheit
degrees in accordance with Thermod settings.

### Some queries
To get all the records in human-readble format of host *mythermo* recorded
in the year *2018* execute in `sqlite>` prompt:

```sql
select
  hostname,
  datetime(switchon_time, 'unixepoch', 'localtime') as switchon_time,
  switchon_temp,
  switchon_status,
  datetime(switchoff_time, 'unixepoch', 'localtime') as switchoff_time,
  switchoff_temp,
  switchoff_status
from thermod_stats
where hostname = 'mythermo'  -- change here the hostname
  and strftime('%Y', datetime(switchon_time, 'unixepoch', 'localtime')) = '2018';
```

To compute how many minutes the heating has been ON per each host per each
month execute:

```sql
select
  hostname,
  strftime('%Y-%m', datetime(switchoff_time, 'unixepoch', 'localtime')) as month,
  round(sum((switchoff_time-switchon_time) / 60)) as heating_on_time
from thermod_stats
group by 1,2
order by 1,2;
```

To get... something else, ask me, I'll try to help you :-)

### Clean database on shutdown
During the shutdown *DB-Stats monitor* cleans the database in two ways:

 1. delete any record that doesn't have a switch off time because that
    record makes no sense from statistics point of view; if you want to keep
    those *invalid* records, start the monitor with `--noclean` option;

 2. delete any record with switch on time older than 3 years; if you want to
    change this time limit, start the monitor with `--timelimit {days}`
    option, where `{days}` is the number of days to keep.
