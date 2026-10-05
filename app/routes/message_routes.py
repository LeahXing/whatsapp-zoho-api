# ============================================================
# WhatsApp Message API Routes
# ============================================================

from fastapi import APIRouter, HTTPException

from app.schemas.message_schema import WhatsAppMessageRequest
from app.services.message_service import process_whatsapp_message


# ============================================================
# Router Configuration
# ============================================================

router = APIRouter(
    prefix="/api/v1/messages",
    tags=["WhatsApp Messages"]
)


# ============================================================
# Receive WhatsApp Message
# ============================================================

@router.post("")
def receive_whatsapp_message(
    message: WhatsAppMessageRequest
):
    """
    Receive one WhatsApp message and store it in Zoho CRM.

    Workflow:
        1. Validate incoming JSON.
        2. Check Message_ID for duplicate.
        3. Store new message in WhatsApp_Messages.
        4. Return processing result.
    """

    try:
        result = process_whatsapp_message(message)

        return result

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )