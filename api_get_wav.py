# -*- coding: utf-8 -*-
import requests

# URL from TTS request result
url = 'http://127.0.0.1:5000/tts/6nipqQGMQyeRfUNPSrHXwu'

response = requests.get(url)
with open('api_get_wav_test.wav', mode='wb') as localfile:
    localfile.write(response.content)


