from pydantic import BaseModel

class LoanInput(BaseModel):
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Gender_Male: int
    Gender_Female: int
    Married_Yes: int
    Married_No: int
    Dependents_0: int
    Dependents_1: int
    Dependents_2: int
    Dependents_3: int
    Education_Graduate: int
    Education_Not_Graduate: int
    Self_Employed_Yes: int
    Self_Employed_No: int
    Property_Area_Rural: int
    Property_Area_Semiurban: int
    Property_Area_Urban: int


