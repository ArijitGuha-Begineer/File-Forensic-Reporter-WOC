import subprocess

loc='/home/arijit/Downloads/substitution2.txt'

def cat(loc):
  st=subprocess.Popen(['cat',loc],stdout=subprocess.PIPE)
  output=st.communicate()
  print(output)

def strings(loc):
  import image
  image.strings(loc)

def binwalk(loc):
  import image
  image.binwalk(loc)

def xxd(loc):
  import image
  image.xxd(loc)

def main(loc):
  strings(loc)
  strings(loc)
  binwalk(loc)
  xxd(loc)
if __name__ == '__main__':
  main(loc)
