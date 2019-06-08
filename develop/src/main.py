"""
=========================================
 comment     : None
 param       : None
 return      : None
========================================
 Display Dpl : BlueStacks ???
=========================================
 Copy Right (C) 2019 All Right Reserved.
   @author LL_SIF_AT @kawaken1025
     Create Date : 2019/06/27
=========================================
"""


import time
import sys
from sif_common.sif_file import file_operator

args = sys.argv
# 譜面データから譜面とBPMを取得
fumen, bpm = file_operator.fumen_reader(args[1])

def live_operator(fumen, slp):
    for i in range(len(fumen)):
        if fumen[i] != "-":
            pass
        else:
            time.sleep(slp)
