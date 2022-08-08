# Yolov5 Custom Object Detection (Logo Detection)

Custom Object Detection model trained and deployed using FastAPI

## To run the Image on Docker

#### Step 1
Run these docker commands
```
$ docker pull ankitgodle/detect_logo_api
$ docker run -p 8000:8000 --name detect_logo ankitgodle/detect_logo_api
```
#### Step 2
After the app startup is complete

Open - `http://0.0.0.0:8000/docs/` in your browser

#### Step 3
Use POST/ api/detect/logo to upload the image and get the predictions

## To run the FastAPI locally
Clone repo and install requirements.txt in a Python>=3.9.0 environment
```
$ git clone https://github.com/AnkitGodle/Logo_Detect_API
$ cd Logo_Detect_API
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
