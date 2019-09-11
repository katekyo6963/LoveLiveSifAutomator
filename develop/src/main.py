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
from sif_util import sif_util
import sif_converter.uwsc.uwsc_global
import sif_converter.uwsc.uwsc_parser

def main():
    args = sys.argv

    # 譜面データから譜面とBPMを取得
    f_op = file_operator.FileOperator()
    fumen, bpm = f_op.fumen_reader(args[1])
    # bpmから1拍の待機時間を取得
    util = sif_util.SifUtil()
    sleep_time = util.get_beat_sleep_time(bpm)

    print(fumen)
    print(bpm)
    print("slp="+ str(sleep_time))



    # ライブ自動処理
    lo = live_operator.LiveOperator()
    print(lo.tap1x)
    # lo.live_automator(fumen, sleep_time) 
    

main()