#!/usr/bin/env python 
import time
import subprocess
headdic = {}
headdic["layout"] = "post"
headdic["date"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))
nametitle = raw_input("File name (Example ***-***-):\n")
headdic["title"] = raw_input("Blog title:\n")
headdic["categories"] = raw_input("Categories:\n")

text ='---\n'+"\n".join(["%s : %s" %(k,v) for k,v in headdic.items()]) + '\n---'
mkname = headdic["date"] + '-'+nametitle+'.markdown'

f = open(mkname,'w+') 
f.write(text)
f.close()
subprocess.call(["subl",mkname])