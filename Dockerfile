FROM python:3.9.13
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r ./requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--reload" ]
