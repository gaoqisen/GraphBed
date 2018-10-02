#!/usr/bin/python
import os
import time
def txt(text):
	file = open('github_image_path.txt','w')
	file.write(text)
	file.close()
	print('ok')
	os.system('open github_image_path.txt')
	os.system('say "ok"')

dir=time.strftime("%Y%m", time.localtime())
fileName=dir+'/'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.png'
if not os.path.exists(dir):
        os.makedirs(dir)
print(fileName)
upload=os.system('screencapture -i '+fileName)
print(upload)
if(upload==0):
	os.system('git add .')
	os.system('git commit -m "'+fileName+' add"')
	os.system('git push origin master')
	str='https://gaoqisen.github.io/GraphBed/'+fileName
	txt(str)
