from LocalizacionTemps import *
from CpuTemps import *
from StressTest import *
from LeyDeEnfriamientoNewton import *
import time
import pandas as pd
import matplotlib.pyplot as plt

def main():
    temperatura = round(obtener_temperatura_ciudad_guatemala(), 2)
    if temperatura is not None:
        print(f'La temperatura en Guatemala es: {temperatura}°C')
    else:
        print(f'No se pudo obtener la temperatura para Guatemala')
    cpu_temps = round(obtener_temperatura_cpu(), 2)
    print(f'Las temperaturas de la CPU antes del stress test son: {cpu_temps}°C')
    

def after():
    Times = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    Total_cpu_temps = []
    Newton_cpu_temps = []
    Temperatura_Ambiente = round(obtener_temperatura_ciudad_guatemala(), 2)
    cpu_temps = round(obtener_temperatura_cpu(), 2)
    print(f'Las temperaturas de la CPU despues del test son: {cpu_temps}°C')
    for i in range(11):
        cpu_temps = round(obtener_temperatura_cpu(), 2)
        Total_cpu_temps.append(cpu_temps)
        time.sleep(30)
        print(f'Obteniendo temperaturas... {i+1}/11')
    k = constante_k(Total_cpu_temps[0], Total_cpu_temps[10], Temperatura_Ambiente, 5)
    for i in range(11):
        Newton_temps = round(ley_de_enfriamiento_de_newton(Total_cpu_temps[0], Temperatura_Ambiente, k, Times[i]), 2)
        Newton_cpu_temps.append(Newton_temps)

    df = pd.DataFrame({'Tiempos':Times, 'Temperatura CPU': Total_cpu_temps, 'Temperatura Newton': Newton_cpu_temps})
    print(df)
    

    plt.scatter(Times, Total_cpu_temps, color='red', label='Temperatura CPU')
    plt.scatter(Times, Newton_cpu_temps, color='blue', label='Temperatura Newton')
    plt.plot(Times, Total_cpu_temps, color='red', linestyle='-', linewidth=1)
    plt.plot(Times, Newton_cpu_temps, color='blue', linestyle='-', linewidth=1)
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Dispersión de Temperaturas CPU vs Tiempo')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    main()
    stress(2)
    after()