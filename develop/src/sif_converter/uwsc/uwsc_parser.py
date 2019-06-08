"""
=========================================
 Comment     : UWSCの関数をなるべくそのまま
 　　　　　　　 使えるようにしたクラス
=========================================
 Display Dpl : 
=========================================
 Copy Right (C) 2019 All Right Reserved.
   @author LL_SIF_AT @kawaken1025
     Create Date : 2019/06/08
=========================================
"""
import pyautogui
import cv2
import win32gui
import pyperclip
import math
from datetime import datetime
import uwsc_grobal as ug
import subprocess


class UWSCparser:

    """
    Comment : UWSC準拠のKBD関数
    Param   : $1 : self
              $2 : 押すキー文字列
              $3 : キーを押すタイプ 0 = 1回 , 1 = 押しっぱなし, 2 = 離す
              $4 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def KBD(self, key, type, ms):
        sec = ms / 1000 # ミリ秒から秒へ変換
        if type == 0:
            pyautogui.press(  key, interval = sec)
        elif type == 1:
            pyautogui.keyDown(key)
        elif type == 2:
            pyautogui.keyUp(key)





    """
    Comment : UWSC準拠のBTN関数
    Param   : $1 : self
              $2 : 押すマウスの方向文字列(right or left)
              $3 : キーを押すタイプ 0 = 1回 , 1 = 押しっぱなし, 2 = 離す
              $4 : 押すx座標
              $5 : 押すy座標
              $6 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def BTN(self, key, type, xs, ys, ms):
        sec = ms / 1000 # ミリ秒から秒へ変換
        pyautogui.click(x=xs, y=ys, button=key, interval=sec)






    """
    Comment : UWSC準拠の1回クリック専用BTN関数
    Param   : $1 : self
              $2 : 押すマウスの方向文字列(right or left)
              $3 : 押すx座標
              $4 : 押すy座標
              $5 : 前回命令から何ミリ秒に押すか
    Return  : None
    備考    :
    """
    def BTN_CLICK(self, key, xs, ys, ms):
        sec = ms / 1000 # ミリ秒から秒へ変換
        pyautogui.click(x=xs, y=ys, button=key, interval=sec)






    """
    Comment : UWSC準拠の画像認識関数(完全一致)
    Param   : $1 : self
              $2 : 認識対象となる画像のパス
              $3 : 使ってない
              $4 : 開始x座標
              $5 : 開始y座標
              $6 : 終了x座標
              $7 : 終了y座標
    Return  : 完全一致する画像があった   : True
              完全一致する画像がなかった : False
    備考    :
    """
    def chkimg(self, picPath, transFlag, x1, y1, x2, y2):
        im = pyautogui.locateOnScreen(picPath, region=(x1 , y1, x2, y2))
        if im is None:
            return False
        else:
            x, y = pyautogui.center(im)
            ug.G_IMG_X = x
            ug.G_IMG_Y = y 
            return True






    """
    Comment : UWSC準拠の画像認識関数(テンプレートマッチング)
    Param   : $1 : self
              $2 : 認識対象となる画像のパス
              $3 : 使ってない
              $4 : 開始x座標
              $5 : 開始y座標
              $6 : 終了x座標
              $7 : 終了y座標
              $8 : あいまいさ 0.0 ~ 1.0
    Return  : 完全一致する画像があった   : True
              完全一致する画像がなかった : False
    備考    :
    """
    def chkimgx(self, picPath, transFlag, x1, y1, x2, y2, threshold):
        im = pyautogui.locateOnScreen(picPath, region=(x1 , y1, x2, y2), confidence=threshold)
        if im is None:
            return False
        else:
            x, y = pyautogui.center(im)
            ug.G_IMGX_X = x
            ug.G_IMGX_Y = y 
            return True


    """
    Comment : クリップボードへ文字列をコピー
    Param   : $1 : self
              $2 : コピーしたい文字列
    Return  : None
    備考    :
    """
    def SENDSTR(self, copyStr):
        pyperclip.copy(copyStr)



    """
    Comment : コマンドプロンプトからコマンドを実行する
    Param   : $1 : self
              $2 : 実行したいコマンド文字列
    Return  : None
    備考    : コマンドの終了は待たない
    """   
    def DOSCMD(self, cmd):
        ret = subprocess.Popen(cmd, shell=True)




    """
    Comment : 現在時刻を取得します
              また取得した時刻はグローバル変数に代入されます
    Param   : $1 : self
    Return  : 現在時刻
    備考    : format : 1970-01-01 00:00:00
    """
    def GETTIME(self):
        now = datetime.now()
        ug.G_TIME_YY = now.year
        ug.G_TIME_MM = now.month
        ug.G_TIME_DD = now.day
        ug.G_TIME_HH = now.hour
        ug.G_TIME_NN = now.minute
        ug.G_TIME_SS = now.second
        ug.G_TIME_ZZ = math.floor(now.microsecond/1000)
        return now



    """
    Comment : 引数で
    Param   : $1 : self
              $2 : 取得したいx秒後の時間
    Return  : 現在時刻 + $2 の時間
    備考    : format : 1970-01-01 00:00:00
    """
    def GETTIME_AFTER(self, afterSecondTime):
        now = datetime.now()
        afterTime = now + datetime.timedelta(seconds=afterSecondTime)
        ug.G_TIME_YY = now.year
        ug.G_TIME_MM = now.month
        ug.G_TIME_DD = now.day
        ug.G_TIME_HH = now.hour
        ug.G_TIME_NN = now.minute
        ug.G_TIME_SS = now.second
        ug.G_TIME_ZZ = math.floor(now.microsecond/1000)
        return afterTime






