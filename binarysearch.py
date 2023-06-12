import os
os.system('cls')

def search(arr,x):
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (high + low)//2
        if (arr[mid]< x):
            low = mid + 1
        elif (arr[mid]> x):
            high = mid -1
        else:
            return mid
    return -1

def recsearch(arr,low,high,x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recsearch(arr,low,high-1,x)
        else:
            return recsearch(arr,mid+1,high,x)
    else:
        return-1
    
arr = [10,11,12,13,14,15,16,17,18]
x = int(input("Masukan Nilai :"))
if(search(arr,x) ):
    print("Index ke- ",(search(arr,x)))
else:
    print("Index tidak ditemukan")
    

print(recsearch(arr,0,len(arr)-1,x))