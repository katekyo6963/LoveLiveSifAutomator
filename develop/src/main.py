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

import sys
import sif_common.messages
from sif_common.sif_file import file_operator
from sif_model import live_operator

def main():
    args = sys.argv

    # 譜面データから譜面とBPMを取得
    f_op = file_operator.FileOperator()
    fumen, bpm = f_op.fumen_reader(args[1])

    print(fumen)
    print(bpm)

main()