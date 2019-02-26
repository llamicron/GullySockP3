My program uses url retrieve to grab a log file from the interntet, which it then names awslog.
Awslog is then opened, as are 12 more text files, cooresponding to the 12 months of the year.
The file parses through each of the lines of awslog, checks for the month it belongs to, increments that month, and then adds that line to the coorespnding file. 