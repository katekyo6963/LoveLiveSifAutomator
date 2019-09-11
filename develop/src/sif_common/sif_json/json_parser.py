import json

class JsonParser():
    COORDINATE_JSON_PATH = '../conf/coordinate.json'

    """
    JSONファイルからボタン毎のタップ位置を取得して返却する
    """
    def get_btn_coordinate(self):
        json_file = open(JsonParser.COORDINATE_JSON_PATH, "r")
        json_obj = json.load(json_file)
        return json_obj['live_btn_coordinate']['tap1x'],\
               json_obj['live_btn_coordinate']['tap1y'],\
               json_obj['live_btn_coordinate']['tap2x'],\
               json_obj['live_btn_coordinate']['tap2y'],\
               json_obj['live_btn_coordinate']['tap3x'],\
               json_obj['live_btn_coordinate']['tap3y'],\
               json_obj['live_btn_coordinate']['tap4x'],\
               json_obj['live_btn_coordinate']['tap4y'],\
               json_obj['live_btn_coordinate']['tap5x'],\
               json_obj['live_btn_coordinate']['tap5y'],\
               json_obj['live_btn_coordinate']['tap6x'],\
               json_obj['live_btn_coordinate']['tap6y'],\
               json_obj['live_btn_coordinate']['tap7x'],\
               json_obj['live_btn_coordinate']['tap7y'],\
               json_obj['live_btn_coordinate']['tap8x'],\
               json_obj['live_btn_coordinate']['tap8y'],\
               json_obj['live_btn_coordinate']['tap9x'],\
               json_obj['live_btn_coordinate']['tap9y']