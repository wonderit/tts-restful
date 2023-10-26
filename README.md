## How to install
0. Set virtualenv (`username`변경 필요)

``` shell
# move to folder
cd /home/`username`/workplace/tts

# check python version=3.10
python -V

# install pip venv
python -m venv tts-env

# activate venv
source tts-env/bin/activate

# install dependencies
pip install -r libs-py310/requirements.txt --no-index --find-links libs-py310
```

1. Edit tts.service file (`username`, `/home/wonderit/workplace/tts`폴더 path 변경 필요)
```shell
[Unit]
Description=Service to run TTS RESTful API
After=network.target
StartLimitIntervalSec=100
StartLimitBurst=5

[Service]
Restart=always
RestartSec=10
User=`username`
ExecStart=`/home/wonderit/workplace/tts`/tts-env/bin/python main.py
StandardOutput=append:`/home/wonderit/workplace/tts`/stdout.log
StandardError=append:`/home/wonderit/workplace/tts`/std_error.log

[Install]
WantedBy=multi-user.target
```

2.  Install packages offline

``` shell
# extract files (already extracted)
#tar -zxf libs.tar.gz

# conda create env or use local python 
#conda create -n tts-restful python=3.10
#conda activate tts-restful

# install libs and dependencies
pip install -r libs-py310/requirements.txt --no-index --find-links libs-py310
```

3. Set systemd.service
```
# copy service file
sudo cp tts.service /etc/systemd/system/tts.service

# reload daemon
sudo systemctl daemon-reload

# run service
sudo systemctl start tts

# stop service
sudo systemctl stop tts

# **enable starting automatically on startup**
sudo systemctl enable tts
sudo systemctl disable tts

# check if service is running
sudo systemctl status tts

# check if its crashing
journalctl -xe

```

## How to run local
1.  Run RESTful server

``` shell
# change permission
chmod 707 run.sh

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
- python version : 3.10

-   TTS 요청 시, 혹은 요청 후에 생성되는 url의 ip, port에 대한 방화벽
    해제 필요.
    -   tts request url :
        http://127.0.1.1:5000/tts/6nipqQGMQyeRfUNPSrHXwu
    -   tts download url : http://127.0.1.1:5000/tts

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
