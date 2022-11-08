

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100] # 0 - 8
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"] # 0 - 6
unsorted = [30, 20, 70, 40, 50, 100, 90] # 0 - 6
print("-----------------------------")


def binery(arr, item):
    low = 0
    hi = len(arr) - 1
    ## looooop
    
    while low <= hi:
        miInd = (low + hi) // 2
        if arr[miInd] == item:
            return item, miInd
        elif item > arr[miInd]:
            low = miInd + 1
        else:
            hi = miInd - 1
            
    return -1







print(binery(nums, 100))     ## (100, 8)
print(binery(nums, 75))
print(binery(words, "fish")) ## ('fish', 5)
print(binery(words, "at")) ## ('at', 0)
print(binery(unsorted, 70))