from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class PlayerBody(EntityMeta):
    __tablename__ = "player_body"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    weight = Column(Integer, nullable=True)
    waist_circumference = Column(Integer, nullable=True)
    waist_circumference = Column(Integer, nullable=True)
    shoulder_width = Column(Integer, nullable=True)
    shoulder_height = Column(Integer, nullable=True)
    neck_width = Column(Integer, nullable=True)
    neck_length = Column(Integer, nullable=True)
    leg_length = Column(Integer, nullable=True)
    leg_circumference = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    chest_measurement = Column(Integer, nullable=True)
    calf_circumference = Column(Integer, nullable=True)
    body_type = Column(Integer, nullable=True)
    arm_circumference = Column(Integer, nullable=True)

    player = relationship("Player", back_populates="player_body_relationship")
