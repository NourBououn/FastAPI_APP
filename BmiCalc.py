from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class BMIOutput(BaseModel):
    bmi: float
    message: str
    
#api app creation
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
#Spécifier endpoints ekher thnia yusslelha l app 

@app.get("/") #decorator
def Hi():
    return {"message": "Marahaba FastAPI "}
#In API we use JSON.
#Specifier new endpoint
@app.get("/calculate_bmi")
def calculate_bmi(weight: float = Query(..., gt=50,lt=300, description="Weight in kg" ) ,
                  height: float = Query(..., gt=1,lt=3, description="Height in cm" )):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        message = "under weight"
    elif 18.5 <= bmi < 35 :
        message = "Normal weight"
    elif 25 <= bmi < 30:
         message = "Over weight"
    else:
        message = "So overweight"          
    
    return BMIOutput(bmi=bmi,message=message)
#Automatic documentation : tawthi9 té2l9a2i
#http://127.0.0.1:8000/docs o naamlou tryout o naamlou test o njarbou l code
#Automatic validation : ta7a9ou mel bayanet : from fastapi import FastAPI, Query nzidou query lahna 
#Pyndantic da3ém l bayent wel ta79i9
#On peut ajouter CORSmiddlewear pour lier avec source web
