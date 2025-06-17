#this algo is about to search in a linear way using the target
def linear_search(num,target):
    target_found = False
    for i in range(len(num)):
        if num[i] == target:
            print(f"target found at index: {i}")
            target_found = True
            break
    if target_found == False:
        print(f"this element is not found")
tar = int(input("enter the elemenet your searching for it must to be an integer: "))
numbers = [9,4,6,7,1,5,0,3,2]
result = linear_search(numbers,tar)

def search_in_list(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
lst = [9,4,6,7,1,5,0,3,2]
trg = int(input("enter the enter the elemenet your searching for it must to be an integer: "))
result = search_in_list(lst,trg)
print(result)