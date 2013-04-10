import matplotlib.pyplot as plotter
import rrdtool

def plot(i_interval,i_end):
    interval = i_interval #1800
    end =   i_end #1320107400
    start = end - (interval * 48 * 7)
    data = rrdtool.fetch('engraph.rrd','AVERAGE',
                     '--start',str(start),'--end',str(end))
    kwhdata = []
    times = []
    count = 0

#get the data and times
    for d in data:
        if count > 1:
            newtime = start
            for member in d:
                newtime += interval
                times.append(newtime)
                kwhdata.append(member[0])
                      
        count += 1

    plotter.plot(times,kwhdata)
    plotter.show()

plot(1800,1320107400)
