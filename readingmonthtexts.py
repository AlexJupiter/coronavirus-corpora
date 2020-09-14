#Creating arrays for GB and US sources
file = open("allsources.txt", "r")
gb = []
us = []

for line in file:
	fields = line.split("	")
	if fields[3] == "GB":
		gb.append(fields[0])
	if fields[3] == "US":
		us.append(fields[0])

print "Len gb sources:"
print len(gb)
print "Len us sources:"
print len(us)

file.close()


#Jan: creating seperate Jan_GB, Jan_US, and Jan_GB&US text files
jan_file = open("jantexts.txt", "r")
jan_gb_texts = []
jan_us_texts = []

for line in jan_file:
	if line[2:10] in gb :
		jan_gb_texts.append(line)
	if line[2:10] in us :
		jan_us_texts.append(line)

print "Len jan_gb_texts:"
print len(jan_gb_texts)
print "Len jan_us_texts:"
print len(jan_us_texts) 

jan_file.close()

with open("Jan_GB.txt", "w") as txt_file:
    for line in jan_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("Jan_US.txt", "w") as txt_file:
    for line in jan_us_texts:
        txt_file.write(line) 

with open("Jan_GB&US.txt", "w") as txt_file:
    for line in jan_gb_texts:
        txt_file.write(line)
    for line in jan_us_texts:
        txt_file.write(line) 


#Feb: creating seperate Feb_GB, Feb_US, and Feb_GB&US text files
feb_file = open("febtexts.txt", "r")
feb_gb_texts = []
feb_us_texts = []

for line in feb_file:
	if line[2:10] in gb :
		feb_gb_texts.append(line)
	if line[2:10] in us :
		feb_us_texts.append(line)

print "Len feb_gb_texts:"
print len(feb_gb_texts)
print "Len feb_us_texts:"
print len(feb_us_texts) 

feb_file.close()

with open("Feb_GB.txt", "w") as txt_file:
    for line in feb_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("Feb_US.txt", "w") as txt_file:
    for line in feb_us_texts:
        txt_file.write(line) 

with open("Feb_GB&US.txt", "w") as txt_file:
    for line in feb_gb_texts:
        txt_file.write(line)
    for line in feb_us_texts:
        txt_file.write(line) 


#Mar: creating seperate Mar_GB, Mar_US, and Mar_GB&US text files
mar_file = open("martexts.txt", "r")
mar_gb_texts = []
mar_us_texts = []

for line in mar_file:
	if line[2:10] in gb :
		mar_gb_texts.append(line)
	if line[2:10] in us :
		mar_us_texts.append(line)

print "Len mar_gb_texts:"
print len(mar_gb_texts)
print "Len mar_us_texts:"
print len(mar_us_texts) 

mar_file.close()

with open("Mar_GB.txt", "w") as txt_file:
    for line in mar_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("Mar_US.txt", "w") as txt_file:
    for line in mar_us_texts:
        txt_file.write(line) 

with open("Mar_GB&US.txt", "w") as txt_file:
    for line in mar_gb_texts:
        txt_file.write(line)
    for line in mar_us_texts:
        txt_file.write(line) 


#Apr: creating seperate Apr_GB, Apr_US, and Apr_GB&US text files
apr_file = open("aprtexts.txt", "r")
apr_gb_texts = []
apr_us_texts = []

for line in apr_file:
	if line[2:10] in gb :
		apr_gb_texts.append(line)
	if line[2:10] in us :
		apr_us_texts.append(line)

print "Len apr_gb_text:"
print len(apr_gb_texts)
print "Len apr_us_texts:"
print len(apr_us_texts) 

apr_file.close()

with open("Apr_GB.txt", "w") as txt_file:
    for line in apr_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("Apr_US.txt", "w") as txt_file:
    for line in apr_us_texts:
        txt_file.write(line) 

with open("Apr_GB&US.txt", "w") as txt_file:
    for line in apr_gb_texts:
        txt_file.write(line)
    for line in apr_us_texts:
        txt_file.write(line) 


#May: creating seperate May_GB, May_US, and May_GB&US text files
may_file = open("maytexts.txt", "r")
may_gb_texts = []
may_us_texts = []

for line in may_file:
	if line[2:10] in gb :
		may_gb_texts.append(line)
	if line[2:10] in us :
		may_us_texts.append(line)

print "Len may_gb_texts:"
print len(may_gb_texts)
print "Len may_us_texts:"
print len(may_us_texts) 

may_file.close()

with open("May_GB.txt", "w") as txt_file:
    for line in may_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("May_US.txt", "w") as txt_file:
    for line in may_us_texts:
        txt_file.write(line) 

with open("May_GB&US.txt", "w") as txt_file:
    for line in may_gb_texts:
        txt_file.write(line)
    for line in may_us_texts:
        txt_file.write(line) 


#June: creating seperate Jun_GB, Jun_US, and Jun_GB&US text files
jun_file = open("juntexts.txt", "r")
jun_gb_texts = []
jun_us_texts = []

for line in jun_file:
	if line[2:10] in gb :
		jun_gb_texts.append(line)
	if line[2:10] in us :
		jun_us_texts.append(line)

print "Len jun_gb_texts:"
print len(jun_gb_texts)
print "Len jun_us_texts:"
print len(jun_us_texts) 

jun_file.close()

with open("Jun_GB.txt", "w") as txt_file:
    for line in jun_gb_texts:
        txt_file.write(line) 

#writing gbtexts to text file
with open("Jun_US.txt", "w") as txt_file:
    for line in jun_us_texts:
        txt_file.write(line) 

with open("Jun_GB&US.txt", "w") as txt_file:
    for line in jun_gb_texts:
        txt_file.write(line)
    for line in jun_us_texts:
        txt_file.write(line) 




