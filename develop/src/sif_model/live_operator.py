
"""
comment : ライブを自動操作します。
param   : $1: 譜面データ
          $2: BPM毎の1拍待機時間
"""

import time

class LiveOperator():

    def live_operator(self, fumen, slp):
        for i in range(len(fumen)):
            if fumen[i] != "-":
                pass
            else:
                time.sleep(slp)
