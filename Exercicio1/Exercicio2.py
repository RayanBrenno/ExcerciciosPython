def complementoUm(binario):
    
    if len(binario) < 8:
        binario = "0" * (8 - len(binario)) + binario
             
    binComp=""
    for n in binario:
        if n=="0":
            binComp = binComp+"1"
        else: binComp = binComp+"0"
    
    if len(binComp) >8:
        return "O numero execedou o tamanho permitido = OVERFLOW"
    
    vetor = []

    for x in binComp :
        vetor.append(x)

    return vetor

binario = "110"
we2 = complementoUm(binario)
print(we2)