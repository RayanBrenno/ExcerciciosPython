# Escreva um código que permita converter um número decimal em binário. Como entrada deve-se definir: o valor a ser convertido e a quantidade de bits usados para armazenar o número convertido. Se o valor binário exceder o tamanho da palavra, deverá ser emitido um erro DATA OVERFLOW. 

def decimalBinario(decimal):
    binario = ""
    
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
        
    if len(binario) >=8:
        return "O numero execedou o tamanho permitido = OVERFLOW"
    
    else:
        if len(binario) < 8:
            binario = "0" * (8 - len(binario)) + binario

        vetor = []
      
        for x in binario :
            vetor.append(x)

        return vetor
    
decimal= 15
we = decimalBinario(decimal)
print(we)