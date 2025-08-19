from pydantic import BaseModel, EmailStr, Field

class EmailRequest(BaseModel):
    to: EmailStr = Field(..., description="Recipient email address")
    subject: str = Field(..., description="Email subject line")
    body: str = Field(..., description="Plain text email content")
