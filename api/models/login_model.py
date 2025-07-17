from pydantic import BaseModel,field_validator

class LoginErrors(BaseModel):
    auth: list
    data: list

class LoginData(BaseModel):
    redirect_code: None
    redirect_url: str

    @field_validator('redirect_url')
    def validate_redirect_url(cls, value):
        if len(value) < 0:
            raise ValueError('Длина url должна быть больше 0')
        return value

class LoginErrorResponse(BaseModel):
    status: str
    data: LoginErrors

class LoginDataResponse(BaseModel):
    status: str
    data: LoginData




