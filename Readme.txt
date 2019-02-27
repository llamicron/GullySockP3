My program uses url retrieve to grab a log file from the interntet, which it then names awslog.
Awslog is then opened, as are 12 more text files, cooresponding to the 12 months of the year.
The file parses through each of the lines of awslog, checks for the month it belongs to, increments that month, and then adds that line to the coorespnding file. 
After the program completes its first cycle it will prompt the user to decide whether or not they want to pick a day, and find out how many log entries there were on that day. The user must stick strictly to the date formatting provided. 