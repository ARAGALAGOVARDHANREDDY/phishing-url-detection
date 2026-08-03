from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import Predictor

app = FastAPI()

# Allow the frontend (served from a different origin) to call this API.
# allow_origins=["*"] is fine for local development; restrict it to your
# actual frontend domain(s) before deploying this publicly.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = Predictor()


class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "API Running Successfully"}


@app.post("/predict")
def predict(data: URLRequest):
    result = predictor.predict(data.url)

    if result is None:
        return {"error": "Feature Extraction Failed"}

    label = "Phishing Website" if result["prediction"] == 1 else "Legitimate Website"

    return {
        "url": data.url,
        "prediction": label,
        "class": result["prediction"],
        "confidence": round(result["confidence"] * 100, 2)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)