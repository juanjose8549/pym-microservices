import strawberry
from typing import Optional, List

from .database.db_models import Advisor as AdvisorDBModel
from .models.graphql_types import Advisor as AdvisorModel
from .resolvers.query_resolvers import get_all_advisors

from fastapi import HTTPException


@strawberry.type
class Query:
    @strawberry.field
    async def allAdvisors() -> Optional[List[AdvisorModel]]:
        allAdvisors = await get_all_advisors(AdvisorDBModel)
        if not allAdvisors:
            raise HTTPException(status_code=404)
        return allAdvisors