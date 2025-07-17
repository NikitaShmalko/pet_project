from pydantic import BaseModel


class Auth(BaseModel):
    auth: list[str]


class ErrorResponse(BaseModel):
    status: str
    errors: Auth
    data: list

class Data(BaseModel):
    redirect_url: str
    redirect_code: None


class SuccessResponse(BaseModel):
    status: str
    data: Data

    test test