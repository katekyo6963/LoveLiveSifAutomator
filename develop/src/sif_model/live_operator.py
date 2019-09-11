
"""
comment : ライブを自動操作します。
param   : $1: 譜面データ
          $2: BPM毎の1拍待機時間
"""

import time
import sif_converter.uwsc.uwsc_parser
import sif_converter.uwsc.uwsc_global
import sif_common.sif_json.json_parser
import pyautogui

class LiveOperator():
    
    # タップ座標を格納するクラス変数
    # 作った後に気づいたけど普通にここで定義すればよかったのでは？
    #   → Phase.2 以降 GUIから設定する機会があれば活用できる・・・
    tap1x = 0
    tap1y = 0
    tap2x = 0
    tap2y = 0
    tap3x = 0
    tap3y = 0
    tap4x = 0
    tap4y = 0
    tap5x = 0
    tap5y = 0
    tap6x = 0
    tap6y = 0
    tap7x = 0
    tap7y = 0
    tap8x = 0
    tap8y = 0
    tap9x = 0
    tap9y = 0
    is_double = False

    def __init__(self):
        # coordinate.jsonからタップ座標を取得
        parser = sif_common.sif_json.json_parser.JsonParser()
        LiveOperator.tap1x, LiveOperator.tap1y, LiveOperator.tap2x, LiveOperator.tap2y,\
        LiveOperator.tap3x, LiveOperator.tap3y, LiveOperator.tap4x, LiveOperator.tap4y,\
        LiveOperator.tap5x, LiveOperator.tap5y, LiveOperator.tap6x, LiveOperator.tap6y,\
        LiveOperator.tap7x, LiveOperator.tap7y, LiveOperator.tap8x, LiveOperator.tap8y,\
        LiveOperator.tap9x, LiveOperator.tap9y = parser.get_btn_coordinate()       

    def live_automator(self, fumen, slp):
        for i in range(len(fumen)):
            if fumen[i] != "-":
                pass
            else:
                time.sleep(slp)

    def live_btn_tap(self, slp, tap_num):
        # 前回タップが同時押しだったら差分-0.1秒を引く
        if LiveOperator.is_double:
            slp = (slp / 1000) - 0.1
        else:
            slp = slp / 1000
        try:
            # 単押し
            if 0 < int(tap_num) < 10:
                if tap_num == 1:
                    pyautogui.click(x=LiveOperator.tap1x, y=LiveOperator.tap1y, button="left", interval=slp)
                elif tap_num == 2:
                    pyautogui.click(x=LiveOperator.tap2x, y=LiveOperator.tap2y, button="left", interval=slp)
                elif tap_num == 3:
                    pyautogui.click(x=LiveOperator.tap3x, y=LiveOperator.tap3y, button="left", interval=slp)
                elif tap_num == 4:
                    pyautogui.click(x=LiveOperator.tap4x, y=LiveOperator.tap4y, button="left", interval=slp)
                elif tap_num == 5:
                    pyautogui.click(x=LiveOperator.tap5x, y=LiveOperator.tap5y, button="left", interval=slp)
                elif tap_num == 6:
                    pyautogui.click(x=LiveOperator.tap6x, y=LiveOperator.tap6y, button="left", interval=slp)
                elif tap_num == 7:
                    pyautogui.click(x=LiveOperator.tap7x, y=LiveOperator.tap7y, button="left", interval=slp)
                elif tap_num == 8:
                    pyautogui.click(x=LiveOperator.tap8x, y=LiveOperator.tap8y, button="left", interval=slp)
                elif tap_num == 9:
                    pyautogui.click(x=LiveOperator.tap9x, y=LiveOperator.tap9y, button="left", interval=slp)
            LiveOperator.is_double = False
        # 同時押し
        except:
            LiveOperator.is_double = True
            if tap_num == "a":
                pass
            elif tap_num == "b":
                pass
            elif tap_num == "c":
                pass
            elif tap_num == "d":
                pass
            elif tap_num == "e":
                pass
            elif tap_num == "f":
                pass
            elif tap_num == "g":
                pass
            elif tap_num == "h":
                pass
            elif tap_num == "i":
                pass
            elif tap_num == "j":
                pass
            elif tap_num == "k":
                pass
            elif tap_num == "l":
                pass
            elif tap_num == "m":
                pass
            elif tap_num == "n":
                pass
            elif tap_num == "o":
                pass
            elif tap_num == "p":
                pass
            elif tap_num == "q":
                pass
            elif tap_num == "r":
                pass
            elif tap_num == "s":
                pass
            elif tap_num == "t":
                pass
            elif tap_num == "u":
                pass
            elif tap_num == "v":
                pass
            elif tap_num == "w":
                pass
            elif tap_num == "x":
                pass
            elif tap_num == "y":
                pass
            elif tap_num == "z":
                pass
            elif tap_num == "A":
                pass
            elif tap_num == "B":
                pass
            elif tap_num == "C":
                pass
            elif tap_num == "D":
                pass
            elif tap_num == "E":
                pass
            elif tap_num == "F":
                pass
            elif tap_num == "G":
                pass
            elif tap_num == "H":
                pass
            elif tap_num == "I":
                pass
            elif tap_num == "J":
                pass

    def live_btn_double_tap(self, slp, xp, yp, xp2,yp2):
        pyautogui.click(x=xp, y=yp, button="left", interval=slp/1000)
        pyautogui.click(x=xp2, y=yp2, button="left", interval=0.1)

    def fumen_creator(self):
        fumen_list = list()
        return