import numpy as np
import sounddevice as sd

from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

def audio_callback(indata, frames, time, status):
    normal_volume = np.linalg.norm(indata) * 10
    global bar
    bar = "#" + str(normal_volume)

def main():
    global bar
    
    bar = ""

    with Live(Text("", style="bold green"), refresh_per_second=20) as live:
        with sd.InputStream(callback=audio_callback, channels=1, samplerate=44100):
            while True:
                live.update(Text(bar, style="bold green"))

main()