import subprocess
import re


def fileidentification(loc):
   command=subprocess.run(['file',loc],capture_output=True,text=True)
   ans=re.findall(r'\w+',command.stdout)
   
   if('PNG' in ans):
	   import image.py
	   image.py.main(loc)


   elif('JPEG' in ans):
	   import image.py
	   image.py.main(loc)
	

   else:
	   print('file not recognisable')

