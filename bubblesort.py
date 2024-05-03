def bubblesort(isArray):
    n = len(isArray)

    for i in range(n):
        for j in range(n-1):
            if isArray[j] > isArray[j+1]:
                isArray[j], isArray[j+1] = isArray[j+1], isArray[j]
        
    



angka = [10, 9, 2, 5, 6]
print(angka)
bubblesort(angka)
print(angka)

buah = ['banana', 'apple', 'purple']
print(buah)
bubblesort(buah)
print(buah)