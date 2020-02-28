import math
import matplotlib.pyplot as plt
from scipy import stats as st
import numpy as np
file1=open('x.txt')
file2=open('y.txt')
#x
x=[]
#x=[32.4,33.500,42.000,28.800,35.200,34.520,32.040,31.160,29.780,28.200,28.820,26.540,30.060,26.480,38.900,29.700,15.260,16.000,14.160,14.200,16.400,24.300,28.580,21.080,30.860,21.680,16.500,18.352,14.392,18.400]
#y=[0.34200,0.35275,0.44400,0.30600,0.37700,0.36970,0.33990,0.33010,0.31405,0.29550,0.30445,0.27715,0.32235,0.27880,0.40675,0.31275,0.16560,0.17500,0.15460,0.15450,0.17800,0.26475,0.30705,0.22530,0.32735,0.24080,0.17525,0.20152,0.15342,0.19600]
x=file1.read()

x=x.split(',')
for i in range(len(x)):
    x[i]=float(x[i])

print(x)
y=[]
y=file2.read()

y=y.split(",")
for i in range(len(y)):
   y[i]=float(y[i])
n=30
sd=np.std(x)
sample_m=np.mean(x) #power oda mean
pop_mean=50.08   #million units
Zcal=(sample_m-pop_mean)/(sd/math.sqrt(n))
#print(Zcal)
sign=0.05
table=st.norm.cdf(Zcal)
#print(table)
if(Zcal<=table):
    print('Accept Ho')
else:
    print('Reject Ho')
# this is  for power
def regression(x,y,z):
    a=sum(x)
    b=sum(y)    

    v=[]
    p=[]
    l=[]

    for i in range(len(x)):
        w=x[i]*y[i]
        v.append(w)
        
        u=x[i]*x[i]
        p.append(u)
    
        t=y[i]*y[i]
        l.append(t)
 
    c=sum(v)
    d=sum(p)
    e=sum(l)

    bo=(b*d-a*c)/(len(x)*d-a*a)
    b1=(len(x)*c-a*b)/(len(x)*d-a*a)
#print("bo=",bo)
#print("b1=",b1)
    i=0
    y2=433
    print("The equation is ",bo,"+x",b1)
    if(z==1):
        while(y2>0):
            #if(y2<=0):
                #print('po')
                #break
            #else;
                y1=bo+(i*b1)
                y2=y2-y1
                i=i+1
        print('The coal will last for ',i,'i.e year:',2017+i)
# For an 100% efficient plant , 900g is enough to produce 1 unit of current
# NLC uses 1kg to produce 1 unit of current
#regression(x,y,0)
calorie_value=9000 #(in Kcal/kg)
Power=22.340   #(MW)
coal_consumed=276.21    #lakh-tons

efficiency=(Power*100000/(coal_consumed*calorie_value))*100
print('efficiency')
print(efficiency)
year=[1,2,3,4,5,6,7]
lignite=[18.17,18.37,18.62,20.56,21.57,20.44,21.01]
regression(year,lignite,1)
plt.figure()
label=[2011,2012,2013,2014,2015,2016,2017]
demand=[85686,92302,93465,94650,95230,95789,96789]
nlc_power=[18789.4,19902.34,19988.65,19729.13,19182.21,22340.59,23456.9]
#plt.bar(demand,year)
index = np.arange(len(label))

a=plt.bar(index-0.2,demand,width=0.2,color='skyblue')
plt.xticks(index,label)

b=plt.bar(index+0.2,nlc_power,width=0.2)
plt.xticks(index,label)
plt.xlabel('YEAR')
plt.legend((a[0],b[0]),('Demand of TN','Power produced by NLC'))
plt.ylabel('Demand of TN & NLC power production')
plt.figure()

percapita=[1000,1080,1040,1065,960,1011,1200]
plt.bar(index-0.2,percapita,width=0.2,color='blue')
plt.xticks(index,label)
plt.xlabel('YEAR')
plt.ylabel('PerCapita Consumption (KWh)')
plt.figure();
labels='coal','nuclear','hydro','res','others'
sizes=[10075.10,986,2182,8423,1437]
colorss=['gold','yellow','blue','pink']
plt.pie(sizes,labels=labels,colors=colorss)
plt.axis('equal')