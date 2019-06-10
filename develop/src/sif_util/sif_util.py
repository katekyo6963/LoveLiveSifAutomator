class SifUtil:
    
    """
    画像ファイルパスを返却します
    """
    IMG_PATH = './images/'
    def get_image_path(self, img_name):
        return SifUtil.IMG_PATH + img_name + ".png"

    """
    16分音符の1拍の待機時間を返します
    """
    def get_beat_sleep_time(self, bpm):
        if int(bpm) == 0:
            return 0

        return 15000/int(bpm)