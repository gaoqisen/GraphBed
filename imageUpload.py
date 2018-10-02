#!/usr/bin/python
import os
import time

def txt(text):
        file = open('github_image_path.txt','w')
        file.write(text)
        file.close()
        os.system('open github_image_path.txt')
        os.system('say "ok"')

# create file
dir=time.strftime("%Y%m", time.localtime())
fileName=dir+'/'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.png'
path='/Users/gaoqisen/Documents/blog/image/GraphBed/'
if not os.path.exists(path+dir):
        os.makedirs(path+dir)
# screencapture
upload=os.system('screencapture -i '+path+fileName)


if(upload==0):
        adds='cd '+path+' ; git add .'
        print(adds)
        add=os.system(adds)
	print(add)
        os.system('cd '+path+' ; git commit -m "'+fileName+' add"')
        os.system('cd '+path+' ; git push origin master')
        str='https://gaoqisen.github.io/GraphBed/'+fileName
        txt(str)
