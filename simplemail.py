

import os
import urllib
import urllib2
import datetime

currentime = datetime.datetime.now()

query_args = {
	'EventType' : 'Motion detected',
	'Action' : 'review monitor',
	'TimeStamp' : currentime}

#update the #name with your e-mail address
	
os.system('echo "image has been saved to http://www.lwaldtech.com" | mail -s "motion detected" name@gmail.com)

		
url = 'http://lwaldtech.com/oopsapi/API/oopsAPI/InsertOops'
query_args = urllib.urlencode(query_args)
query_args = query_args.encode('ascii')
request = urllib2.Request(url, query_args)
response = urllib2.urlopen(request).read

		

		
