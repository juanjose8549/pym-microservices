import strawberry
from typing import Optional
from odmantic import Model

@strawberry.type
class Advisor:
    id: strawberry.ID
    name: str
    expertise: str = "Finance"