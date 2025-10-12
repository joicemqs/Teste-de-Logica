array = [9,2,3,1,4]

def completaIntervalo(arr):
    maior = max(arr) # recebe o maior valor dentro do array
    for i in range(maior): # laço de repetição de 0 até o maior número
        if i in arr: # confere se o número já esxiste na array
            continue #continua para a próxima repetiçao do for
        else:
            array.append(i) # adiciona número faltante
        print(array)
    n = len(arr)
    for i in range(1,n): 
        aux = arr[i]  
        j = i-1 
        while j >= 0 and aux < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1 
        arr[j+1] = aux
    print("-------------------------------")    
    print(arr)
     

completaIntervalo(array)
