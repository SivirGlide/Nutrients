from pydantic import BaseModel, EmailStr, Field, field_validator


class ValidateSignupForm(BaseModel):
    name: str = Field(..., min_length=3, max_length=63)
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator('password')
    def validate_password(cls, pwd):
        if len(pwd) < 6:
            raise ValueError('Password must be at least 6 characters')
        return pwd

    @field_validator('confirm_password')
    def matching_password(cls, confirm_password, form):
        if confirm_password != form.data['password']:
            raise ValueError('Password confirmation does not match')
        return confirm_password


class ValidateLoginForm(BaseModel):
    email: EmailStr
    password: str
