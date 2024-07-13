from typing import Optional

import strawberry
from strawberry.schema_directive import Location

from .query import Query
from .mutation import Mutation


@strawberry.schema_directive(locations=[Location.SCHEMA])
class Contact:
    name: str = strawberry.field(description="Contact title of the subgraph owner")
    url: Optional[str] = strawberry.field(
        description="URL where the subgraph's owner can be reached"
    )
    description: Optional[str] = strawberry.field(
        description="Other relevant notes can be included here; supports markdown links"
    )



schema = strawberry.federation.Schema(
    Query,
    Mutation,
    enable_federation_2=True,
    schema_directives=[
        Contact(
            name="Server Team",
            url="https://myteam.slack.com/archives/teams-chat-room-url",
            description=(
                "send urgent issues to [#oncall]"
                "(https://yourteam.slack.com/archives/oncall)."
            ),
        )
    ],
)
