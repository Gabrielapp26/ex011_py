#Desafio 10 
#Escreva um programa que converta uma temperatura digitada em graus Celsius em graus Fahrenheit
c = float(input("Digite uma temperatura: "))
f = c * 1.8 + 32
print("{} C é {} F".format(c, f))