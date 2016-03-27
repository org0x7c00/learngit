#!/usr/bin/env python
import subprocess
cmd = ['ping','-c','5','114.114.114.114']
child = subprocess.Popen(cmd)
child.wait()

