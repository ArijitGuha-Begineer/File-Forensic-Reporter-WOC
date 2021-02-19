import subprocess
import re
import os

def fileidentification(loc):
 command=subprocess.run(['file',loc],capture_output=True,text=True)
 text=re.findall(r"\w+",command.stdout)

 
if('PNG' in text):
	os.system('image.py')

elif('JPEG' in text):
	os.system('image.py')

else:
	print('file not recognisable')
