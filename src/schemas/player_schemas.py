from pydantic import BaseModel, Field
from fastapi import Query
from typing import Optional, List


class GetPlayerRequestSchema(BaseModel):
    quantity: Optional[int] = Field(Query(1, description="Number of players to return"))
    id: Optional[int] = Field(Query(None, description="Player ID"))
    min_age: Optional[int] = Field(Query(None, description="Player minimum age"))
    max_age: Optional[int] = Field(Query(None, description="Player maximum age"))
    min_height: Optional[int] = Field(Query(None, description="Player minimum height"))
    max_height: Optional[int] = Field(Query(None, description="Player maximum height"))
    registered_position: Optional[str] = Field(
        Query(None, description="Player favoured position")
    )
    positions: List[str] = Field(Query([], description="Player positions"))
    name: Optional[str] = Field(Query(None, description="Player name"))
    nationality: Optional[str] = Field(Query(None, description="Player nationality"))
    strong_foot: Optional[str] = Field(Query(None, description="Player strong foot"))
    favoured_side: Optional[str] = Field(Query(None, description="Player favoured side"))
    skin_colour: Optional[int] = Field(Query(None, description="Player skin colour"))
