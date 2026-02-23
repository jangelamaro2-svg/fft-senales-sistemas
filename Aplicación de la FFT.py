import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# Definición del dominio del tiempo
# -----------------------------------------
fs = 1000  # frecuencia de muestreo
t = np.linspace(-1, 1, fs)

# -----------------------------------------
# 1. Señales en el dominio del tiempo
# -----------------------------------------

# Pulso rectangular
pulso = np.where(np.abs(t) < 0.2, 1, 0)

# Escalón
escalon = np.where(t >= 0, 1, 0)

# Señal senoidal
f0 = 5  # frecuencia 5 Hz
seno = np.sin(2 * np.pi * f0 * t)

# -----------------------------------------
# 2. Transformada de Fourier
# -----------------------------------------
def calcular_fft(signal):
    fft_signal = np.fft.fft(signal)
    fft_shift = np.fft.fftshift(fft_signal)
    freq = np.fft.fftshift(np.fft.fftfreq(len(signal), d=(t[1]-t[0])))
    return freq, fft_shift

freq_p, fft_p = calcular_fft(pulso)
freq_e, fft_e = calcular_fft(escalon)
freq_s, fft_s = calcular_fft(seno)

# -----------------------------------------
# 3. Graficar resultados
# -----------------------------------------
def graficar(t, signal, freq, fft_signal, titulo):
    plt.figure(figsize=(12,5))
    
    plt.subplot(1,2,1)
    plt.plot(t, signal)
    plt.title("Dominio del Tiempo - " + titulo)
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    
    plt.subplot(1,2,2)
    plt.plot(freq, np.abs(fft_signal))
    plt.title("Magnitud FFT - " + titulo)
    plt.xlabel("Frecuencia")
    plt.ylabel("Magnitud")
    
    plt.tight_layout()
    plt.show()

graficar(t, pulso, freq_p, fft_p, "Pulso Rectangular")
graficar(t, escalon, freq_e, fft_e, "Escalón")
graficar(t, seno, freq_s, fft_s, "Señal Senoidal")