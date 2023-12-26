from sqlalchemy import Column, ForeignKey, Table

from models.base_model import EntityMeta


player_position_association = Table(
    "player_positions",
    EntityMeta.metadata,
    Column("player_id", ForeignKey("players.id")),
    Column("position_id", ForeignKey("positions.id")),
)
