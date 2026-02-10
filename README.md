# FitGuardian AI — Modern AI Fitness + Health Assistant

## 1) High-level product vision
FitGuardian AI is an AI-powered wellness copilot that merges **fitness image intelligence** (pose/body review) with **medical-document simplification** and **prescription education**. It helps users make safer day-to-day decisions through clear, non-alarming insights, while strictly avoiding diagnosis and continuously reinforcing medical disclaimers.

## 2) Feature list (preserved + new)
### Preserved core features
- AI fitness agent experience.
- Image-based body/pose/fitness analysis.
- Gemini API-ready architecture for LLM + vision.
- Actionable fitness insights.

### New mandatory features
- Medical report upload (PDF/images) with key metric extraction.
- Plain-language explanation of blood/lab/medical findings.
- Prescription and medicine recognition + usage education.
- Misuse/self-medication warnings and side-effect awareness.
- Unified fitness + medical context planner.

### Additional innovation
- AI Coach Console (chat-like guided output panel).
- Dark/light accessibility mode.
- Modular multi-model adapter design (Gemini primary, extensible to others).
- API layer structured for future habit tracking, reminders, and wearable ingestion.

## 3) Tech stack chosen (with reasons)
- **Frontend:** HTML/CSS/Vanilla JS for a zero-friction starter that can be quickly migrated to Next.js/React.
- **Backend API:** FastAPI for typed endpoints, async file handling, and production-friendly routing.
- **AI Layer:** Provider abstraction (`GeminiVisionClient`) enabling Gemini now and future OpenAI/Claude fallbacks.
- **Data Layer (recommended next):** PostgreSQL + pgvector for user profile, analysis history, and semantic retrieval.
- **Infra (recommended next):** Docker + reverse proxy + object storage for report/image files.

## 4) System architecture
- **Client App** uploads image/document inputs and user context.
- **API Gateway (FastAPI)** validates files and routes requests by domain (`fitness`, `medical`, `prescription`).
- **AI Orchestrator** builds safe prompts, calls Gemini vision/text model, enforces disclaimers.
- **Safety Layer** blocks diagnostic wording and adds risk-aware language.
- **Persistence Layer (next step)** stores analysis history and user goals.
- **Planner Module** merges outputs into a weekly integrated health-fitness plan.

## 5) Data flow (textual diagram)
1. User uploads fitness image / report / prescription in UI.
2. Frontend sends multipart request to `/api/analyze/*` endpoint.
3. Backend validates MIME type + request shape.
4. AI adapter sends prompt + file content to Gemini vision/text flow.
5. Result is normalized into `{summary, insights, disclaimer}` schema.
6. Response returns to UI and is rendered in AI Coach Console.
7. (Future) Result is stored for trend tracking and personalized planning.

## 6) Security & privacy considerations
- Explicit non-diagnostic disclaimers on every medical-related response.
- Avoid storing PHI by default; use short-lived processing where possible.
- Encrypt data at rest and in transit when persistence is enabled.
- Role-based access and audit logs for administrative actions.
- Input file validation + size limits + malware scanning in production.
- Prompt-hardening to reduce unsafe outputs and hallucinated treatment advice.

## 7) Key AI components
- **Prompt templates** per domain (fitness, report, prescription).
- **Model adapter layer** for provider portability.
- **Safety policy injector** for plain-language, non-alarming outputs.
- **Integrated recommendation composer** to unify exercise, diet, and lifestyle guidance.

## 8) Sample implementation snippets
- Frontend orchestration: `assets/app.js`
- API contract + endpoints: `backend/main.py`
- Gemini adapter stub: `backend/services/gemini_client.py`

## 9) Future scalability roadmap
- Add auth (OIDC), tenant isolation, and encrypted profile vault.
- Introduce event-driven jobs for OCR, summarization, and report trend charts.
- Add wearable integrations (Apple Health/Fitbit/Garmin).
- Implement multilingual output and region-aware nutrition advice.
- Launch clinician handoff mode (downloadable report packet with timeline).

---

### Medical disclaimer
This project provides educational information only and does **not** provide medical diagnosis, treatment plans, or emergency support. Always consult a licensed clinician for diagnosis and treatment decisions.
