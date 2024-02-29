def poimpoim(): 
    hexDec={
        #Hexadecimal para decimal
        "A" : "10",
        "B" : "11",
        "C" : "12",
        "D" : "13",
        "E" : "14",
        "F" : "15",
    }
    
    hexBin={
        #Hexadecimal para Binario
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111"
    }

    binHex={
        #Binario para Hexadecimal
        "0000" : "0",
        "0001" : "1",
        "0010" : "2",
        "0011" : "3",
        "0100" : "4",
        "0101" : "5",
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "10",
        "1011" : "11",
        "1100" : "12",
        "1101" : "13",
        "1110" : "14",
        "1111" : "15"
    }

    binOct={
        #Binario para Octal
        "000" : "0",
        "001" : "1",
        "010" : "2",
        "011" : "3",
        "100" : "4",
        "101" : "5",
        "110" : "6",
        "111" : "7"
    }

    octBin={
        #Octal para Binario
        "0" : "000",
        "1" : "001",
        "2" : "010",
        "3" : "011",
        "4" : "100",
        "5" : "101",
        "6" : "110",
        "7" : "111"
    }

    decHex={
        #Numeros do Decimal trocando para as letras do Hexa 
        10 : "A",
        11 : "B",
        12 : "C",
        13 : "D",
        14 : "E",
        15 : "F",
    }

    def decimalBinario(decimal):

        binario = ""
        
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal = decimal // 2

        return binario

    def decimalOctal(decimal):
        octal = ""
        while decimal > 0:
            resto = decimal % 8
            octal = str(resto) + octal
            decimal = decimal // 8

        return octal

    def decimalHexadecimal(decimal,decHex):
        hexadecimal = ""
        while decimal > 0:
            resto = decimal % 16
            if 10 <= resto <=15:
                resto = decHex[resto]
            hexadecimal = str(resto) + hexadecimal
            decimal = decimal // 16

        return hexadecimal

    def binarioOctal(binario,binOct):
        octal=""
        n=0
        if len(binario)%3 == 1: binario= "00"+binario
        elif len(binario)%3 == 2: binario= "0"+binario

        while n< len(binario):
            temp = binario[n:n+3]
            octal += binOct[temp]
            n+=3
        return octal

    def binarioHexadecimal(binario,binHex,decHex):
        hexa=""
        n=0
        if len(binario)%4 == 1: binario= "000"+binario
        elif len(binario)%4 == 2: binario= "00"+binario
        elif len(binario)%4 == 3: binario= "0"+binario

        while n< len(binario):
            temp = binario[n:n+4]
            temp = binHex[temp]

            if 10 <= int(temp) <=15:
                temp = int(temp)
                temp = decHex[temp]
                hexa += temp 

            else: hexa += temp

            n+=4
        return hexa

    def octalBinario(octBin,octal):
        binario=""

        for temp in octal:
            binario += octBin[temp]
        
        binario = binario.lstrip('0')

        return binario

    def hexadecimalBinario(hexBin,hexadecimal):
        binario=""

        for temp in hexadecimal:
            binario += hexBin[temp]

        binario = binario.lstrip('0')

        return binario

    def hexadecimalOctal(hexadecimal):

        binario=hexadecimalBinario(hexBin,hexadecimal)
        octal=binarioOctal(binario,binOct)

        return octal

    def octalHexadecimal(octal):

        binario=octalBinario(octBin,octal)
        hexadecimal=binarioHexadecimal(binario,binHex,decHex)

        return hexadecimal

    def binarioDecimal(binario):
        soma = 0
        expoente = len(binario)-1

        for n in binario:
            soma += int(n) * (2 ** expoente)
            expoente -=1   

        return soma
    
    def octalDecimal(octal):
        soma = 0
        expoente = len(octal)-1

        for n in octal:
            soma += int(n) * (8 ** expoente)
            expoente -=1   

        return soma

    def hexadecimalDecimal(hexadecimal,hexDec):
        soma = 0
        expoente = len(hexadecimal)-1

        for n in hexadecimal:
            
            if n in hexDec:
                n = hexDec[n]   

            soma += int(n) * (16 ** expoente)
            expoente -=1   

        return soma

    def testing1():
      
        def askForType():
            while True:
                type = input("What type of number will you enter? \n"
                        "1-Decimal\n"
                        "2-Binario\n"
                        "3-Octal\n"
                        "4-Hexadecimal\n"
                        "") 
                if type.isdigit() and 1<=int(type)<=4: break
                else: print("\n""Please enter a valid number") 
            return type
        
        type = askForType() 
        
        def askForNumber(type):
            
            if type == "1":
                while True:
                    number = input("Put the Number: ")         
                    if number.isdigit(): break
                    else: print("\n""Please enter a valid number")
                    
            elif type == "2":
                while True:
                    number = input("Put the Number: ")         
                    if number.isdigit(): 
                        if all('0' <= n <= '1' for n in number): break
                        else: print("\n""Please enter a valid number")
                    else: print("\n""Please enter a valid number")
                    
            elif type == "3":
                while True:
                    number = input("Put the Number: ")         
                    if number.isdigit(): 
                        if all('0' <= n <= '7' for n in number): break
                        else: print("\n""Please enter a valid number")
                    else: print("\n""Please enter a valid number")
                    
            else:
                while True:
                    number = input("Put the Number: ") 
                    number = number.upper()
                    def right(number):
                        contains_number = any(char.isdigit() for char in number)
                        contains_af = all(char.lower() in 'abcdef' for char in number if char.isalpha())
                        return contains_number and contains_af
                    
                    if right(number)==True:break     
                    else: print("\n""Please enter a valid number")
            
            return number
        
        number = askForNumber(type)
        action = ""
        
        while action != "4":
            
            if type == "1":
                number = int(number)
                while True:
                    action = input("\n""What action do you want to perform with the number?\n"
                                    "1-Transform it into Binary\n"
                                    "2-Transform it into Octal\n"
                                    "3-Transform it into Hexadecimal\n"
                                    "4-Leave\n"
                                    "")         
                    if action.isdigit() and 1<=int(action)<=4: break
                    else: print("\n""Please enter a valid number")

                if action == "1": print(f"The number digited in Binary is {decimalBinario(number)}")
                elif action == "2": print(f"The number digited in Octal is {decimalOctal(number)}")
                elif action == "3": print(f"The number digited in Hexadecimal is {decimalHexadecimal(number,decHex)}")
    
            elif type == "2":
                while True:
                    action = input("\n""What action do you want to perform with the number?\n"
                                "1-Transform em Decimal\n"
                                "2-Transform it into Octal\n"
                                "3-Transform it into Hexadecimal\n"
                                "4-Leave\n"
                                "")         
                    if action.isdigit() and 1<=int(action)<=4: break
                    else: print("\n""Please enter a valid number")
                    
                if action == "1": print(f"The number digited in Decimal is {binarioDecimal(number)}")
                elif action == "2": print(f"The number digited in Octal is {binarioOctal(number,binOct)}")
                elif action == "3": print(f"The number digited in Hexadecimal is {binarioHexadecimal(number,binHex,decHex)}")
                
            elif type == "3":
                while True:
                    action = input("\n""What action do you want to perform with the number?\n"
                                "1-Transform it into Decimal\n"
                                "2-Transform it into Binary\n"
                                "3-Transform it into Hexadecimal\n"
                                "4-Leave\n"
                                "")         
                    if action.isdigit() and 1<=int(action)<=4: break
                    else: print("\n""Please enter a valid number")
                    
                if action == "1": print(f"The number digited in Decimal is {octalDecimal(number)}")
                elif action == "2": print(f"The number digited in Binary is {octalBinario(octBin, number)}")
                elif action == "3": print(f"The number digited in Hexadecimal is {octalHexadecimal(number)}")
                
            else:
                while True:
                    action = input("\n""What action do you want to perform with the number?\n"
                                "1-Transforma-lo em Decimal\n"
                                "2-Transform it into Binary\n"
                                "3-Transform it into Octal\n"
                                "4-Leave\n"
                                "")         
                    if action.isdigit() and 1<=int(action)<=4: break
                    else: print("\n""Please enter a valid number")
                    
                if action == "1": print(f"The number digited in Decimal is {hexadecimalDecimal(number,hexDec)}")
                elif action == "2": print(f"The number digited in Binary is {hexadecimalBinario(hexBin,number)}")
                elif action == "3": print(f"The number digited in Hexadecimal is {hexadecimalOctal(number)}")
                         
            if action == "4":
                print("Exiting the program...")
                break
            
            temp = type            
            type = input("\n""Do you want change the number?\n"
                         "Y/N\n"
                         "")
            if type.upper()=="Y":
                type = askForType()
                number = askForNumber(type)
            else: type = temp 
    
    def testing2():
        while True:
            number = input("Digite o número (decimal) que deseja fazer as conversões: ") 
            if number.isdigit(): break
            else: print("Por favor, digite um número válido.")

        decimal = int(number)
        binario = decimalBinario(decimal)
        octal = decimalOctal(decimal)
        hexadecimal = decimalHexadecimal(decimal,decHex)
        print("------------------------------------------------------------------")
        print("Binarios")
        print(f"Decimal para Binário:     {binario}")
        print(f"Octal para Binario:       {octalBinario(octBin, octal)}")
        print(f"Hexadecimal para Binario: {hexadecimalBinario(hexBin,hexadecimal)}")
        print("------------------------------------------------------------------")
        print("Octais")
        print(f"Decimal para Octal:     {octal}")
        print(f"Binario para Octal:     {binarioOctal(binario,binOct)}")
        print(f"Hexadecimal para Octal: {hexadecimalOctal(hexadecimal)}")
        print("------------------------------------------------------------------")
        print("Hexadecimais")
        print(f"Decimal para Hexadecimal: {hexadecimal}")
        print(f"Binario para Hexadecimal: {binarioHexadecimal(binario,binHex,decHex)}")
        print(f"Octal para Hexadecimal:   {octalHexadecimal(octal)}")
        print("------------------------------------------------------------------")
        print("Decimais:")
        print(f"Binario para Decimal:     {binarioDecimal(binario)}")
        print(f"Octal para Decimal:       {octalDecimal(octal)}")
        print(f"Hexadecimal para Decimal: {hexadecimalDecimal(hexadecimal,hexDec)}")
        print("------------------------------------------------------------------")
        print("Abraço Gomide S2")
        
    testing1()
    testing2()
    
poimpoim()