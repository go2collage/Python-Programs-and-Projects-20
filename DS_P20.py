# Python Program / Project

def bucketsort(arr):
    bucket = []
    maxe = max(arr)
    size = maxe/len(arr)

    # Create empty bucket
    for i in range(len(arr)):
        bucket.append([])

    # Insert elements into their respective 
    for i in range(len(arr)):
        j = int (arr[i]/size)
        if j!= len(arr):
            bucket[j].append(arr[i])
        else:
            bucket[len(arr)-1].append(arr[i])

    # Sort the elements of each bucket
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    
    # Get sorted elements
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    
    return arr

# Driver Code

num = int(input("Enter how many students in 12 class:"))
arr = []

i = 0
for i in range(num):
    item = float(input("Enter percentage marks: "))
    arr.append(item)

print("Before sorting percentage list: ")
print(arr)

bucketsort(arr)
print("After sorting using Bucket Sort list is: ")
print(arr)

print("Top five percentage marks: ")
for i in range(len(arr)-1, 1, -1):
    print(arr[i])
