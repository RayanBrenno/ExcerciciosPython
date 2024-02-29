alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

frase=input("Digite a frase que desejar \n"
            "")

fraseFinal=""
    
for x in frase:
    if x == " ":
        fraseFinal += "   "
        
    elif x.upper() in alfabeto:
        fraseFinal += str(alfabeto.index(x.upper())+1) + " "
    
    else:
        print("Nao foi possivel realizar a troca para numero, caractere nao encontrado")
        fraseFinal=""
        break

print(fraseFinal)