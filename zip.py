import zipfile
import subprocess

loc='/home/arijit/Downloads/TRUMP.zip'




try:
	    with zipfile.ZipFile(loc,'r') as my_zip:
	    	my_zip.extractall(loc)

except:
	   data=subprocess.Popen(['fcrackzip','-u','-D','-p','/home/arijit/Downloads/rockyou.txt',loc],stdout=subprocess.PIPE)
	   output=data.communicate()[0]
	   with open("Report.md","a+b") as f:
		   f.write(output)
		   f.close()



	

