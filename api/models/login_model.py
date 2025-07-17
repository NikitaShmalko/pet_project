from pydantic import BaseModel,field_validator
from typing import Optional, Union, List


class LoginErrors(BaseModel):
    auth: List[str]

class LoginErrorResponse(BaseModel):
    status: str
    errors: LoginErrors
    data: Union[LoginErrors, List]

class LoginData(BaseModel):
    redirect_code: Optional[str] = None
    redirect_url: str

    @field_validator('redirect_url')
    def validate_redirect_url(cls, value):
        if len(value) == 0:
            raise ValueError('Длина url должна быть больше 0')
        return value

class LoginDataResponse(BaseModel):
    status: str
    data: LoginData




