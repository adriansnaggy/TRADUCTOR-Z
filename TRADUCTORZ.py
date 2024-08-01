dictmemes = {
            "LOL" : "una respuesta a algo gracioso",
            "CRINGE" : "algo raro o embarazoso",
            "ROFL" : "una respuesta a una broma", 
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"
            "WOW" : "es una expresion de sorpresa"
            "XD" : "respuesta a algo chistoso"
            }

print("hola, este es un programa en el que puedes preguntar cual es una expresion actual que no entiendas")

    
for i in range(5):
    nomb = input("escribe una palabra en mayusculas para poder traducirla: ")
    if nomb in dictmemes:
        print("significa: ", dictmemes[nomb])
    else:
        print("disculpe todavia no tenemos esa palabra, consulte de nuevo en nuevas actualaizaciones :)")
        
        
        
        
        
        
