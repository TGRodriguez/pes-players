from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class PlayerFace(EntityMeta):
    __tablename__ = "player_face"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    skin_colour = Column(Integer, nullable=True)
    nose_width = Column(Integer, nullable=True)
    nose_type = Column(Integer, nullable=True)
    nose_height = Column(Integer, nullable=True)
    mouth_type = Column(Integer, nullable=True)
    mouth_size = Column(Integer, nullable=True)
    mouth_position = Column(Integer, nullable=True)
    jaw_width = Column(Integer, nullable=True)
    jaw_type = Column(Integer, nullable=True)
    jaw_chin = Column(Integer, nullable=True)
    head_width = Column(Integer, nullable=True)
    head_overall_position = Column(Integer, nullable=True)
    head_height = Column(Integer, nullable=True)
    hair_volume = Column(Integer, nullable=True)
    hair_type = Column(Text, nullable=True)
    hair_shape = Column(Integer, nullable=True)
    hair_front = Column(Integer, nullable=True)
    hair_darkness = Column(Integer, nullable=True)
    hair_colour_rgb_r = Column(Integer, nullable=True)
    hair_colour_rgb_g = Column(Integer, nullable=True)
    hair_colour_rgb_b = Column(Integer, nullable=True)
    hair_colour_config = Column(Integer, nullable=True)
    hair = Column(Integer, nullable=True)
    facial_hair_type = Column(Integer, nullable=True)
    facial_hair_colour = Column(Integer, nullable=True)
    face_type = Column(Text, nullable=True)
    face_id = Column(Integer, nullable=True)
    eyes_width = Column(Integer, nullable=True)
    eyes_type = Column(Integer, nullable=True)
    eyes_position = Column(Integer, nullable=True)
    eyes_length = Column(Integer, nullable=True)
    eyes_colour_2 = Column(Text, nullable=True)
    eyes_colour_1 = Column(Integer, nullable=True)
    eyes_angle = Column(Integer, nullable=True)
    cheecks_type = Column(Integer, nullable=True)
    cheecks_shape = Column(Integer, nullable=True)
    brows_type = Column(Integer, nullable=True)
    brows_spacing = Column(Integer, nullable=True)
    brows_height = Column(Integer, nullable=True)
    brows_angle = Column(Integer, nullable=True)

    player = relationship("Player", back_populates="player_face_relationship")
