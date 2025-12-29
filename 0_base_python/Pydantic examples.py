from datetime import datetime
from pydantic import BaseModel,PositiveInt

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None
    tastes: dict[str,PositiveInt]

external_data = {
    'id': '123',
    'signup_ts': '2023-01-01 00:00:00',
    'tastes': {'coding': 10, 'sleeping': 7, 'reading': 5}
}

user = User(**external_data)
print(user)
print(user.model_dump())