# Loan Prediction Project

This project implements a machine learning model for loan prediction, with a complete pipeline from data processing to deployment. The application uses FastAPI for the backend API and Streamlit for the frontend interface.

## Project Structure

```
loan-prediction-project/
│
├── data/                          # Raw & processed data
│   └── train.csv                  # Training dataset
│
├── models/                        # Saved models
│   ├── loan_model.pkl            # Trained model
│   ├── encoder.pkl               # Categorical encoder
│   ├── scaler.pkl                # Numerical scaler
│   └── feature_names.pkl         # Feature names
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
│   └── streamlit_app.py
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
The API will be available at http://localhost:8000

### 3. Running the Frontend

Start the Streamlit app:
```bash
streamlit run frontend/streamlit_app.py
```
The frontend will be available at http://localhost:8501

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

## Azure Deployment

The project includes a GitHub Actions workflow for automatic deployment to Azure App Service. To set up deployment:

1. Create an Azure App Service
2. Add the following secrets to your GitHub repository:
   - `AZURE_CREDENTIALS`: Azure service principal credentials
   - `DOCKER_HUB_USERNAME`: Docker Hub username
   - `DOCKER_HUB_ACCESS_TOKEN`: Docker Hub access token

3. Update the following variables in `.github/workflows/azure-deploy.yml`:
   - `AZURE_WEBAPP_NAME`: Your Azure App Service name
   - `DOCKER_IMAGE_NAME`: Your Docker image name

4. Push to the main branch to trigger deployment

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