# MachineDowntime
README: CSV-Based Machine Learning API

Overview

This API allows users to:
	1.	Upload a CSV file for training a machine learning model.
	2.	Train the model using the uploaded dataset.
	3.	Make predictions using the trained model.

The API uses FastAPI for building endpoints and scikit-learn for machine learning tasks.

Setup Instructions

1. Prerequisites
	•	Python 3.8 or higher
	•	Recommended: Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate



2. Install Dependencies

Run the following command to install the required packages:

pip install fastapi uvicorn scikit-learn pandas

3. Save the Code

Save the API code into a file named main.py.

4. Run the API

Start the server using the following command:

uvicorn main:app --reload

The server will start running at http://127.0.0.1:8000.

5. Access the Documentation

FastAPI provides interactive API documentation at:
	•	Swagger UI: http://127.0.0.1:8000/docs
	•	ReDoc: http://127.0.0.1:8000/redoc

API Endpoints

1. Upload Dataset
	•	Endpoint: /upload
	•	Method: POST
	•	Description: Upload a CSV file for training.
	•	Headers:
	•	Content-Type: multipart/form-data
	•	Body:
	•	A CSV file with a target column for the dependent variable.

Example Request:

curl -X POST "http://127.0.0.1:8000/upload" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@path/to/dataset.csv"

Example Response:

{
  "message": "Dataset uploaded successfully and split into train/test."
}

2. Train Model
	•	Endpoint: /train
	•	Method: POST
	•	Description: Train a machine learning model on the uploaded dataset.

Example Request:

curl -X POST "http://127.0.0.1:8000/train"

Example Response:

{
  "message": "Model trained successfully."
}

3. Make Predictions
	•	Endpoint: /predict
	•	Method: POST
	•	Description: Make predictions using the trained model.
	•	Headers:
	•	Content-Type: application/json
	•	Body:
	•	A JSON object containing feature values for prediction.

Example Request:

curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"input": [{"feature1": 10, "feature2": 20}, {"feature1": 15, "feature2": 25}]}'

Example Response:

{
  "predictions": [30.5, 35.7]
}

Expected Dataset Format
	•	The uploaded CSV file must include:
	•	Independent features as columns (e.g., feature1, feature2).
	•	A column named target for the dependent variable.

Example Dataset:

feature1	feature2	target
10	20	30
15	25	40

Error Handling
	•	Missing CSV File:

{
  "error": "Please upload a valid CSV file."
}


	•	Missing target Column:

{
  "error": "CSV must include a 'target' column for training."
}


	•	Model Not Trained:

{
  "error": "Model not trained. Use the /train endpoint first."
}

Testing the API

Use tools like Postman, curl, or FastAPI’s built-in Swagger UI to test the API.

License

This project is open-source and available for personal or commercial use.
