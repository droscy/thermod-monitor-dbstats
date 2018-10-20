# -*- coding: utf-8 -*-
"""Setup script for Thermod DB-Stats monitor.

@author:     Simone Rossetto
@copyright:  2018 Simone Rossetto
@license:    GNU General Public License v3
@contact:    simros85@gmail.com

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
"""

from setuptools import setup

def get_version():
    main_ns = {}
    version_str = None
    
    with open('thermod-monitor-dbstats','rt') as script:
        for line in script:
            if line.find('__version__') == 0:
                version_str = '# -*- coding: utf-8 -*-\n{}'.format(line)
                break
    
    exec(version_str, main_ns)
    return main_ns['__version__']

setup(name='thermod-monitor-dbstats',
      version=get_version(),
      description='Thermod DB-Stats monitor.',
      long_description='Thermod DB-Stats monitor collects statistics on Thermod operation',
      author='Simone Rossetto',
      author_email='simros85@gmail.com',
      url='https://github.com/droscy/thermod-monitor-dbstats',
      license = 'GPL-3.0+',
      scripts=['thermod-monitor-dbstats'],
      install_requires=['thermod >= 1.2.0',
                        'requests >= 2.4.3'])

# vim: fileencoding=utf-8 tabstop=4 shiftwidth=4 expandtab
