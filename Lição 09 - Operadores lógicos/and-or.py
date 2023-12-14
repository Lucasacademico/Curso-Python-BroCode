# Operadores lógicos (and, or, not) = São usados para verificar se duas ou mais condicionais são verdadeiras/falsas.

temperatura = float(input("Quanto está a temperatura lá fora? "))

if temperatura >= 0 and temperatura <= 30:
    print("A temperatura esta boa hoje!")
    print("Aproveite o dia!")
elif temperatura < 0 or temperatura > 30:
    print("Temperatura não ta muito boa hoje")
    print("Fique em casa!")