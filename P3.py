from urllib.request import urlretrieve
import re 

urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog')


log = open("testlog.txt" , "r")



for line in log:
    print (line)
