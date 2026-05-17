import time 

m=int(input("Enter Timer(in hours):"))
m*=3600
for x in range(m,0,-1):
    s=x% 60  
    min = int(x  /60) % 60
    h=int(x/3600)
    print(f"{h:02}:{min:02}:{s:02}")
    time.sleep(1)

print("TIME UP!")
