## begin license ##
#
# "Meresco PyLucene" contains JVM initialization for pylucene
#
# Copyright (C) 2015 Koninklijke Bibliotheek (KB) http://www.kb.nl
# Copyright (C) 2015, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Meresco PyLucene"
#
# "Meresco PyLucene" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Meresco PyLucene" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Meresco PyLucene"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

version = '$Version: 0$'[9:-1].strip()
name='meresco-pylucene'

from distutils.core import setup
from os import walk
from os.path import join

packages = []
for path, dirs, files in walk('meresco'):
    if '__init__.py' in files and path != 'meresco':
        packages.append(path.replace('/', '.'))
data_files = []
for path, dirs, files in walk('doc'):
    files = [f for f in files if f != 'license.conf']
    if files:
        data_files.append((path.replace('doc', '/usr/share/doc/%s' % name, 1), [join(path, f) for f in files]))


setup(
    name=name,
    packages=[
        'meresco',                      #DO_NOT_DISTRIBUTE
    ] + packages,
    data_files=data_files,
    version = version,
    url = 'http://seecr.nl',
    author = 'Seecr (Seek You Too B.V.)',
    author_email = 'info@seecr.nl',
    description = 'JVM initialization for pylucene',
    long_description = '"Meresco Lucene" contains JVM initialization for pylucene',
    license = 'GPLv2',
    platforms = 'all',
)
