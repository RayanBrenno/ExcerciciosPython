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