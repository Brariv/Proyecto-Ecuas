import math

def ley_de_enfriamiento_de_newton(T, T_a, k, t):
    return T_a + (T - T_a) * math.exp(-k * t)

#def ley_de_enfriamiento_de_newton(T_o, T_a, k, T_f):
#    return -math.log((T_f - T_a) / (T_o - T_a)) / k

def constante_k(T_o, T_f, T_a, t):
    return -math.log((T_f - T_a) / (T_o - T_a)) / t

print(constante_k(82, 70, 28, 5))

print(ley_de_enfriamiento_de_newton(82, 28, 0.050262885656181214, 45))

