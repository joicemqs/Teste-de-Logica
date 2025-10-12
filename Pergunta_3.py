array = [1,15,2,7,2,5,7,1,4]

def existeSoma (x,arr):
    n = len(arr)
    for i in range (n): # percorre array 
        y = x - arr[i] # resgistra a diferença entre o numero digitado e o número da array
        for j in range (n): # percorre a array para buscar a diferença
            if j == i: # evita que a array compare um número com ele mesmo 
                continue
            elif arr[j] == y: # se a diferença for encontrada na array retorna true
                return True
    return False # retorna false se a diferença entre x e qualquer valor da diferença não for encontrada

print("----------------------------------------------------")
x = int (input("Digite a soma que deseja encontrar no array: "))
if existeSoma(x,array):
    print("\nA soma existe no array!")
else:
    print("\nA soma não existe no array!")
print("----------------------------------------------------")