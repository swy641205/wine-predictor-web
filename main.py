from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

data = pd.read_csv("winequality-white.csv", delimiter=";")
coefficients = {
    'const': 150.1928,
    'fixed acidity': 0.0655,
    'volatile acidity': -1.8632,
    'residual sugar': 0.0815,
    'free sulfur dioxide': 0.0037,
    'density': -150.2842,
    'pH': 0.6863,
    'sulphates': 0.6315,
    'alcohol': 0.1935
}


@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.get("/random_data/")
def random_data():
    # 從資料表中隨機選擇一筆數據
    random_row = data.sample().iloc[0].to_dict()
    return random_row


@app.post("/predict/")
async def predict_quality(
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    residual_sugar: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...)
):
    values = {
        'fixed acidity': fixed_acidity,
        'volatile acidity': volatile_acidity,
        'residual sugar': residual_sugar,
        'free sulfur dioxide': free_sulfur_dioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }

    predicted_quality = coefficients['const']
    for key, value in values.items():
        predicted_quality += coefficients[key] * value

    return {"quality": predicted_quality}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
