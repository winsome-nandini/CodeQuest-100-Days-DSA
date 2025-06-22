l=list(map(float,input("Enter sensor readings:").split()))
mean=sum(l)/len(l)
var=0
for i in l:
    var+=((mean-i)**2)/len(l)
print("Average:",mean,"\nVariance:",var,"\nStandard Deviation:",var**0.5)