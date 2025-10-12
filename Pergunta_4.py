array = [9,2,3,1,4]

def completaIntervalo(arr):
    maior = max(arr)
    n = len(arr)
    for i in range(maior):
        if i in arr:
            continue
        else:
            array.append(i)
    print(array)
    

completaIntervalo(array)