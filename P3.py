##from urllib.request import urlretrieve
import re 
i = 0 

##urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog')



log = open("testlog.txt" , "r")

## this goes through the lines, prints and counts them. 
for line in log:
    print (line)
    a = 24
    x = re.findall("(local|remote) (- -) (.{}.Oct.1994.)".format(a), line)
    print (x)
    
    ##this answers number 1
    i = i+1
    print (i)
    
    
