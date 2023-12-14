temperatura = float(input("Quanto está a temperatura lá fora? "))

if not (temperatura >= 0 and temperatura <= 30):
    print("Temperatura não ta muito boa hoje")
    print("Fique em casa!")
elif not (temperatura < 0 or temperatura > 30):
    print("A temperatura esta boa hoje!")
    print("Aproveite o dia!")
