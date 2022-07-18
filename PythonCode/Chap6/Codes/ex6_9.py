arr = [('banana', 2), ('apple', 5), ('carrot', 3)]


def setting(data):
    return data[1] # data의 두번째 원소를 리턴.


res = sorted(arr, key=setting)
print(res)

arr.sort(key=setting)
print(arr)
