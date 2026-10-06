from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FitAI API",
    description="AI-powered virtual fitting backend"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():

    return {
        "project": "FitAI",
        "message": "FitAI Backend is running",
        "status": "success"
    }


@app.post("/analyze")
async def analyze_photo(
    file: UploadFile = File(...)
):

    return {
        "success": True,
        "message": "Photo received successfully",
        "estimated_height": 165,
        "body_profile": "Medium",
        "recommended_size": "M"
    }


@app.post("/recommend")
async def recommend_outfit(data: dict):

    occasion = data.get("occasion")
    outfit = data.get("outfit")
    color = data.get("color")
    budget = data.get("budget")

    return {
        "success": True,
        "occasion": occasion,
        "outfit": outfit,
        "color": color,
        "budget": budget,
        "recommended_size": "M"
    }
