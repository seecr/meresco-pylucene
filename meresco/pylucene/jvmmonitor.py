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

from meresco.core import Observable
from java.lang import Runtime

try:
    from gustos.common.units import MEMORY
except ImportError:
    from warnings import warn
    warn("Unable to import gustos.common, please install", ImportWarning)
    MEMORY='memory'


class JvmMonitor(Observable):

    def handle(self):
        runtime = Runtime.getRuntime()
        maxMem = runtime.maxMemory()
        freeMem = runtime.freeMemory()
        totalMem = runtime.totalMemory()
        unallocatedMem = maxMem - totalMem
        availableMem = unallocatedMem + freeMem
        self.call.report(values={
                "Memory": {
                    "JVM Memory": {
                        "Free": {
                            MEMORY: freeMem
                        },
                        "Max": {
                            MEMORY: maxMem
                        },
                        "Total": {
                            MEMORY: totalMem
                        },
                        "Available": {
                            MEMORY: availableMem
                        }

                    }
                }
            })
        return
        yield
