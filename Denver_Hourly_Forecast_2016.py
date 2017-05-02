from forecastiopy import *
import csv
import os
import pandas as pd
import datetime
import time

# Get API key from Dark Sky
apikey = 'some value'
 
Denver = [39.742043, -104.991531, 1480575600]
Denver_Time = 1451606400
 
fio = ForecastIO.ForecastIO(apikey,
                            latitude=Denver[0],
                            longitude=Denver[1],
                            time=str(Denver[2])) 
print 'Latitude', fio.latitude, 'Longitude', fio.longitude
print 'Timezone', fio.timezone
print fio.get_url() # You might want to see the request url
print

req_list = {}
# Change b_mth from 1 to 12 to indicate month
b_mth = '12/'
# Change second variable in range() to 32 for Jan, Mar, May, Jul, Aug, Oct, and Dec months
# Change second variable in range() to 31 for Apr, Jun, Sep and Nov months.
# Change second variable in range() to 30 for Feb.
for b_day in range(1,32):
    dt = datetime.datetime(2016, 12, b_day, 0, 0)
    req_list[b_mth + str(b_day) + '/2016'] = int((time.mktime(dt.timetuple())))
#print(req_list)
sortedReqList = sorted(req_list.items())
#for i in sortedReqList:
#    print(i)
    
columns = ['Date', 'Hour', 'apparentTemperature', 'cloudCover', 'humidity', 'temperature', 'time', 'visibility', 'windSpeed']
index = ['Row']
dF = pd.DataFrame(columns = columns, index = index)
dF1= pd.DataFrame(columns = columns, index = index)
# Change filename to reflect month
csv_file = "C:\Temp\Denver_Dec_Hourly_2016_Forecast.csv"
#print(type(dF))
for req_day in sortedReqList:
    Denver_Time = req_day[1]
    fio = ForecastIO.ForecastIO(apikey,
                            latitude=Denver[0],
                            longitude=Denver[1],
                            time=str(Denver_Time))

    if fio.has_hourly() is True:
        hourly = FIOHourly.FIOHourly(fio)
        print 'Hourly'
        print 'Summary:' #, hourly.summary
        print 'Icon:' #, hourly.icon
        print
        for hour in xrange(0, hourly.hours()):
            print 'Hour', hour+1
            for item in hourly.get_hour(hour).keys():
                print item + ' : ' + str(hourly.get_hour(hour)[item])
                dF['Date'] = req_day[0]
                dF['Hour'] = int(hour)
                if item == 'time':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'cloudCover':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'temperature':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'apparentTemperature':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'windSpeed':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'humidity':
                    dF[str(item)] = hourly.get_hour(hour)[item]
                if item == 'visibility':
                    dF[str(item)] = hourly.get_hour(hour)[item]
            dF1 = dF1.append(dF)   
    else:
        print 'No Hourly data'

#print dF

#save to csv_file
dF1.to_csv(csv_file, sep=',')

new_dF = pd.read_csv(csv_file,index_col=0)
print new_dF
