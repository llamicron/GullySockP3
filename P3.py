##from urllib.request import urlretrieve
import re 
linenum = 0 
day = 1
months = ["error", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

##urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog')



log = open("testlog.txt" , "r")

## this goes through the lines, prints and counts them. 
for line in log:
    ##print (line)
    
    if re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Oct\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9]+)"), line):
        print (line)    
                
       
    
    ##this answers number 1
    linenum = linenum+1
    print (linenum)
    
    
