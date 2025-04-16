from wsgiref.validate import validator

from pydantic import BaseModel, EmailStr, Field


class ValidateSignupForm(BaseModel):
    name: str = Field(..., min_length=3, max_length=63)
    email: EmailStr
    password: str
    confirm_password: str

    @validator('password')
    def validate_password(cls, password):
        if len(password) < 6:
            raise ValueError('Password must be at least 6 characters')
        return password

    @validator('confirm_password')
    def matching_password(cls, confirm_password, form):
        if confirm_password != form.password:
            raise ValueError('Password confirmation does not match')
        return confirm_password

