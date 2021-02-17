import subprocess

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.run(['strings',loc],capture_output=True,text=True)
   print(st.stdout)

strings('/home/arijit/Downloads/rocks.jpg')




