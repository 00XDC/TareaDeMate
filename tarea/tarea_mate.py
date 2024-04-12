import math
def distancia_puntos(lado1, lado2):
    return math.sqrt((lado2[0] - lado1[0])*2 + (lado2[1] - lado1[1])*2)

def tipo_triangulo(lado1, lado2, lado3):
    lados = sorted([distancia_puntos(lado1, lado2), distancia_puntos(lado2, lado3), distancia_puntos(lado3, lado1)])
    a, b, c = lados
    
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or b == c or c == a:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    return tipo, sum(lados)

def area_triangulo(lado1, lado2, lado3):
    a = distancia_puntos(lado1, lado2)
    b = distancia_puntos(lado2, lado3)
    c = distancia_puntos(lado3, lado1)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def angulos_triangulo(lado1, lado2, lado3):
    a = distancia_puntos(lado1, lado2)
    b = distancia_puntos(lado2, lado3)
    c = distancia_puntos(lado3, lado1)
    A = math.acos((b*2 + c2 - a*2) / (2 * b * c))
    B = math.acos((c*2 + a2 - b*2) / (2 * c * a))
    C = math.acos((a*2 + b2 - c*2) / (2 * a * b))
    return math.degrees(A), math.degrees(B), math.degrees(C)

def main():
    vertices = []
    for i in range(3):
        x = float(input(f"Ingrese la coordenada x del vértice {i+1}: "))
        y = float(input(f"Ingrese la coordenada y del vértice {i+1}: "))
        vertices.append((x, y))
    
    tipo, perimetro = tipo_triangulo(*vertices)
    area = area_triangulo(*vertices)
    angulos = angulos_triangulo(*vertices)
    
    print(f"El triángulo es {tipo}")
    print(f"Su perímetro es {perimetro}")
    print(f"Su área es {area}")
    print(f"Los ángulos son: A={angulos[0]}, B={angulos[1]}, C={angulos[2]}")

if __name__ == "_main_":
    main()