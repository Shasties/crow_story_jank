import json, os, shutil

def main():
    save_path = ""
    level=""
    with open("./config.json") as f:
        j = json.load(f)
        save_path = j['save_path']
        level = j['level'].upper()
    save_dir = '\\'.join(save_path.split('\\')[:-1])
    backup_path = save_dir + "\\Slot0.bak"
    temp_path = save_dir + "\\Slot0.tmp"
    reset_bytes = [1333,1334,1335,1336,1414]
    if not os.path.exists(backup_path):
        shutil.copyfile(save_path,backup_path)
    if os.path.exists(temp_path):
        os.remove(temp_path)
    with open(backup_path,'rb') as f:
        with open(temp_path,'ab') as g:
            for i in range(2182):
                byte = f.read(1)
                if i in reset_bytes:
                    g.write(b'\x00')
                elif i == 1337:
                    g.write(b'\x30')
                else:
                    g.write(byte)
            lb = b'\x41\x31'
            if level == "A2":
                lb = b'\x41\x32'
            elif level == "A3":
                lb = b'\x41\x33'
            #elif level == "ATOP":
            #    lb = b'\x41\x54\x6F\x70'
            elif level == "B1":
                lb = b'\x42\x31'
            elif level == "B2":
                lb = b'\x42\x32'
            elif level == "B3":
                lb = b'\x42\x33'
            #elif level == "BTOP":
            #    lb = b'\x42\x54\x6F\x70' 
            #elif level == "BBOSS":
            #    lb = b'\x42\x42\x6F\x73\x73'               
            level_bytes = b'\x4C\x65\x76\x65\x6C\x5F'+lb
            ender = b'\x00\x05\x00\x00\x00\x4E\x6F\x6E\x65\x00\x05\x00\x00\x00\x4E\x6F\x6E\x65\x00\x00\x00\x00\x00'
            g.write(level_bytes)
            g.write(ender)
    shutil.copy(temp_path,save_path)

    


                

 


if __name__ == "__main__":
    main()