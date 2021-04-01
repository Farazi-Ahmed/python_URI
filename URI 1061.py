# 1061
dia,date1=input().split()
date1 = int(date1)
h1,m1,s1=map(int,input().split(":"))

dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=map(int,input().split(":"))

timestart = (86400*date1)+(3600*h1)+(60*m1)+s1
timeend = (86400*date2)+(3600*h2)+(60*m2)+s2

duration = timeend - timestart

days = duration//86400
duration = duration%86400

hour = duration//3600
duration = duration%3600

mins = duration//60
duration = duration%60

print("%d dia(s)"%days)
print("%d hora(s)"%hour)
print("%d minuto(s)"%mins)
print("%d segundo(s)"%duration)