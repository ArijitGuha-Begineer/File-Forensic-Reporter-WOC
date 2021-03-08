import subprocess
import re

loc='/home/arijit/Downloads/task.zip'
def fileidentification(loc):
   command=subprocess.run(['file',loc],capture_output=True,text=True)
   ans=re.findall(r'\w+',command.stdout)
   
   if('PNG' in ans):
	   import image
	   image.main(loc)


   elif('JPEG' in ans):
	   import image
	   image.main(loc)


   elif('ASCII text'in ans):
   	   import txt
   	   txt.main(loc)

   elif('PDF'in ans):
   	   import pdf
   	   pdf.main(loc)

   elif('WAVE'in ans):
   	   import wav
   	   wav.main(loc)

   elif('Zip'in ans):
         import zip

	

   else:
	   print('file not recognisable')


fileidentification(loc)


