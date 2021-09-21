from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo: '))
ang = radians(ang)
print("Através do ângulo {:.2f}º obtemos o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}"
      .format(ang, sin(ang), cos(ang), tan(ang)))
