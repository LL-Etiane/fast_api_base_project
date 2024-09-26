from pydantic import field_validator
import re

class EmailValidator:
    @field_validator("email")
    def validate_email(cls, value):
        if not value:
            raise ValueError("Email is required")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Email is invalid")
        return value