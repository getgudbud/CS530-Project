import sounddevice as sd
import numpy as np
import time
from rpi_ws281x import PixelStrip, Color

sd.default.device = 2

# LED strip configuration:
LED_COUNT = 60  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

# Define a function to map a frequency to a color
def freq_to_color(freq):
    # Use a simple linear mapping from frequency to hue
    hue = int((freq - 100) / (2000 - 100) * 360) % 360
    # Convert hue to RGB using HSV color model
    h = hue / 60
    i = int(h)
    f = h - i
    p = 0
    q = int(255 * (1 - f))
    t = int(255 * f)
    if i == 0:
        r, g, b = 255, t, p
    elif i == 1:
        r, g, b = q, 255, p
    elif i == 2:
        r, g, b = p, 255, t
    elif i == 3:
        r, g, b = p, q, 255
    elif i == 4:
        r, g, b = t, p, 255
    else:
        r, g, b = 255, p, q
    return r, g, b

# Define a function to get the dominant frequency of the audio data
def get_dominant_frequency(audio_data, sample_rate):
    # Compute the Fourier transform of the audio data
    fft = np.fft.rfft(audio_data)
    # Compute the magnitude of the Fourier transform
    mag = np.abs(fft)
    # Find the index of the maximum magnitude
    max_index = np.argmax(mag)
    # Convert the index to frequency using the sample rate
    freq = max_index * sample_rate / len(audio_data)
    return freq

# Define a function to capture and process the audio data
def audio_process():
    # Set the sample rate and the duration of the audio data
    sample_rate = 44100
    duration = 0.1
    # Capture the audio data from the microphone
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    # Wait until the recording is finished
    sd.wait()
    # Convert the audio data to a numpy array
    audio_data = np.frombuffer(audio_data, dtype=np.float32)
    # Get the dominant frequency of the audio data
    freq = get_dominant_frequency(audio_data, sample_rate)
    # Map the frequency to a color
    color = freq_to_color(freq)
    # Return the color
    return color

# Main loop
while True:
    # Get the color from the audio data
    color = audio_process()
    # Set the color of the LED strip
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(*color))
    # Show the color of the LED strip
    strip.show()
    # Wait for a short time
    time.sleep(0.01)
