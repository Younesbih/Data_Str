#this algo is about to search in a linear way using the target
def linear_search(num,target):
    target_found = False
    for i in range(len(num)):
        if num[i] == target:
            print(f"target found at index: {i}")
            break
    if not target_found:
        print(f"this element is not found")
tar = int(input("enter the elemenet your searching for it must to be an integer: "))
numbers = [9,4,6,7,1,5,0,3,2]
linear_search(numbers,tar)
