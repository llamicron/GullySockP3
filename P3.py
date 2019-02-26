from urllib.request import urlretrieve
import re 
urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog.txt')


log = open("testlog.txt" , "r")

janlog = open("janlog.txt", "w+")
print ("janlog created")
feblog = open("feblog.txt", "w+")
print ("feblog created")
marlog = open("marlog.txt", "w+")
print ("marlog created")
aprlog = open("aprlog.txt", "w+")
print ("aprlog created")
maylog = open("maylog.txt", "w+")
print ("maylog created")
junlog = open("junlog.txt", "w+")
print ("junlog created")
jullog = open("jullog.txt", "w+")
print ("jullog created")
auglog = open("auglog.txt", "w+")
print ("auglog created")
seplog = open("seplog.txt", "w+")
print ("seplog created")
octlog = open("octlog.txt", "w+")
print ("octlog created")
novlog = open("novlog.txt", "w+")
print ("novlog created")
declog = open("declog.txt", "w+")
print ("declog created")
linenum = 0 
octnum = 0
novnum = 0
decnum = 0
jannum = 0
febnum = 0
marnum = 0
aprnum = 0
maynum = 0
junnum = 0
julnum = 0
augnum = 0
sepnum = 0
error = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0





## this goes through the lines, prints and counts them. 
for line in log:
    #print (line)
    
    
    #counts the month, and writes them to their own file
    if re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Oct\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        octnum += 1
        octlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Nov\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        novnum += 1
        novlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Dec\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        decnum += 1  
        declog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jan\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        jannum += 1 
        janlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Feb\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        febnum += 1       
        feblog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Mar\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        marnum+= 1
        marlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Apr\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        aprnum+= 1
        aprlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/May\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        maynum+= 1
        maylog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jun\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        junnum+= 1
        junlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jul\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        julnum+= 1
        jullog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Aug\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        augnum+= 1
        auglog.write(line)
        
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Sep\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        sepnum+= 1
        seplog.write(line)
    
    else:
        error += 1
        
        #counts the error codes
    if re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(3[0-9]+)( [0-9-]+)"), line): 
        cnt3 += 1
            
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(4[0-9]+)( [0-9-]+)"), line): 
        cnt4 += 1
            
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(5[0-9]+)( [0-9-]+)"), line): 
        cnt5 += 1        
           
       

    
    ##this answers number 1
    linenum = linenum + 1
    #print (linenum)

print ("The file has " , linenum, " log entries.")    
print ("October has " , octnum, " log entries.")
print ("November has " , novnum, " log entries.")
print ("December has " , decnum, " log entries.")
print ("January has " , jannum, " log entries.")
print ("Febuary has " , febnum, " log entries.")
print ("March has " , marnum, " log entries.")
print ("April has " , aprnum, " log entries.")
print ("May has " , maynum, " log entries.")
print ("June has " , junnum, " log entries.")
print ("July has " , julnum, " log entries.")
print ("August has " , augnum, " log entries.")
print ("September has " , sepnum, " log entries.")

janlog.close()
feblog.close()
marlog.close()
aprlog.close()
maylog.close()
junlog.close()
jullog.close()
auglog.close()
seplog.close()
octlog.close()
novlog.close()
declog.close()

print ("there are ", cnt3, " 3XX errors")
print ("there are ", cnt4, " 4XX errors")
print ("there are ", cnt5, " 5XX errors")
print ("there are ", error, " unusable entries")