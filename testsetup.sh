#!/bin/bash
## begin license ##
#
# "Meresco PyLucene" contains JVM initialization for pylucene
#
# Copyright (C) 2012-2013, 2015-2016, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
# Copyright (C) 2015 Stichting Kennisnet http://www.kennisnet.nl
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

source /usr/share/seecr-tools/functions.d/test

set -e
mydir=$(cd $(dirname $0); pwd)
rm -rf tmp build

definePythonVars
$PYTHON setup.py install --root tmp
removeDoNotDistribute tmp
cp -r test tmp/test
find tmp -type f -exec sed -e "
    s,^usrSharePath.*$,usrSharePath='$mydir/tmp/usr/share/meresco-pylucene',;
    " -i {} \;

runtests "$@"

rm -rf tmp build
