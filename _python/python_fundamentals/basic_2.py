# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    newList = []
    for x in range(num,-1,-1):
        newList.append(x)
    return newList
# print(countdown(5))

# Create a function that will receive a list with two numbers. Print the first value and return the second.
def printAndReturn(myList):
    print(myList[0])
    return myList[1]
# print(printAndReturn([1,2]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(myList):
    return myList[0]+ myList[-1]
# print(firstPlusLength([1,2,3,4,5]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def firstPlusLength(myList):
    newList=[]
    if len(myList)<=2:
        return False
    else
        for x in range(2,len(myList)):
            if(myList[x]>myList[1]):
                newList.append(myList[x])
        return newList

# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def thisLengthThatValu(size,val):
    myList=[]
    for x in range(size+1):
        myList.append(val)
    return myList

