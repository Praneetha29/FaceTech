#import io
import uvicorn
from face_recog import get_attendance
from starlette.responses import Response
import numpy as np
from PIL import Image
from fastapi import FastAPI, File
from fastapi import UploadFile

app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)


@app.post("/segmentation")
def get_segmentation_map(file: UploadFile = File(...)):
    """Get segmentation maps from image file"""
    image = np.array(Image.open(file.file))
    # TODO : fix this to work
    #attendance = get_attendance(image)
    attendance = ["pramod","paneer"]
    #bytes_io = io.BytesIO()
    #segmented_image.save(bytes_io, format="PNG")
    return attendance

if __name__ == "__main__":
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)