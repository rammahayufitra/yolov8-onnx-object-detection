import configparser
import ast
import sys

config = configparser.ConfigParser() 
print(sys.argv)
if sys.argv[1] == "1":
    config.read("./public/config1.cfg")
elif sys.argv[1] == "2":
    config.read("/.opt/public/config2.cfg")
elif sys.argv[1] == "3":
    config.read("/.opt/public/config3.cfg")
elif sys.argv[1] == "4":
    config.read("/.opt/public/config4.cfg")
else:
    print("FILE CONFIG BELUM TERSEDIA")
    pass

STATUS_LATENCY = int(config['LATENCY']['STATUS_LATENCY'])

