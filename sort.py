n = [[0,0]*12]
#ghjkl
def SortInsert(sorting_list, start = 1):
    for i in range(start,len(sorting_list)):
        for j in range(i,0,-1):
            n[0][0] += 1
            if sorting_list[j] < sorting_list[j-1]:
                n[0][1] +=1
                sorting_list[j], sorting_list[j-1] = sorting_list[j-1], sorting_list[j]
            else:
                break

def SortShell(sorting_list):
    step = len(sorting_list) // 2
    while step > 0:
        for i in range(0,step):
            for j in range(i+step,len(sorting_list),step):
                for k in range(j,0,-step):
                    if sorting_list[j] < sorting_list[j-step]:
                        sorting_list[j], sorting_list[j-step] = sorting_list[j-step], sorting_list[j]
                    else:
                        break
        step //= 2  
    SortInsert(li)     

def SortMerge(sorting_list):
    if len(sorting_list) > 1:
        n = len(sorting_list) // 2
        leftPart = sorting_list[:n]
        rightPart = sorting_list[n:]
        SortMerge(leftPart)
        SortMerge(rightPart)
        i = j = k = 0
        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                sorting_list[k] = leftPart[i]
                i+=1
            else:
                sorting_list[k] = rightPart[j]
                j+=1
            k+=1
        while i < len(leftPart):
            sorting_list[k] = leftPart[i]
            i+=1
            k+=1
        while j < len(rightPart):
            sorting_list[k] = rightPart[j]
            j+=1
            k+=1

def SortQuick(sorting_list, leftInd=0, rightInd=0):
    if rightInd == 0:
        rightInd = len(sorting_list)-1
    i = leftInd
    j = rightInd
    pivot = sorting_list[leftInd + (rightInd - leftInd) // 2]
    while i <= j:
        while sorting_list[i] < pivot:
            i+=1
        while sorting_list[j] > pivot:
            j-=1
        if i <= j:
            sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
            i+=1
            j-=1
    if leftInd < j:
        SortQuick(sorting_list, leftInd, j)
    tInd:if i < righ
        SortQuick(sorting_list, i, rightInd)

a = [2,6,-5,2,9,0,-4]
SortQuick(a)
print(a)

def LinearSearch(_list, key):
    for i in range(len(_list)):
        if _list[i] == key:
            return i
    return -1

li = [3,2,5,1,4]
SortInsert(li)

start = len(li)
li.append(0)
li.append(-1)
print(li)
SortInsert(li, start)
print(li)

li = [5,4,3,2,1]
SortShell(li)
print(li)

li = [3,2,5,1,4,6,-1,0]
SortMerge(li)
print(li)


