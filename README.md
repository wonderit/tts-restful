## How to install

1.  Install packages offline

``` shell
# extract files (already extracted)
#tar -zxf libs.tar.gz

# install libs and dependencies
pip install -r libs/requirements.txt --no-index --find-links libs
```

2.  Run RESTful server

``` shell
# run server
./run.sh

# check log
tail -f main.log
vi main.log
```

## API

### /tts

-   `POST` : send TTS request
- `json body` :
    ```json
    {       
        'text': 'This is a test.',
        'lang': 'es',
        'gender': 0 // male : 0, female : 1   
    }
    ```
  
### /tts/:file_id

-   `GET` : get wav file

## How to Use

-   Send tts request

``` python
import json
import requests

url = 'http://127.0.0.1:5000/tts'

input_parameters = {
    'text': 'This is a test.',
    'lang': 'es',
    'gender': 0 # male : 0, female : 1
}
input_json = json.dumps(input_parameters)
response = requests.post(url, input_json)
print(response.json())
```

``` shell
# run tts request test written in python
python api_post.py
```

-   Download wav file

``` python
import requests

# URL from TTS request result
url = 'http://127.0.0.1:5000/tts/6nipqQGMQyeRfUNPSrHXwu'

response = requests.get(url)
with open('api_get_wav_test.wav', mode='wb') as localfile:
    localfile.write(response.content)
```

``` shell
# run download wav file test written in python
python api_get_wav.py
```

### 참고사항

#### 방화벽 설정

-   TTS 요청 시, 혹은 요청 후에 생성되는 url의 ip, port에 대한 방화벽
    해제 필요.
    -   tts request url :
        http://127.0.1.58:5000/tts/6nipqQGMQyeRfUNPSrHXwu
    -   tts download url : http://127.0.1.58:5000/tts

#### Export packages offline

``` shell
# create requirements.txt
pip freeze > requirements.txt

# download files from requirements.txt
mkdir libs && pip download -r requirements.txt -d libs

# add requirements.txt to the folder
cp requirements.txt ./libs/

# archive libs
tar -zcf libs.tar.gz libs
```
