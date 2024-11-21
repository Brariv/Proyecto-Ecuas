from LocalizacionTemps import *
from CpuTemps import *
from StressTest import *

def main():
    temperatura = obtener_temperatura_ciudad_guatemala()
    if temperatura is not None:
        print(f'La temperatura en Guatemala es {temperatura}°C')
    else:
        print(f'No se pudo obtener la temperatura para Guatemala')
    cpu_temps = obtener_temperatura_cpu()
    print(f'Las temperaturas de la CPU antes del stress test son: {cpu_temps}')
    

def after():
    cpu_temps = obtener_temperatura_cpu()
    print(f'Las temperaturas de la CPU despues del test son: {cpu_temps}')


if __name__ == '__main__':
    main()
    stress(2)
    after()