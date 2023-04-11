import uvicorn
from face_recog import get_attendance
from starlette.responses import Response
import numpy as np
from PIL import Image
from fastapi import FastAPI, File
from fastapi import UploadFile
from supabase import create_client, Client

app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)


# @app.post("/segmentation")
# def get_segmentation_map(file: UploadFile = File(...)):
#     """Get segmentation maps from image file"""
#     image = np.array(Image.open(file.file))
#     # TODO : fix this to work
#     #attendance = get_attendance(image)
#     attendance = ["pramod","paneer"]
#     #bytes_io = io.BytesIO()
#     #segmented_image.save(bytes_io, format="PNG")
#     return attendance

@app.get("/studentEntry")
def studentEntry(name:str,roll:int):
   url: str = 'https://fxbseklwnpspoqnezkrc.supabase.co'
   key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ4YnNla2x3bnBzcG9xbmV6a3JjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzk2NjQ0ODIsImV4cCI6MTk5NTI0MDQ4Mn0.7IiQaOdP52xzTEf5-ASz77rZuI2ix7xPuWE0yJxvfUY'
   supabase: Client = create_client(url, key)
   data, count = supabase.table('student').insert({"rollid": roll, "name": name , "imageid":link}).execute()
   response = supabase.table('student').select("*").execute()
   data=response.data;
   return data

@app.get("/viewclassdata/")
def classData(id:int):
   url: str = 'https://fxbseklwnpspoqnezkrc.supabase.co'
   key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ4YnNla2x3bnBzcG9xbmV6a3JjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzk2NjQ0ODIsImV4cCI6MTk5NTI0MDQ4Mn0.7IiQaOdP52xzTEf5-ASz77rZuI2ix7xPuWE0yJxvfUY'
   supabase: Client = create_client(url, key)
   response=supabase.table('ec100'+str(id)).select("*").execute()
   data=response.data
   return data

@app.get("/viewstudentdata")
def studentData(id:int):
   data=[]
   url: str = 'https://fxbseklwnpspoqnezkrc.supabase.co'
   key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ4YnNla2x3bnBzcG9xbmV6a3JjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzk2NjQ0ODIsImV4cCI6MTk5NTI0MDQ4Mn0.7IiQaOdP52xzTEf5-ASz77rZuI2ix7xPuWE0yJxvfUY'
   supabase: Client = create_client(url, key)
   for i in range(3):
      response=supabase.table('ec100'+str(i)).select("*").eq("rollid",id).execute()
      data_class=response.data
      data.append(data_class)
   return data

if __name__ == "__main__":
   uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)