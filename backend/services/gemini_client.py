"""Gemini client abstraction with room for multi-model routing."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLMResult:
    summary: str
    insights: list[str]


class GeminiVisionClient:
    async def analyze_image(self, image_bytes: bytes, prompt: str) -> LLMResult:
        # Replace this stub with the Gemini SDK call.
        # Keep implementation isolated to enable OpenAI/Claude fallback routing.
        return LLMResult(
            summary="Posture suggests mild shoulder forward-roll and weak hip stability.",
            insights=[
                "Prioritize thoracic mobility warmup before upper body sessions.",
                "Add unilateral glute strengthening 3x/week.",
                "Use progressive overload only when form remains stable.",
            ],
        )

    async def analyze_document(self, raw_bytes: bytes, prompt: str) -> LLMResult:
        return LLMResult(
            summary="Report extracted and simplified successfully.",
            insights=[
                "1-2 metrics appear outside common ranges; monitor trends, not one value.",
                "Discuss medication/lab interactions with your physician.",
                "Lifestyle and follow-up tests can often improve markers over time.",
            ],
        )
