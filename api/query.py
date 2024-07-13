import strawberry
from typing import Optional, List

from .database.db_models import Advisor as AdvisorDBModel
from .models.graphql_types import Advisor as AdvisorModel
from .resolvers.query_resolvers import get_all_advisors

from fastapi import HTTPException

@strawberry.federation.type(keys=["id"])
class Thing:
    id: strawberry.ID
    name: Optional[str]

    @classmethod
    def resolve_reference(cls, **representation) -> "Thing":
        id_ = strawberry.ID(representation["id"])

        return cls(id=id_, name="Thing")


@strawberry.type
class Query:
    @strawberry.field
    def thing(self, id: strawberry.ID) -> Optional[Thing]:
        return Thing(id=id, name="Thing")

    @strawberry.field
    async def allAdvisors() -> Optional[List[AdvisorModel]]:
        allAdvisors = await get_all_advisors(AdvisorDBModel)
        if not allAdvisors:
            raise HTTPException(status_code=404)
        return allAdvisors