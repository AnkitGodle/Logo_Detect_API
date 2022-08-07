from webbrowser import get
import uvicorn
from fastapi import FastAPI
from fastapi import UploadFile, File
from starlette.responses import Response
from PIL import Image
from app.detect_logo import get_yolov5,read_image
import io



app=FastAPI()
model = get_yolov5()
@app.get('/')
def root():
    return{"message": "Please use 'https://0.0.0.0:8000/docs' to run the logo detector"}


@app.post('/api/detectlogo')
async def detect_logo(file: bytes = File(...)):
    image = read_image(file)
    results = model(image)
    results.crop()
    results.render()
    for img in results.imgs:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="jpeg")
    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

