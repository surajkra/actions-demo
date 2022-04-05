import os
import sys
import pprint

if __name__=="__main__":
  print("Hi there from Python")
  #print(os.environ["UBUNTU_SERVER"])
  pprint(dict(os.environ))
