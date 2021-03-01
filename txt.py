import subprocess

def cat(loc):
  ct=subprocess.run(['cat',loc],capture_output=True,text=True)
  print(ct.stdout)


def strings(loc):
	st=subprocess.run(['strings',loc],capture_output=True,text=True)
	print(st.stdout)

def binwalk(loc):
	bn=subprocess.run(['binwalk',loc],capture_output=True,text=True)
	print(bn.stdout)



def main(loc):
  cat(loc)
  strings(loc)
  binwalk()


if __name__ == '__main__':
  main(loc)
