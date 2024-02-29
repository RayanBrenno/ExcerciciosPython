def soma(binario1, binario2):

    binario1 = binario1[::-1]
    binario2 = binario2[::-1]
    resultado = ""
    c = 0
    
    for a, b in zip(binario1, binario2):
        sum = int(a) ^ int(b) ^ c
        c = int(a) and int(b) or ((int(a) ^ int(b)) and c)
        resultado = str(sum) + resultado

    if c == 1:
        print("OBS: Ocorreu um Overflow na soma")

    return resultado

def complementoUm(binario):
    
    if len(binario) < 8:
        binario = "0" * (8 - len(binario)) + binario
             
    binComp1=""
    for n in binario:
        if n=="0":
            binComp1 = binComp1+"1"
        else: binComp1 = binComp1+"0"
    
    if len(binComp1) >8:
        return "O numero execedou o tamanho permitido = OVERFLOW"

    return binComp1

def complementoDois(binario):
    
    binComp1 = complementoUm(binario)
    binSoma="00000001"
    binComp2=soma(binComp1,binSoma)

    vetor = []

    for x in binComp2 :
        vetor.append(x)

    if binComp2[0] != binComp1[0]: return "O numero execedou o tamanho permitido = OVERFLOW"
    else: return vetor
    
binario = "110"
hu = complementoDois(binario)
print(hu)