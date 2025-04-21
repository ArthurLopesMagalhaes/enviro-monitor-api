# sensor_reader.py (simulado)
import random
import time

def read_temperature(canal=None, tipo=None) -> float:
    # Simula uma temperatura entre 20°C e 80°C com leve flutuação
    temperature = random.uniform(20.0, 80.0)
    time.sleep(0.1)  # simula tempo de leitura
    return temperature
