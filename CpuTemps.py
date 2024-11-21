import wmi

def obtener_temperatura_cpu():
    try:
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperatura = w.Sensor()
        for sensor in temperatura:
            if sensor.SensorType == u'Temperature' and sensor.Name == u'CPU Package':
                return sensor.Value
    except Exception as e:
        return -2
    

print(obtener_temperatura_cpu())