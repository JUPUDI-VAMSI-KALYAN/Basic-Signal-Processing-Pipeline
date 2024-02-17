import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Generate a simple sine wave signal
def generate_sine_wave(duration, sampling_rate, frequency):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal

# Butterworth low-pass filter implementation
def butter_lowpass_filter(data, cutoff_freq, sampling_rate, order=5):
    nyquist_freq = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data

# Simple amplitude modulation (AM)
def amplitude_modulation(signal, modulation_index):
    return signal * modulation_index * np.cos(2 * np.pi * frequency * t)

# Perform FFT and plot frequency spectrum
def plot_spectrum(signal, sampling_rate):
    freq_spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    plt.plot(freqs, np.abs(freq_spectrum))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum')
    plt.show()

# Integration of the signal processing pipeline
def signal_processing_pipeline(signal, sampling_rate):
    # Filtering
    cutoff_freq = 1000  # Example cutoff frequency
    filtered_signal = butter_lowpass_filter(signal, cutoff_freq, sampling_rate)
    
    # Modulation
    modulation_index = 0.5  
    modulated_signal = amplitude_modulation(filtered_signal, modulation_index)
    
    # Spectral Analysis
    plot_spectrum(modulated_signal, sampling_rate)

# Example usage
if __name__ == "__main__":
    duration = 1.0  # Duration of the signal in seconds
    sampling_rate = 44100  # Sampling rate in Hz
    frequency = 440  # Frequency of the sine wave in Hz (A4 note)
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = generate_sine_wave(duration, sampling_rate, frequency)
    
    signal_processing_pipeline(signal, sampling_rate)
