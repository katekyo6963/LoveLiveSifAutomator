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

def live_operator(fumen, slp):
    for i in range(len(fumen)):
        if fumen[i] != "-":
            # btn tap
            time.sleep(1)
        else:
            time.sleep(slp)
