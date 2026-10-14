time=int(input())
h=time//3600
time=time-3600*h
m=time//60
time=time-60*m
s=time
print("0"+str(h)+":0"+str(m)+":"+"0"+str(s))