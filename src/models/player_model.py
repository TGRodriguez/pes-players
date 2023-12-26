from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta
from models.position_model import Position

# from models.player_position_model import (
#     player_position_association,
# )


class Player(EntityMeta):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)
    shirt_name = Column(Text, nullable=True)
    callname_id = Column(Integer, nullable=True)
    nationality = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    strong_foot = Column(Text, nullable=True)
    injury_tolerance = Column(Text, nullable=True)
    favoured_side = Column(Text, nullable=True)
    registered_position = Column(Integer, ForeignKey("positions.id"))
    registered_position_relationship = relationship(
        Position, foreign_keys=[registered_position]
    )

    # PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "position": self.registered_position_relationship,
        }
