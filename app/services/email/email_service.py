# email_service.py
import ssl
from email.message import EmailMessage
import aiosmtplib
import certifi
from app.core.config import settings
from langchain.tools import tool

ssl_context = ssl.create_default_context(cafile=certifi.where())

@tool("send_email_tool")
async def send_email_tool(to: str, subject: str, body: str):
    """Send an email with the given recipient, subject, and body."""
    if not all([
        settings.EMAIL_HOST,
        settings.EMAIL_PORT,
        settings.EMAIL_USERNAME,
        settings.EMAIL_PASSWORD,
    ]):
        return {"status": "failed", "reason": "Missing email configuration"}

    msg = EmailMessage()
    msg["From"] = settings.EMAIL_USERNAME   # ✅ matches login
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    await aiosmtplib.send(
        msg,
        hostname=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_USERNAME,
        password=settings.EMAIL_PASSWORD,
        start_tls=True,
        tls_context=ssl_context,
    )
    return {"status": "sent"}
