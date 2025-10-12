array = [1,15,2,7,2,5,7,1,4]

def existeSoma (x,arr):
    n = len(arr)
    for i in range (n):
        y = x - arr[i]
        print(y)
        for j in range (n):
            if arr[j] == y:
                return True
    return False

print(existeSoma(10, array))