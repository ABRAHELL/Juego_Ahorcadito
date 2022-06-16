

palabra = input("Ingrese palabra:  ")
largoPalabra = len(palabra)

letrasIngresadas = []
letrasAcertadas = 0

while letrasAcertadas < largoPalabra:
    letraIngresada = input("Ingrese letra:  ")
    
    
    if letraIngresada in letrasIngresadas:
        print("Esa ya está, intenta con otra:  ")
        letraIngresada = input("Ingrese otra letra:  ")
        
    letrasIngresadas.append(letraIngresada)
    
    if letraIngresada in palabra:
        letrasAcertadas += 1
        
print("Letras mencionadas: ", letrasIngresadas)
print("Felicidades!! lo lograste")


        
    