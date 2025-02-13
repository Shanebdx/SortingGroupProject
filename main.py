
import random
import csv
import time as tm
import sys


# Function to find the partition position
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):

    if begin >= end:
        return
    
    pivot_idx = partition(array, begin, end)

    quick_sort_recursion(array, begin, pivot_idx-1)

    quick_sort_recursion(array, pivot_idx+1, end)
      
def quickSort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

def is_positive_int(s: str):
    """ Check if the string represents a positive integer. """
    return s.isdigit() and (len(s) == 1 or s[0] != '0')

def bubbleSort(myList): # Bubble Sort Algorithm
    """A Simple Sorting Algorithm that checks every element against the next and performs swaps, implemented from class py file given"""
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                           myList[j + 1], myList[j]
    return myList

def reverseList(myList):
    """Takes in a list Argument and retruns that list reversed"""
    return list(reversed(myList))

def generateRandomList(size = 100):
     """Generates a random list thats equally distrubeted taken from class slides"""
     m = random.sample(range(10*size), size)
     return m

def generateRandomSortedList(size = 100):
    """Generates a random list that is then sorted, uses radixSort for speed"""
    myList = generateRandomList(size)
    result = radixSort(myList)
    return result

def merge_sort(m):
    """
    Merge Sort, breaks list down recursivly into smaller and smaller subsection till each group has 2 elements. Than sorts upward.
    Takes list as argument
    """
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    """Helper Recursion function for mergeSort"""
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def countingSort(arr, exp1):
    """Helper function for Radix Sort"""
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    """A very efficent algorithm that uses digits and clever math to sort integer list"""
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    
    return arr

def bubbleSortTest(case = '2'):
    """A function responsible for testing bubble sort, takes case number for copmlexity of sort, ie worst case, avg case, best case
        Helper to main menu funciton 
    """
    #Sizes we will test and their resulting times
    testSizes = [100, 1000, 10000]
    testTimes = []

    """ 1 = best 2 = avg 3 = worst """

    #Match case number to case
    match case:
        case '1':

            #Best Case Scenairo
            #Generates a sorted List for bubble sort
            #Starts timer sorts list than stops timer
            
            #Goes through each size and sorts list
            for size in testSizes:
                data = generateRandomSortedList(size)
                start = tm.perf_counter()
                sortedList = bubbleSort(data)
                end = tm.perf_counter()

                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Best Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            #Alloows the user to input their own Ns for testing
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomSortedList(size)
                    start = tm.perf_counter()
                    sortedList = bubbleSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Best Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '2':

            #Avg Case Scenairo
            #Generates a sorted List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = bubbleSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Average Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = bubbleSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Average Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '3':

            #Worst Case Scenairo
            #Generates a reverswed sorted List causing bubble sort to make the maximum amount of comparisions
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = reverseList(generateRandomSortedList(size))
                start = tm.perf_counter()
                sortedList = bubbleSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Worst Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = reverseList(generateRandomList(size))
                    start = tm.perf_counter()
                    sortedList = bubbleSort(data)
                    end = tm.perf_counter() 
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Worst Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

def quickSortTest(case = '2'):

    #Sizes we will test and their resulting times
    testSizes = [100, 1000, 10000]
    testTimes = []
    overFlow = False

    """ 1 = best 2 = avg 3 = worst """
    match case:
        case '1':

            #Best Case Scenairo
            #Generates a random List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = quickSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Best Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = quickSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Best Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '2':

            #Avg Case Scenairo
            #Generates a random List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = quickSort(data)
                end = tm.perf_counter()

                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Average Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = quickSort(data)
                    end = tm.perf_counter()
                    
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Average Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '3':

            #Worst Case Scenairo
            #Generates a sorted List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomSortedList(size)
                start = tm.perf_counter()
                try:
                    sortedList = quickSort(data)
                except RecursionError:
                    overFlow = True
                end = tm.perf_counter()


                if(overFlow):
                    testTimes.append("INF. STACK OVERFLOW")
                    overFlow = False
                else:
                    testTimes.append(round(end-start,5))

            print("Results For Worst Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)
                    data = reverseList(generateRandomSortedList(size))

                    start = tm.perf_counter()
                    try:
                        sortedList = quickSort(data)
                    except RecursionError:
                        overFlow = True
                    end = tm.perf_counter()

                    #Same test as before! For Explantion read comments above.
                    if(overFlow):
                        testTimes.append("INF. STACK OVERFLOW")
                        overFlow = False
                    else:
                        testTimes.append(round(end-start,5))
                        print("Results For Worst Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

def mergeSortTest(case = '2'):
    #Sizes we will test and their resulting times
    testSizes = [100, 1000, 10000]
    testTimes = []

    """ 1 = best 2 = avg 3 = worst """
    match case:
        case '1':

            #Best Case Scenairo
            #Generates a random List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = merge_sort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Best Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = merge_sort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Best Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '2':

            #Avg Case Scenairo
            #Generates a sorted List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = merge_sort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Average Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = merge_sort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Average Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '3':

            #Worst Case Scenairo
            #Generates a random list, all cases are the same for merge sort!
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = reverseList(generateRandomSortedList(size))
                start = tm.perf_counter()
                sortedList = merge_sort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Worst Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = merge_sort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Worst Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

def radixSortTest(case = '2'):
    #Sizes we will test and their resulting times
    testSizes = [100, 1000, 10000]
    testTimes = []

    """ 1 = best 2 = avg 3 = worst """
    match case:
        case '1':

            #Best Case Scenairo
            #Generates a random List
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = radixSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Best Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = radixSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Best Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '2':

            #Avg Case Scenairo
            #Generates a random list
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)
                start = tm.perf_counter()
                sortedList = radixSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Average Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = radixSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Average Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

        case '3':

            #Worst Case Scenairo
            #Generates a random list, all cases are the same for radix sort
            #Starts timer sorts list than stops timer
            
            for size in testSizes:
                data = generateRandomList(size)

                start = tm.perf_counter()
                sortedList = radixSort(data)
                end = tm.perf_counter()
                #Add results to testTimes and then rounds to 5 decimals
                testTimes.append(round(end-start,5))

            print("Results For Worst Case Scenario: ")
            
            #Zip results up to then print them out nicely
            results = zip(testSizes,testTimes)

            for size, time in results:
                print(f"For N = {size}, it takes {time} Seconds.")
            
            while True:
                print("Do You Want To Use Another N? (if so enter N, to exit enter -1) ")
                userChoice = input("Enter N: ")
               

                if(is_positive_int(userChoice)):
                    #Convert the input to an int if possible
                    size = int(userChoice)
                    testSizes.append(size)

                    data = generateRandomList(size)
                    start = tm.perf_counter()
                    sortedList = radixSort(data)
                    end = tm.perf_counter()
                    #Add results to testTimes and then rounds to 5 decimals
                    testTimes.append(round(end-start,5))
                    print("Results For Worst Case Scenario: ")
            
                    #Zip results up to then print them out nicely
                    results = zip(testSizes,testTimes)

                    for size, time in results:
                        print(f"For N = {size}, it takes {time} Seconds.")
                elif(userChoice == '-1'):
                    testSizes = []
                    testTimes = []
                    return True
                else:
                    print("Invalid Response Try Again.")

def bubbleSortMenu(): 
    """A simple menu using a match (switch) statment"""
    while True:
        menuString = """
Select The Scenario For Sorting.

1. Best Case (Already Sorted)
2. Average Case (Random)
3. Worst Case (Reverse Sorted)
4. Return To Main Menu
"""
        print(menuString)
        userChoice = input("Enter your choice: ")

        match(userChoice):
            case '1':
                bubbleSortTest(userChoice)
            case '2':
                bubbleSortTest(userChoice)
            case '3':
                bubbleSortTest(userChoice)
            case '4':
                return True
        
        print("Invalid Choice Try Again.")

def quickSortMenu(): 
    """A simple menu using a match (switch) statment"""
    
    while True:
        menuString = """
Select The Scenario For Sorting.

1. Best Case (Random)
2. Average Case (Random)
3. Worst Case (Already Sorted)
4. Return To Main Menu
"""
        print(menuString)
        userChoice = input("Enter your choice: ")

        match(userChoice):
            case '1':
                quickSortTest(userChoice)
            case '2':
                quickSortTest(userChoice)
            case '3':
                quickSortTest(userChoice)
            case '4':
                return True
        
        print("Invalid Choice Try Again.")

def radixSortMenu(): 
    """A simple menu using a match (switch) statment"""
    
    while True:
        menuString = """
Select The Scenario For Sorting.

1. Best Case (Random)
2. Average Case (Random)
3. Worst Case (Random)
4. Return To Main Menu
"""
        print(menuString)
        userChoice = input("Enter your choice: ")

        match(userChoice):
            case '1':
                radixSortTest(userChoice)
            case '2':
                radixSortTest(userChoice)
            case '3':
                radixSortTest(userChoice)
            case '4':
                return True
        
        print("Invalid Choice Try Again.")

def mergeSortMenu(): 
    """A simple menu using a match (switch) statment"""

    while True:
        menuString = """
Select The Scenario For Sorting.

1. Best Case (Random)
2. Average Case (Random)
3. Worst Case (Random)
4. Return To Main Menu
"""
        print(menuString)
        userChoice = input("Enter your choice: ")

        match(userChoice):
            case '1':
                mergeSortTest(userChoice)
            case '2':
                mergeSortTest(userChoice)
            case '3':
                mergeSortTest(userChoice)
            case '4':
                return True
        
        print("Invalid Choice Try Again.")

def collectDataMenu():
    #includes overFlow flag in scope
    overFlow = False

    """A funciton to collect data about these algoirthms, outputs a csv file returns void/nothing"""
    
    #Sizes that will be tested
    sizes = []

    #Declares the timers (I dont think this is nessecary but force of habbit from C++ and Java.)
    start = tm.perf_counter()
    stop = tm.perf_counter()

    #Intiliazes the output data frame. This will be used to store all of our data, below are the labels we will be collecting.
    df = [['Sorting Algorithm', 'Case', 'Size (n)', 'Time']]


    #A simple while loop for users to input the sizes they want to test
    print("Input Data Sizes Tested (-1 to stop): ")

    while True:
        userInput = input("Insert Sizes (-1 to stop)")

        #using is positive int function for input validation.
        if(is_positive_int(userInput)):
            sizes.append(int(userInput))
            
            print("Sizes: ", sizes)

        elif(userInput == "-1"):
            break
        else:
            "Please Enter A Real Positive Integer"

    print("Input File Name: ")
    fn = input("Type File Name Here: ")
    fn = fn + ".csv"

    #Checking theres atleast one size if not, defaults to 100 elements if no sizes are provided
    if(len(sizes) == 0):
        sizes.append(100)
    


    #For Each Size
    for size in sizes:
       
        #Bubble Sort

        #Data responding to different cases below
        dataBest = generateRandomSortedList(size)
        dataAvg = generateRandomList(size)
        dataWorst = reverseList(generateRandomSortedList(size))

        #Cases that should be tested, (data, name)
        cases = [(dataBest, "Best"), (dataAvg, "Avg"), (dataWorst, "Worst")]

        for case in cases:
            start = tm.perf_counter()
            value = bubbleSort(case[0])
            stop = tm.perf_counter()
            df.append(["Bubble Sort", case[1], size, round(stop - start, 5)])

        #Quick Sort
        dataBest = generateRandomList(size)
        dataAvg = generateRandomList(size)
        dataWorst = generateRandomSortedList(size)

        #Cases that should be tested, (data, name)
        cases = [(dataBest, "Best"), (dataAvg, "Avg"), (dataWorst, "Worst")]

        for case in cases:
            start = tm.perf_counter()
            try:
                value = quickSort(case[0])
            except RecursionError:
                overFlow = True
            stop = tm.perf_counter()

            
            if(overFlow):
                timeDiff = ("INF. STACK OVERFLOW")
                
                #Resets overFlow Flag
                overFlow = False
            else:
                timeDiff = (round(stop-start,5))
            
            df.append(["Quick Sort", case[1], size, timeDiff])

        #Merge Sort
        dataBest = generateRandomList(size)
        dataAvg = generateRandomList(size)
        dataWorst = generateRandomList(size)

        #Cases that should be tested, (data, name)
        cases = [(dataBest, "Best"), (dataAvg, "Avg"), (dataWorst, "Worst")]

        for case in cases:
            start = tm.perf_counter()
            value = merge_sort(case[0])
            stop = tm.perf_counter()
            df.append(["Merge Sort", case[1], size, round(stop - start, 5)])  

        #Radix Sort
        dataBest = generateRandomList(size)
        dataAvg = generateRandomList(size)
        dataWorst = generateRandomList(size)

        #Cases that should be tested, (data, name)
        cases = [(dataBest, "Best"), (dataAvg, "Avg"), (dataWorst, "Worst")]

        for case in cases:
            start = tm.perf_counter()
            value = radixSort(case[0])
            stop = tm.perf_counter()
            df.append(["Radix Sort", case[1], size, round(stop - start, 5)])     

        
    #Store Data to CSV
    # Open the file in write mode
    with open(fn, mode='w', newline='') as file:
        # Create a csv.writer object
        writer = csv.writer(file)
        # Write data to the CSV file
        #CSV File Can be exported to google sheets or excel to make data graphs
        writer.writerows(df)

if __name__ == "__main__":

    while True:
        menuString ="""

Welcome to S25 Sorting Group Project
(Tyler Kelly, Zeke Fletcher, and Graeme LastName)
Select the Alogrithm you want to test.

1. Bubble Sort
2. Quick Sort
3. Merge Sort
4. Radix Sort
5. Collect Data
6. Quit
"""
        print(menuString)
        
        userChoice = input("Please Enter A Choice: ")

        match userChoice:
            case '1':
                bubbleSortMenu()
                continue
            case '2':
                quickSortMenu()
                continue
            case '3':
                mergeSortMenu()
                continue
            case '4':
                radixSortMenu()
                continue
            case '5':
                collectDataMenu()
                continue
            case '6':
                exit()
            case '7':
                break
        
        print("Invalid Choice Try Again")
    

