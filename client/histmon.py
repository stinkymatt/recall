# histmon.py
#
# Follow a file like tail -f.
# credit to for tail functionality:
# http://stackoverflow.com/questions/5419888/reading-from-a-frequently-updated-file

import sys
import os
import time
import requests
import json

def follow(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

def submit_command(**com):
	dest_url = "http://localhost:8888"
	data = json.dumps(com)
	r = requests.post(dest_url, data)


if __name__ == '__main__':
	#http://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
	tzoffset = (time.timezone if (time.localtime().tm_isdst == 0) else time.altzone) / 60 / 60 * -1
	histf = os.path.basename(sys.argv[1])
	hostn = histf[5:-15] # should I pull this from the actual hostname?
	histd = histf[-14:-4] # should I change this to pull the actual day?
	logfile = open(sys.argv[1],"r")
	loglines = follow(logfile)
	ts = ""
	for line in loglines:
		if line[0] == '#':
			ts = line[1:-1]
		else:
			print hostn,histd,ts,tzoffset,line[:-1]
			submit_command(hostname=hostn, cmddate=histd,cmdts=ts,cmdtz=tzoffset,cmd=line[:-1])
