from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class PlayerStats(EntityMeta):
    __tablename__ = "player_stats"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    top_speed = Column(Integer, nullable=True)
    technique = Column(Integer, nullable=True)
    team_work = Column(Integer, nullable=True)
    stamina = Column(Integer, nullable=True)
    shot_technique = Column(Integer, nullable=True)
    shot_power = Column(Integer, nullable=True)
    shot_accuracy = Column(Integer, nullable=True)
    short_pass_speed = Column(Integer, nullable=True)
    short_pass_accuracy = Column(Integer, nullable=True)
    response = Column(Integer, nullable=True)
    mentality = Column(Integer, nullable=True)
    long_pass_speed = Column(Integer, nullable=True)
    long_pass_accuracy = Column(Integer, nullable=True)
    jump = Column(Integer, nullable=True)
    heading = Column(Integer, nullable=True)
    goal_keeping = Column(Integer, nullable=True)
    free_kick_accuracy = Column(Integer, nullable=True)
    dribble_speed = Column(Integer, nullable=True)
    dribble_accuracy = Column(Integer, nullable=True)
    defense = Column(Integer, nullable=True)
    curling = Column(Integer, nullable=True)
    balance = Column(Integer, nullable=True)
    attack = Column(Integer, nullable=True)
    agility = Column(Integer, nullable=True)
    aggression = Column(Integer, nullable=True)
    acceleration = Column(Integer, nullable=True)
    average_stats = Column(Integer, nullable=True)

    player = relationship("Player", back_populates="player_stats_relationship")
