import csv,re,datetime
import calendar
import sys

import rrdtool

def monthNum(mnt):
    if(mnt == 'Jan'):
        return 1
    elif(mnt == 'Feb'):
        return 2
    elif(mnt == 'Mar'):
        return 3
    elif(mnt == 'Apr'):
        return 4
    elif(mnt == 'May'):
        return 5
    elif(mnt == 'Jun'):
        return 6
    elif(mnt == 'Jul'):
        return 7
    elif(mnt == 'Aug'):
        return 8
    elif(mnt == 'Sep'):
        return 9
    elif(mnt == 'Oct'):
        return 10
    elif(mnt == 'Nov'):
        return 11
    elif(mnt == 'Dec'):
        return 12
    else:
        return -1

datafile = open('coe_power_dat.csv',"rb")
reader = csv.reader(datafile)

headers = []
rawdata = []

rownum = 0
for row in reader:
    if rownum == 0:
        headers = row
    else:
        colnum = 0
        rawdata.append(row)
    rownum += 1

datafile.close

#data is an array of arrays.  Each array contains all the data from one row
data = []

for datarow in rawdata:
    dat = []

    rawdate = datarow[0]
    timef = re.split(r'\W',rawdate) 
    mn = monthNum(timef[2])
    yr = (int)(timef[3])
    dy = (int)(timef[1])
    hr = (int)(timef[4])
    sc = (int)(timef[5])
    datet = datetime.datetime(yr,mn,dy,hr,sc)
    timesp = calendar.timegm(datet.utctimetuple())
    dat.append(timesp)

    colnum = 0
    for d in datarow:
        if colnum != 0:
            dat.append(d)
        colnum += 1
    print dat
    data.append(dat)


datasources = []
rras = []
num = 0
for h in headers:
    if num != 0:
        datasources.append('DS:' + h + ':GAUGE:1800:U:U')
    num += 1



rrdtool.create('engraph.rrd','--start','1314836999','--step','1800',
               datasources,
               'RRA:AVERAGE:0.5:1:2400')

nxs = 0
for r in data:
    
    t = str(r[0])+':'+str(r[1])+':'+str(r[2])+':'+str(r[3])+':'+str(r[4])
    print t
    rrdtool.update('engraph.rrd',t)
    
