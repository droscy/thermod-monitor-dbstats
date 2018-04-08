# Thermod DB-Stats monitor
This monitor collects statistics on Thermod operation.

## License
Thermod DB-Stats monitor v0.0.0 \
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
To install *Thermod DB-Stats monitor* first uncompress the tarball and run

```bash
python3 setup.py install
```


## Starting/Stopping the monitor
To start *Thermod DB-Stats monitor* from the same system where Thermod is
running simply execute

```bash
thermod-monitor-dbstats --dbfile {file-path}
```

where `{file-path}` must be set to a file-path where to store all the
informations get from Thermod.

If Thermod is running on a different system, the option `--host` can be set
to the name of the running host. To have the full list of available options
run *Thermod DB-Stats monitor* with `--help` option.

### Systemd
If *systemd* is in use, copy the file `thermod-monitor-dbstats.service`
to folder `/lib/systemd/system`, change it to meet your requirements (i.e.
the path where you want to save the file) then execute

```bash
systemctl daemon-reload
systemctl enable thermod-monitor-dbstats.service
```

to automatically start the monitor at system startup.
