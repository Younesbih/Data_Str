# first algo is about to sort in a descending way fixing element by element
def Sorting():
    numbers = [9,4,6,7,1,5,0,3,2]
    for j in range(len(numbers)-1):
        for i in range(len(numbers)-1-j):
            if numbers[i]> numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                print(numbers)
    return numbers
result = Sorting()
print(result)