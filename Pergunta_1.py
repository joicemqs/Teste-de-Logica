def umNaFrente(arr):
    print(arr) #mostra array inicial
    print("------------------------------------------------")
    n = len(arr)
    for i in range(1,n): #Percorre o array a partir do segundo número
        aux = arr[i]  #atribui a variavl auxiliar como o valor atual da posição i
        j = i-1 # define j como o valor anterior da posição i
        while j >= 0 and aux == 1: # executa enquanto o valor de posição j >= 0 e o valor atual é 1
            arr[j+1] = arr[j] #coloca na posição atual o valor da posição anterior
            j -= 1 #diminui j, ou seja vai uma posição para traz / para o loop quando j = -1
        arr[j+1] = aux  #coloca na posição 0 (j + 1 = 0) o número atual da repetição i
        print(arr)#mostra o array etapa por etapa


array = [2,1,5,2,5,2,1,1,1,7,9,13,127,21]
umNaFrente(array)
print("------------------------------------------------")
print(array)
