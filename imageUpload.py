#!/usr/bin/python
import os
import time
def txt(text):
	file = open('github_image_path.txt','w')
	file.write(text)
	file.close()
	print('ok')
	os.system('open github_image_path.txt')
	

fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())+'.png'
print(fileName)
upload=os.system('screencapture -i '+fileName)
print(upload)
if(upload==0):
	print('success')
	os.system('git add .')
	os.system('git commit -m "'+fileName+' add"')
	os.system('git push origin master')
	str='https://gaoqisen.github.io/GraphBed/'+fileName
	print(str)
	txt(str)
	print('end')
