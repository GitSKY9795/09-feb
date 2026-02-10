"""FastAPI backend for FitGuardian AI."""
from __future__ import annotations

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from services.gemini_client import GeminiVisionClient

app = FastAPI(title="FitGuardian AI API", version="2.0.0")
llm_client = GeminiVisionClient()


class AnalysisResponse(BaseModel):
    summary: str
    insights: list[str]
    disclaimer: str


DISCLAIMER = (
    "Educational guidance only. This output is not a medical diagnosis and "
    "must not replace qualified medical consultation."
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/analyze/fitness", response_model=AnalysisResponse)
async def analyze_fitness(
    file: UploadFile = File(...),
    context: str = Form(default=""),
) -> AnalysisResponse:
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Fitness analysis requires image input")

    result = await llm_client.analyze_image(
        image_bytes=await file.read(),
        prompt=(
            "Analyze posture and body mechanics for safe fitness improvement. "
            f"User context: {context}. Keep response concise, actionable, non-diagnostic."
        ),
    )
    return AnalysisResponse(summary=result.summary, insights=result.insights, disclaimer=DISCLAIMER)


@app.post("/api/analyze/medical", response_model=AnalysisResponse)
async def analyze_medical_report(
    file: UploadFile = File(...),
    context: str = Form(default=""),
) -> AnalysisResponse:
    result = await llm_client.analyze_document(
        raw_bytes=await file.read(),
        prompt=(
            "Extract key biomarkers and explain them in simple non-alarming language. "
            "Mention possible (non-diagnostic) conditions and questions for physician. "
            f"User context: {context}"
        ),
    )
    return AnalysisResponse(summary=result.summary, insights=result.insights, disclaimer=DISCLAIMER)


@app.post("/api/analyze/prescription", response_model=AnalysisResponse)
async def analyze_prescription(
    file: UploadFile = File(...),
    context: str = Form(default=""),
) -> AnalysisResponse:
    result = await llm_client.analyze_document(
        raw_bytes=await file.read(),
        prompt=(
            "Identify medicines and explain purpose, common side effects, precautions, "
            "and general timing. Include warnings against self-medication. "
            f"Context: {context}"
        ),
    )
    return AnalysisResponse(summary=result.summary, insights=result.insights, disclaimer=DISCLAIMER)
