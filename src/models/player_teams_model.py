from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class PlayerTeams(EntityMeta):
    __tablename__ = "player_teams"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    national_team = Column(Text, nullable=True)
    club_team = Column(Text, nullable=True)

    player = relationship("Player", back_populates="player_teams_relationship")
