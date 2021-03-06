# Copyright (C) 2014-2015 Will Metcalf (william.metcalf@gmail.com)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import logging
import subprocess
import re
import socket

log = logging.getLogger(__name__)

class Utils:
    """Various Utilities"""
    def is_valid_ipv4(self,ip):
        if ip:
            if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip) == None:
                return False
            else:
                try:
                    socket.inet_aton(ip)
                    return True
                except socket.error:
                    return False
        else:
            return False    

    def cmd_wrapper(self,cmd):
        #print("running command and waiting for it to finish %s" % (cmd))
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout,stderr = p.communicate()
        return (p.returncode, stdout, stderr)


    def set_default_gw(self,gw):
        """ Set a new default gw
        @return: True/False on Success/Fail
        """
        if self.is_valid_ipv4(gw):
            ret,out,err = self.cmd_wrapper("route change -p 0.0.0.0 mask 0.0.0.0 %s" % (gw))
            if ret == 0:
                return True
            else:
                return False
        else:
            return False