nome= input ("Nome do paciente:")
peso= float (input("Peso do paciente em quilogramas:"))
altura= float (input("Altura do paciente em metros:"))

imc= peso/('altura*altura')
print ('Seu IMC equivale a:',imc) 

# > maior                                                        
# < menor
 
 if imc <18.5:
   print (f'O paciente (nome) esta abaixo do peso', imc)

elif imc >=18 and peso <=34.  
