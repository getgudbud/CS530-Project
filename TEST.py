import sounddevice as sd
import numpy as np
import time
from rpi_ws281x import PixelStrip, Color

sd.default.device = 3

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

# Define a function to get the volume of the audio data
def get_volume(audio_data):
    # Compute the root mean square (RMS) of the audio data
    rms = np.sqrt(np.mean(audio_data**2))
    # Convert the RMS to a volume in the range 0-255
    volume = int(rms * 255)
    return volume

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
    # Get the volume of the audio data
    volume = get_volume(audio_data)
    # Return the volume
    return volume

# Define a function to get a color from the rainbow gradient
def get_rainbow_color(i, offset):
    # Map the index plus an offset to a hue in the range 0-360
    hue = (i + offset) % 360
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

# Initialize the offset to 0
offset = 0

# Main loop
while True:
    # Get the volume from the audio data
    volume = audio_process()
    # Set the brightness of the LED strip
    strip.setBrightness(volume)
    # Calculate the number of LEDs to light up based on the volume
    num_leds = int(volume / 255 * LED_COUNT / 2)
    # Turn off all LEDs
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    # Set the color of the middle LEDs and branch out
    for i in range(num_leds):
        # Calculate the index of the LEDs to the left and right of the middle
        left_index = LED_COUNT // 2 - i
        right_index = LED_COUNT // 2 + i
        # Get a color from the rainbow gradient
        color = get_rainbow_color(i, offset)
        # Set the color of the LEDs
        strip.setPixelColor(left_index, Color(*color))
        strip.setPixelColor(right_index, Color(*color))
    # Increment the offset
    offset = (offset + 1) % 360
    # Show the color of the LED strip
    strip.show()
    # Wait for a short time
    time.sleep(0.01)
