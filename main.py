from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import io

app = FastAPI()

# Global variables for storing the model, data
model = None
X_train, X_test, y_train, y_test = None, None, None, None


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global X_train, X_test, y_train, y_test
    
    if file.content_type != "text/csv":
        return JSONResponse(content={"error": "Please upload a valid CSV file."}, status_code=400)
    
    # Read the file
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    
    if "target" not in df.columns:
        return JSONResponse(content={"error": "CSV must include a 'target' column for training."}, status_code=400)
    
    # Split features, target
    X = df.drop(columns=["target"])
    y = df["target"]
    
    # Split into train - test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return {"message": "Dataset uploaded successfully and split into train/test."}


@app.post("/train")
def train_model():
    global model, X_train, y_train
    
    if X_train is None or y_train is None:
        return JSONResponse(content={"error": "No dataset uploaded. Use the /upload endpoint first."}, status_code=400)
    
    # Training the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return {"message": "Model trained successfully."}


@app.post("/predict")
def predict(data: dict):
    global model
    
    if model is None:
        return JSONResponse(content={"error": "Model not trained. Use the /train endpoint first."}, status_code=400)
    
    # Extract data for prediction
    X_new = pd.DataFrame(data["input"])
    
    # Generate predictions
    predictions = model.predict(X_new).tolist()
    return {"predictions": predictions}