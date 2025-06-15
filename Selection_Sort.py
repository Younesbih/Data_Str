# this algo is about to sort in a ascending way selecting first element and searching for the smallest element
def Sorting(numbers):
    for j in range(len(numbers)):
        min_index = j
        for i in range(j+1,len(numbers)):
            if numbers[i] < numbers[min_index]:
                min_index = i
        numbers[j],numbers[min_index] = numbers[min_index],numbers[j]
        print(numbers)
    return numbers
result = Sorting([9,4,6,7,1,5,0,3,2])
print(f"The sorted list is: {result}")