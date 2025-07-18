from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware

# api.ip....
app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class PatientData(BaseModel):
    # CRP : float  
    ESR : float  
    RBC_Count : float  
    PLT_Count : float  
    Hemoglobin : float  
    MCH : float  
    Sickness_Duration_Months : float  
    Reticulocyte_Count : float  
    Monocytes : float  
    WBC_Count : float  
    MPV : float  
    MBL_Level : float  
    MCV : float  
    RDW : float  
    C3 : float  
    Hematocrit : float  
    Lymphocytes : float  
    MCHC : float  
    Neutrophils : float  
    Basophils : float  
    Eosinophils : float  
    Age : float  
    C4 : float  
    Esbach : float

# Chargement des artefacts
try:
    model = joblib.load('common_svc_model.pkl')
    scaler = joblib.load('common_features_scaler.pkl')

    with open('diagnosis.json', 'r') as f:
        label_mapping = json.load(f)
    feature_names = joblib.load('common_features.pkl')

except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement des artefacts: {str(e)}")

@app.post("/predict")
async def predict(patient: PatientData):
    try:
        input_features = [
            patient.MPV,
            patient.Lymphocytes,
            patient.Esbach,
            patient.MBL_Level,
            patient.Basophils,
            patient.WBC_Count,
            patient.Age,
            patient.Sickness_Duration_Months,
            patient.Hemoglobin,
            patient.Eosinophils,
            patient.C4,
            patient.Reticulocyte_Count,
            patient.Neutrophils,
            patient.PLT_Count,
            patient.RBC_Count,
            patient.Monocytes,
            patient.C3,
            patient.Hematocrit,
            patient.MCV,
            patient.MCHC,
            patient.RDW,
            patient.ESR,
            patient.MCH,
            ]
        
        # Prétraitement et prédiction
        input_df = pd.DataFrame([input_features], columns=feature_names)
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        
        return {
            "diagnosis": label_mapping[str(prediction[0])],
            "probability": float(model.predict_proba(input_scaled).max()),
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/features")
async def get_features():
    return {"features": feature_names}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)