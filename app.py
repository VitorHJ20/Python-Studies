githcelsius = 0.0
kelvin = 0.0
farehn= 0.0
unidmed = ""
print ("\033c", end="")

while celsius == 0.0 :
    celsius = input ("Digite a temperatura em celsius:")
    try:
        celsius = float(Celsius)
    except:
        print ("temperatura deve ser informada corretamente")
        celsius = 0.0


while unidmed == "":
    unidmed = input ("Digite k para Kelvin ou f para Farenheit")
    if unidmed !="k" and unidmed != "f":
        print ('Outra unidade de medida deve ser informada corretamente')
        unidmed = ""
        
if unidmed == "k":
            kelvin = celsius + 273
            print ("temperatura em celsius=",celsius)
            print ("temperatura em kelvin=", kelvin)
elif unidmed == "k":
    farehn =((celsius * 9) / 5 + 32)
    print ("Temperatura em celsius =", celsius)
    print ("temperatura em farenheit", farenh) 
else:
    print ("Unidade de medida invalida ")
    
 