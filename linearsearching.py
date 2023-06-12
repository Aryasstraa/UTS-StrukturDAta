import os
os.system('cls')

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] ==x:
            return i        
    return -1

def recsearch(arr,x,cur_idx):
    if cur_idx > len(arr)-1:
        return -1
    if arr[cur_idx] ==x:
        return cur_idx
    return recsearch(arr,x,cur_idx+1)



arr = [45,18,17,95,100,40,21,45]
x = 100
print(recsearch(arr,x,0))
# print("index ke-",search(arr,x))
# print("Urutan ke-",(search(arr,x)+1))
# hasil = search(arr,x)
# print(arr[hasil])