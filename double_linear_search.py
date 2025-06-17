#this algo is about to search in a linear way "that's mean you that you search from both sides from the start and from the end of the list"
def search_in_list(list,target):
    for i in range(len(list)//2):
        opposite = len(list)-1-i
        if list[i] == target:
            return i
        elif list[opposite] == target:
            return opposite
    return -1
lst = [9,4,6,7,1,5,0,3,2]
trg = int(input("enter the enter the elemenet your searching for it must to be an integer: "))
result = search_in_list(lst,trg)
print(result)