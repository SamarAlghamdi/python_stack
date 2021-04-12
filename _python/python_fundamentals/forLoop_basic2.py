# Given a list, write a function that changes all positive numbers in the list to "big"
def biggie_size(arr):
    newArr=[]
    for x in range(len(arr)):
        if arr[x]>0:
            newArr.append("big")
        else:
            newArr.append(arr[x])
    return newArr
# print(biggie_size([-1, 3, 5, -5]) )

# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(arr):
    count=0
    for x in range(len(arr)):
        if arr[x]>0:
            count+=1
    arr[-1]=count
    return arr
# print(count_positives([-1,1,1,1]))

# Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(arr):
    sum=0
    for x in range(len(arr)):
        sum+=arr[x]
    return sum

# Create a function that takes a list and returns the average of all the values
def average(arr):
    sum=0
    for x in range(len(arr)):
        sum+=arr[x]
    return sum/len(arr)
# print(average([1,2,3,4]))

# Create a function that takes a list and returns the length of the list.
def length(arr):
    return len(arr)

# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(arr):
    if len(arr)>0:
        min=arr[0]
        for x in range(len(arr)):
            if arr[x]<min:
                min=arr[x]
        return min
    else:
        return False

# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(arr):
    if len(arr)>0:
        max=arr[0]
        for x in range(len(arr)):
            if arr[x]>max:
                max=arr[x]
        return max
    else:
        return False

# Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(arr):
    sum=0
    avg=0
    if len(arr)>0:
        min= arr[0]
        max=arr[0]
        for x in range(len(arr)):
            sum+=arr[x]
            if arr[x]>max:
                max=arr[x]
            elif arr[x]<min:
                min=arr[x]
        avg =sum/len(arr)
        return {'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': len(arr) }
    else:
        return False
# print(ultimate_analysis([37,2,1,-9]))

# Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
def reverse_list(arr):
    arr.reverse()
    return arr
print(reverse_list([37,2,1,-9]))
