import os
import sys
import pprint

if __name__=="__main__":
  print("Hi there from Python")
  UBUNTU_SERVER = os.environ['UBUNTU_SERVER']
  POLYGON_API = os.environ['POLYGON_API_KEY']
  #print(os.environ["UBUNTU_SERVER"])
  print(UBUNTU_SERVER)
  pprint.pprint(dict(os.environ))
