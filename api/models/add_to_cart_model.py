from pydantic import BaseModel, field_validator

class CartData(BaseModel):
    count: int
    total: str
    item_id:int

    @field_validator('item_id')
    def validate_item_id(cls, value):
        if value <=0:
            raise ValueError('item_id должен быть больше нуля')
        return value

    @field_validator('total')
    def validate_total(cls, value):
        if len(value) < 1:
            raise ValueError('len(total) должна быть больше 1')
        return value


class AddToCartResponse(BaseModel):
    status: str
    data: CartData






