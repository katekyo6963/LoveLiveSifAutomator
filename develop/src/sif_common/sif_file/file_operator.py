import re

class FileOperator():

    """
    譜面データからBPMと譜面データを取得します
    """
    def fumen_reader(self, sifumen_data):
        fumen = ""
        with open(sifumen_data, 'r', encoding="utf-8_sig") as lines:
            for line in lines:
                if line[0] == "[":
                    # 何もしない
                    pass
                elif "bpm=" in line:
                    bpm = re.sub("\\D", "", line)
                else:
                    fumen += line.rstrip()
        return fumen, bpm