from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta
from models.position_model import Position
from models.player_face_model import PlayerFace
from sqlalchemy.ext.associationproxy import association_proxy

from models.player_position_model import (
    player_position_association,
)


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
        Position,
        uselist=False,
        back_populates="player",
        foreign_keys=[registered_position],
    )
    player_face_relationship = relationship(
        PlayerFace, back_populates="player", uselist=False
    )

    # Relación muchos a muchos con la tabla player_positions
    favoured_positions = relationship(
        Position,
        secondary=player_position_association,
        back_populates="players",
    )

    # Usar association_proxy para acceder a las posiciones favoritas directamente
    favoured_positions_names = association_proxy("favoured_positions", "position_name")
    favoured_positions_codes = association_proxy("favoured_positions", "position_code")

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "nationality": self.nationality.__str__(),
            "age": self.age.__str__(),
            "strong_foot": self.strong_foot.__str__(),
            "injury_tolerance": self.injury_tolerance.__str__(),
            "favoured_side": self.favoured_side.__str__(),
            "favoured_position": self.registered_position_relationship.normalize(),
            "positions": [
                f"{position.position_name} ({position.position_code})"
                for position in self.favoured_positions
            ],
            "skin_colour": self.player_face_relationship.skin_colour,
        }
