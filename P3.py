from urllib.request import urlretrieve

urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog')

def main ():
    log = open("testlog.txt" , "r")
    for line in log:
        print (line)
    print ('caleb')
        

