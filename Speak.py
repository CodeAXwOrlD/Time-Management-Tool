import requests # pip install requests
from pygame import mixer # pip install pygame
import os
from typing import Union # pip install typing
from os import getcwd


def generate_audio(message: str,voice : str = "Aditi"):
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"

    headers = {'User-Agent':'Mozilla/5.0(Maciontosh;intel Mac OS X 10_15_7)AppleWebKit/537.36(KHTML,like Gecoko)Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None

def speak(message: str, voice: str = "Aditi", folder: str = "", extension: str = ".mp3") -> Union[None,str]:
    try:
        result_content = generate_audio(message,voice)
        if result_content:
            file_path = os.path.join(folder, f"output{extension}")
            with open(file_path, "wb") as audio_file:
                audio_file.write(result_content)
            mixer.init()
            mixer.music.load(file_path)
            mixer.music.play()
            while mixer.music.get_busy():
                pass
            mixer.quit()
            return file_path
        else:
            return None
    except Exception as e:
        print(e)
