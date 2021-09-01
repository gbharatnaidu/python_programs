#Move all the negative elements to one side of the array
arr=[1, -1, 3, 2, -7, -5, 11, 6]

for i in range(0,len(arr)):
    if(arr[i]<0):
        for j in range(i+1,len(arr)):
            if(arr[j]>=0):
                value=arr.pop(j)
                arr.insert(i,value)
                break
print(arr)
        
