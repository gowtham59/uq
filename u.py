f1,g2=map(int,input().split())
if(f1>g2):
  gt3=f1
else:
  gt3=g2
while(True):
  if((gt3%f1) == 0 and (gt3%g2) == 0):
    lcm=gt3
    break
  gt3=gt3+1
print(lcm)
