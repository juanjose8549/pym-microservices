import strawberry
from typing import Optional, List

from .database.db_models import Advisor as AdvisorDBModel
from .models.graphql_types import Advisor as AdvisorModel, AdvisorInput
from .resolvers.mutation_resolvers import insert_advisor

from fastapi import HTTPException

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_advisor(input: AdvisorInput) -> Optional[AdvisorModel]:
        new_advisor = AdvisorDBModel(
            name=input.name,
            expertise=input.expertise,
        )
        inserted_advisor = await insert_advisor(new_advisor)
        if not insert_advisor:
            raise HTTPException(status_code=404)
        return inserted_advisor