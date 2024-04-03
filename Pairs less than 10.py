a=[6,3,2,5,6,7,1]
sum=0
if a[0]+a[1]<=10:
    sum+=(a[0]+a[1])
for i in range(1,len(a)-1):
    if a[i]+a[i+1]<=10:
        if a[i-1]==a[i]:
            sum+=a[i+1]
        else:
            sum+=(a[i]+a[i+1])
print(sum)