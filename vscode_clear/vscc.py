import os
import json
import urllib.parse

file_path = "~/.config/Code/User/workspaceStorage"


print(os.path.expanduser(file_path))

abs_path = os.path.expanduser(file_path)

if (not os.path.isdir(abs_path)):
    print("vscode工作区存储目录配置有误")
    exit(-1)

for f in os.listdir(abs_path):
    ws_dir = f
    f = open(os.path.join(abs_path, f, "workspace.json"), 'r')

    json_src = ""

    for line in f.readlines():
        json_src += line.replace('\r','').replace('\n','')
    
    
    json_src =  urllib.parse.unquote(json_src)
    # print(json_src)
    json_object =  json.loads(json_src)
    dir_name = None
    try:
        dir_name = json_object['folder']
        
        
    except KeyError:
        print("json文件解析失败, 目录为" + os.path.join(abs_path, ws_dir) )

    if (dir_name == None):
        continue
    else:
        acture_path = dir_name[7:]
        
        if (os.path.exists(acture_path) and os.path.isdir(acture_path)):
            # print("T\t" + acture_path)
            pass
        else:
            # print("F\t" + acture_path)
            invalid_path = abs_path + "/" + ws_dir
            clear_cmd = "rm -r " + invalid_path;
            print(clear_cmd)
            os.system(clear_cmd)
  

    