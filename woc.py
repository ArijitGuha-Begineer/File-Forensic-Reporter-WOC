import subprocess
import re
import os
import sys

data=sys.argv[1]
loc=os.path.abspath(data)

def fileidentification(loc):
   command=subprocess.run(['file',loc],capture_output=True,text=True)
   ans=re.findall(r'\w+',command.stdout)
   
   if('PNG' in ans):
	   import png
	   png.main(loc)


   elif('JPEG' in ans):
	   import jpg
	   jpg.main(loc)

   elif('bitmap' in ans):
	   import bmp
	   bmp.main(loc)   


   elif('ASCII'in ans):
   	   import text
   	   text.main(loc)

   elif('PDF'in ans):
   	   import pdf
   	   pdf.main(loc)

   elif('WAVE'in ans):
   	   import wav
   	   wav.main(loc)

   elif('Zip'in ans):
	   import Zip
	   Zip.main(loc)
       

   elif('Microsoft'in ans):
	    import officefiles
	    officefiles.main(loc)

   else:
	   print('file not recognisable')


fileidentification(loc)

