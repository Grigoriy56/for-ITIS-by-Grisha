import sys
from client import Client

if __name__ == '__main__':
    print(sys.argv)
    a = Client(sys.argv[1])
    a.loop()