import subprocess

def cat(loc):
  ct=subprocess.run(['cat',loc],capture_output=True,text=True)
  print(ct.stdout)


def strings(loc):
	st=subprocess.run(['strings',loc],capture_output=True,text=True)
	print(st.stdout)


def main(loc):
  cat(loc)
  strings(loc)


if __name__ == '__main__':
  main(loc)