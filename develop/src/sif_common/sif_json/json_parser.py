import json

class JsonParser():
    COORDINATE_JSON_PATH = '../../../conf/coordinate.json'

    """
    JSONファイルからボタン毎のタップ位置を取得して返却する
    """
    def get_btn_coordinate(self):
        json_file = open(JsonParser.COORDINATE_JSON_PATH, "r")
        json_obj = json.load(json_file)
        return