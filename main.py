# ============================================================
# WhatsApp → Zoho CRM Integration API
# ============================================================

from fastapi import FastAPI

from app.routes.message_routes import router as message_router


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="WhatsApp Zoho Integration API",
    description=(
        "API for receiving WhatsApp group messages "
        "and integrating them with Zoho CRM."
    ),
    version="1.0.0"
)


# ============================================================
# Register API Routes
# ============================================================

app.include_router(message_router)


# ============================================================
# Health Check
# ============================================================

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "WhatsApp Zoho Integration API"
    }