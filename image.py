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

def binwalk(loc):
	bn=subprocess.run(['binwalk -e',loc],shell=True,capture_output=True,text=True)
	print(bn.stdout)

def stegseek(loc):
	sk=subprocess.run(['stegseek',loc,'enter your wordlist.txt'],capture_output=True,text=True)
    print(sk.stdout)

loc=''
def main(loc):
	strings(loc)
	exiftool(loc)
	zsteg(loc)
	binwalk(loc)
	stegseek(loc)

if __name__ == '__main__':
	main(loc)







