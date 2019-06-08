

def fumen_reader(sifumen_data):
    fumen = ""
    with open(sifumen_data, 'r', encoding="utf-8_sig") as lines:
        for line in lines:
            if line[0] == "[":
                # 何もしない
                pass
            else:
                fumen += line.rstrip()
    
    return fumen