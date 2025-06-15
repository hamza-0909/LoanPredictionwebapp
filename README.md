# Loan Prediction Project

This project implements a machine learning model for loan prediction, with a complete pipeline from data processing to deployment. The application uses FastAPI for the backend API and HTML CSS JS for the frontend interface.

## Project Structure

```
loan-prediction-project/
│
├── data/                          # Raw & processed data
│   └── train.csv                  # Training dataset
│
├── models/                        # Saved models
│   ├── loan_model.pkl            # Trained model

│
├── notebooks/                     # ML experimentation notebooks
│   └── 01_data_cleaning_and_modeling.ipynb
│
├── app/                           # FastAPI app
│   ├── main.py                    # Main FastAPI server
│   └── model/                     # Model loaded by FastAPI
│       └── loan_model.pkl
│
├── frontend/                      # Streamlit frontend
│   └── index.html
│
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker instructions
├── .gitignore                     # GitHub version control
│
├── mlruns/                        # MLflow experiment logs
│
└── .github/                       # GitHub Actions for CI/CD
    └── workflows/
        └── azure-deploy.yml       # Azure build & deploy pipeline
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd loan-prediction-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Data Processing and Model Training

1. Place your `train.csv` file in the `data/` directory
2. Run the Jupyter notebook:
```bash
jupyter notebook notebooks/01_data_cleaning_and_modeling.ipynb
```
3. Execute all cells in the notebook to train and save the model

### 2. Running the API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000 


## API Endpoints

- `GET /`: Welcome message
- `POST /predict`: Make loan predictions
- `GET /health`: Health check endpoint

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t loan-prediction .
```

2. Run the container:
```bash
docker run -p 8000:8000 loan-prediction
```


## Model Details

The project uses three models for prediction:
- Random Forest Classifier
- Logistic Regression
- XGBoost Classifier

The best performing model is automatically selected and saved for deployment.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
