import pyaudio
import numpy as np
from matplotlib import pyplot as plt


FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

pa = pyaudio.PyAudio()

stream = pa.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print('start recording')

seconds = 8
frames = []
second_tracking = 0
second_count = 0
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
    second_tracking += 1
    if second_tracking == RATE/FRAMES_PER_BUFFER:
        second_count += 1
        second_tracking = 0
        print(f'Time Left: {seconds - second_count} seconds')


stream.stop_stream()
stream.close()
pa.terminate()

onef = np.frombuffer(frames[0], dtype=np.int16)

num_frames = 40
frame_size = 3200
sampling_rate = 16000  # Adjust based on your actual audio

# Generate fake data similar to your frame structure


# Create a time axis in seconds
time_per_sample = 1 / sampling_rate  # Time per sample
time_axis = np.linspace(0, frame_size * time_per_sample, frame_size)  # Time for one frame

# Plot multiple frames in a continuous time series
plt.figure(figsize=(12, 6))

for i in range(num_frames):
    start_time = i * frame_size * time_per_sample  # Offset each frame correctly in time
    plt.plot(time_axis + start_time, np.frombuffer(frames[i], dtype=np.int16), alpha=0.7, label=f"Frame {i+1}")

# Labels and title
plt.title("Time Series Audio Frames Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()