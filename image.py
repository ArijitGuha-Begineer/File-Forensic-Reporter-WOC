import subprocess

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.run(['strings',loc],capture_output=True,text=True)
   print(st.stdout)

def exiftool(loc):  #calling exiftool for PNG and JPG files
   ex=subprocess.run(['exiftool',loc],capture_output=True,text=True)
   print(ex.stdout)

def zsteg(loc):     #calling zsteg for PNG files
   zs=subprocess.run(['zsteg',loc],capture_output=True,text=True)
   print(zs.stdout)

loc='Enter your location of file'
def main(loc):
	strings(loc)
	exiftool(loc)
	zsteg(loc)

if __name__ == '__main__':
	main(loc)






