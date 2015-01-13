## begin license ##
#
# "Meresco PyLucene" contains JVM initialization for pylucene
#
# Copyright (C) 2015 Koninklijke Bibliotheek (KB) http://www.kb.nl
# Copyright (C) 2015 Seecr (Seek You Too B.V.) http://seecr.nl
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

from os import getenv
from lucene import initVM, getVMEnv
from warnings import warn

def getJVM():
    vmargs = [] #['-agentlib:hprof=heap=sites']
    pyluceneVmargs = getenv('PYLUCENE_VM_ARGS')
    if pyluceneVmargs:
        vmargs.extend(pyluceneVmargs.split(','))
    heapDumpPath = getenv('PYLUCENE_HEAPDUMP_PATH')
    if heapDumpPath:
        vmargs.extend(['-XX:+HeapDumpOnOutOfMemoryError', '-XX:HeapDumpPath=%s' % heapDumpPath])
    maxheap = getenv('PYLUCENE_MAXHEAP')
    if not maxheap:
        maxheap = '4g'
        warn("Using '4g' as maxheap for lucene.initVM(). To override use PYLUCENE_MAXHEAP environment variable.")
    try:
        return initVM(maxheap=maxheap, vmargs=','.join(vmargs))
    except ValueError:
        return getVMEnv()
