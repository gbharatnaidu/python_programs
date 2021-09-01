arr1=[1,10,12,12,1,1,5,10,23,1]
arr2=[]
for i in range(0,len(arr1)):
    arr2.append(-1)

print(arr2)
for i in range(0,len(arr1)):
    count=1
    for j in range(i+1,len(arr1)):
        if(arr1[i]==arr1[j]):
            count+=1
            arr2[j]=0 
    if(arr2[i]!=0):
            arr2[i]=count

for i in range(0,len(arr1)):
    if(arr2[i]>0):
        print("no of times ",arr1[i]," is occured ",arr2[i])
        
