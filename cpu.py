#!/usr/bin/env python 
from __future__ import print_function
from collections import OrderedDict
import pprint

def CPU_info():
    CPU_info = OrderedDict()
    procinfo = OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                CPU_info['proc%s' % nprocs] = procinfo
                nprocs +=1
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return CPU_info


if '__main__' == __name__:
    CPU_info = CPU_info()
    for processor in CPU_info.keys():
        print(CPU_info[processor]['model name'])
