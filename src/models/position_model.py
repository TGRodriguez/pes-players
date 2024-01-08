from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from models.base_model import EntityMeta
from sqlalchemy.orm import relationship


class Position(EntityMeta):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    position_name = Column(Text, nullable=True)
    position_code = Column(Text, nullable=True)

    player = relationship("Player", back_populates="registered_position_relationship")

    players = relationship(
        "Player",
        secondary="player_positions",
        back_populates="favoured_positions",
    )

    def normalize(self):
        return {f"{self.position_name} ({self.position_code})"}
