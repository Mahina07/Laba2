def func():
    list_all = list(map(int, input().split()))
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(list_all)):
        if list_all[i] % 2 == 0:
            list1.append(list_all[i])
        if list_all[i] % 3 == 0:
            list2.append(list_all[i])
        if list_all[i] % 5 == 0:
            list3.append(list_all[i])
    return list1, list2, list3
print(func())

