# About
This is a project done by Diego De La Toba and Ian Sanchez as a final project for CS530. 

# Goal
The primary aim of this project is to design and implement an LED display system using a Raspberry Pi that synchronizes audio input in real-time, offering visually stunning patterns to enhance any audio experience. While digitizing and controlling LED lights may appear mundane, the real-world applications are vital

# Different Files

## `install.py`
Script will install all the dependencies you need to run the program. Run with

```shell
cd CS530/installation/

sudo python3 install.py
```

## `frequency_to_color.py`
Script will take in audio input and analyze different frequencies rersulting in different patterns.

```shell
cd CS530/python/

sudo python3 frequency_to_color.py
```
## `rainbow_volume_bar.py`
Script will take in audio input and analyze the volume level to create a volume bar effect on the LED strip that starts at the middle of the strip branching out in both directions as the music gets louder. a unique rainbow pattern

```shell
cd CS530/python/

sudo python3 rainbow_volume_bar.py
```
## `volume_warning.py`
Script will analyze volume levels and warn users about high volume levels. Green: Good. Yellow: Ok. Red: Bad.

```shell
cd CS530/python/

sudo python3 volume_warning.py
```

# Setting Up Your RasberryPi
## Python Dependencies
Code is compatible with Python 2.7 or 3.5. A few Python dependencies must also be installed:
- Numpy
- Scipy (for digital signal processing)
- RPI_WS281x (for led strip controll)
- PyAudio (for recording audio with microphone)
- Sounddevice (for mic input)

### Install dependencies with `install.py`

This project makes it very simple and easy to install all the dependencies you need to run the program. so you'll want to start off by entering the CS 530 directory with the following shell command:

```shell
cd CS530
```

Once you are in the CS530 directory, run this command:

```shell
sudo python3 install.py
```

This process should take a couple minutes assuming your raspberry pi has to install all of the dependencies however, this will truly depend on the speed of your internet and processor.

## Modify `config.py` to meet your needs

This file will contain all the configuration data that is variable between set ups. Our set up was using a strip with exactly 30 LEDs and our audio device index two. 

```python
'audio_device': 2,
'led_count': 60,
'led_pin': 18,
'led_freq_hz': 800000,
'led_dma': 10,
'led_brightness': 255,
'led_invert': False
```
# 

