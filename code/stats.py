#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

total = 0
listofnumbers=[]
candidates=[]
rowcount=0
mean=0
median=0
stddev=0
new_min=0
new_max=1
contents=[]

def minimum(numbers):
    minval=99999999
    for value in numbers:
        if value<minval:
            minval=value
    return minval

def maximum(numbers):
    maxval=0
    for value in numbers:
        if value>maxval:
            maxval=value
    return maxval

def calMean(numbers):
    total=0
    for number in numbers:
        total+=number
    count=len(numbers)
    mean=total/count
    return mean

def calMedian(numbers):
    numbers.sort()
    count=len(numbers)
    if count%2==0:
        median=numbers[(count/2)-2]
    else:
        median=numbers[(count+1)/2-1]
    return median

def stddev(mean,listofnumbers):
    sigma=0
    for value in listofnumbers:
        sigma+=(value-mean)**2
        
    stddeval=(sigma/rowcount)**0.5
    return stddeval

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normalzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    new_max=1
    new_min=0
    norm = (value-minval)/(maxval-minval)
    norm=norm*(new_max-new_min)+new_min
    return norm

def zscore(value,mean,stdDev):
    zee=(value-mean)/stdDev
    return zee

def statspercand():
    candStats={}
    for row in csv.reader(fileinput.input()):
        if not fileinput.isfirstline():
            if(row[2] in candStats.keys()):
                #Candidate: List of values
                candStats[row[2]].append(float(row[9]))
            else:
                candStats[row[2]]=[]
                candStats[row[2]].append(float(row[9]))
    
    for each in candStats.keys():
        print "Stats for "+str(each)+" *************************"
        values=[]
        total=0
        values=candStats[each]
        for value in values:
            total+=value 
        minval=minimum(values)
        maxval=maximum(values) 
        mean=calMean(values)
        median=calMedian(values)
        stdDev=stddev(mean,values)
        
        print "Total: %s" % total
        print "Minimum: " +str(minval)
        print "Maximum: " +str(maxval)
        print "Mean: " +str(mean)
        print "Median: " +str(median)
        print "Standard Deviation: " +str(stdDev)
    


for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])
        rowcount+=1
        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
        if row[2] not in candidates:
            candidates.append(row[2])

        listofnumbers.append(float(row[9]))
        
minval=minimum(listofnumbers)
maxval=maximum(listofnumbers)
mean=calMean(listofnumbers)
median=calMedian(listofnumbers)
stdDev=stddev(mean,listofnumbers)
##### Print out the stats
print "Total: %s" % total
print "Minimum: " +str(minval)
print "Maximum: " +str(maxval)
print "Mean: " +str(mean)
print "Median: " +str(median)
print "Standard Deviation: " +str(stdDev)
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])
##### Comma separated list of unique candidate names
print "Candidates: " + str(candidates)
#### Z-Scores of some values
values=[2500, 50, 250, 35, 8, 100, 19]
meanses=[mean]*len(values)
stdDevs=[stdDev]*len(values)
print "Z-score of the values: %r" % map(zscore,values,meanses,stdDevs)
     
print "Candidate Statistics"        
statspercand()



'''
Sample Output:

priya@ubuntu:~/Documents/Data Mining$ python stats.py CA.csv
Total: 146858886.14
Minimum: -30000.0
Maximum: 30000.0
Mean: 168.685431492
Median: 50.0
Standard Deviation: 438.307269816
Min-max normalized values: [0.5416666666666666, 0.5008333333333334, 0.5041666666666667, 0.5005833333333334, 0.5001333333333333, 0.5016666666666667, 0.5003166666666666]
Candidates: ['Obama, Barack', 'Gingrich, Newt', 'Pawlenty, Timothy', 'Johnson, Gary Earl', 'Bachmann, Michele', 'Romney, Mitt', 'Paul, Ron', 'Perry, Rick', 'McCotter, Thaddeus G', "Roemer, Charles E. 'Buddy' III", 'Cain, Herman', 'Huntsman, Jon', 'Santorum, Rick', 'Stein, Jill']
Z-score of the values: [5.318904633925753, -0.27078134373938056, 0.1855195523965487, -0.30500391094957524, -0.3666045319279257, -0.15670611970539824, -0.34150798264044957]
Candidate Statistics
Stats for Huntsman, Jon *************************
Total: 405345.0
Minimum: -2500.0
Maximum: 5000.0
Mean: 830.625
Median: 250.0
Standard Deviation: 23.5908297936
Stats for Cain, Herman *************************
Total: 565445.91
Minimum: -2500.0
Maximum: 5000.0
Mean: 354.289417293
Median: 250.0
Standard Deviation: 21.8069652692
Stats for Gingrich, Newt *************************
Total: 1233163.51
Minimum: -5000.0
Maximum: 5000.0
Mean: 221.31434135
Median: 100.0
Standard Deviation: 47.7652498732
Stats for Obama, Barack *************************
Total: 91715283.62
Minimum: -25800.0
Maximum: 25800.0
Mean: 126.626099158
Median: 50.0
Standard Deviation: 298.470945764
Stats for Johnson, Gary Earl *************************
Total: 202336.67
Minimum: 0.88
Maximum: 2500.0
Mean: 431.421471215
Median: 250.0
Standard Deviation: 14.5473006585
Stats for Stein, Jill *************************
Total: 52304.47
Minimum: -250.0
Maximum: 2500.0
Mean: 281.206827957
Median: 250.0
Standard Deviation: 5.40105218511
Stats for Romney, Mitt *************************
Total: 46012305.74
Minimum: -30000.0
Maximum: 30000.0
Mean: 420.05409708
Median: 100.0
Standard Deviation: 278.199082114
Stats for Bachmann, Michele *************************
Total: 358764.02
Minimum: -1500.0
Maximum: 5000.0
Mean: 190.629128587
Median: 100.0
Standard Deviation: 15.3894348527
Stats for McCotter, Thaddeus G *************************
Total: 1030.0
Minimum: 25.0
Maximum: 500.0
Mean: 257.5
Median: 25.0
Standard Deviation: 0.36015025187
Stats for Santorum, Rick *************************
Total: 975543.12
Minimum: -5000.0
Maximum: 5000.0
Mean: 194.758059493
Median: 100.0
Standard Deviation: 34.7192560679
Stats for Roemer, Charles E. 'Buddy' III *************************
Total: 38646.17
Minimum: -100.0
Maximum: 100.0
Mean: 57.0844460857
Median: 50.0
Standard Deviation: 1.13283533264
Stats for Perry, Rick *************************
Total: 1585080.6
Minimum: -2500.0
Maximum: 5000.0
Mean: 1244.17629513
Median: 1000.0
Standard Deviation: 51.1423255318
Stats for Paul, Ron *************************
Total: 2940807.31
Minimum: -2500.0
Maximum: 5000.0
Mean: 155.31886078
Median: 100.0
Standard Deviation: 42.9764971991
Stats for Pawlenty, Timothy *************************
Total: 772830.0
Minimum: -5000.0
Maximum: 10000.0
Mean: 1139.86725664
Median: 2000.0
Standard Deviation: 62.7633699615

'''
            
