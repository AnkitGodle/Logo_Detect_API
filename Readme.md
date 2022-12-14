# Yolov5 Custom Object Detection (Logo Detection)

Custom Object Detection model trained and deployed using FastAPI

## To run the Docker image

### Step 1
Run these docker commands
```
$ docker pull ankitgodle/detect_logo_api
$ docker run -p 8000:8000 --name detect_logo ankitgodle/detect_logo_api
```
### Step 2
After the app startup is complete

Open URL - http://0.0.0.0:8000/docs/ in your browser. 
If you get Error 502, try URL - http://127.0.0.1:8000/docs

### Step 3
Use POST/ api/detect/logo to upload the image and get the inferences

## To run the FastAPI locally
Clone repo, install requirements.txt in a Python>=3.9.0 environment and follow step 2 and step 3 from above
```
$ git clone https://github.com/AnkitGodle/Logo_Detect_API
$ cd Logo_Detect_API
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## General Information

[app](https://github.com/AnkitGodle/Logo_Detect_API/tree/main/app) - Contains the trained model, FastAPI code

[logo_data](https://github.com/AnkitGodle/Logo_Detect_API/tree/main/logo_data) - Contains training/test data

[Yolo_train.ipynb](https://github.com/AnkitGodle/Logo_Detect_API/blob/main/Yolo_train.ipynb) - Model training code
