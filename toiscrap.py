import urllib
import re
import subprocess
import time
import sys


allurls = []
mon = 1
sttime = 39965
url = "http://timesofindia.indiatimes.com/2009/1/1/archivelist/year-2009,month-" + str(mon) + ",starttime-"+ str(sttime) + ".cms"
for i in xrange(31):
	url = "http://timesofindia.indiatimes.com/2009/1/1/archivelist/year-2009,month-" + str(mon) + ",starttime-"+ str(sttime) + ".cms"
	allurls.append(url)
	sttime+=1
target = open("data.txt",'w')
for urls in allurls:
	# urls = "http://timesofindia.indiatimes.com/2017/1/1/archivelist/year-2017,month-1,starttime-42736.cms"

	these_regex = "January(.*)contentboxhead2"
	pattern = re.compile(these_regex)
	htmlfile=urllib.urlopen(urls)
	htmltext=htmlfile.read()
	replaced1 = re.sub("\n", " ",htmltext)
	titles=re.findall(pattern,replaced1)

	regex1 = "<a href=\"(.+?)\""
	pattern = re.compile(regex1)
	titles1=re.findall(pattern,titles[0])
	i=0
	j=0
	while i < len(titles1):
		print titles1[i]
		# i+=1
		print("\n\n\n\n")
		urls = titles1[i]
		these_regex = "\"Normal\">(.+)<\/artte"
		pattern = re.compile(these_regex)
		htmlfile=urllib.urlopen(urls)
		htmltext=htmlfile.read()
		replaced = re.sub("\n", " ",htmltext)
		titles = re.findall(pattern,replaced)
		if(len(titles)==0):
			print "Error in %d...trying again"%i
			j+=1
		else:
			replaced = re.sub("<[^>]*>","",titles[0]) 
			print replaced
			print("\n\ni is : %d\n\n"%i)
			target.write(replaced)
			target.write("\n\n")
			i+=1
		if j>=3:
			print("\n\n")
			i+=1
target.close()
