def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            print(i)

missing_number([1,2,3,4],6)

