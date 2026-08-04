# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:57:39 2023

@author: Pablo
"""

import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])