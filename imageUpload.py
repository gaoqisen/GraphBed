#!/usr/bin/python
import os
import time

def txt(text):
	print(text)
	file = open('github_image_path.txt','w')
	file.write(text)
	file.close()
	print('ok')
	os.system('open github_image_path.txt')
	os.system('say "ok"')

# create file
dir=time.strftime("%Y%m", time.localtime())
fileName=dir+'/'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.png'
path='/Users/gaoqisen/Documents/blog/image/GraphBed'
print(path+dir)
if not os.path.exists(path+dir):
        os.makedirs(path+dir)
print(path+fileName)
# screencapture
upload=os.system('screencapture -i '+path+fileName)


if(upload==0):
	os.system('git add .')
	os.system('git commit -m "'+fileName+' add"')
	os.system('git push origin master')
	str='https://gaoqisen.github.io/GraphBed/'+fileName
	txt(str)
