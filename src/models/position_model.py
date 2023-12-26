from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    Text,
)

from models.base_model import EntityMeta


class Position(EntityMeta):
    __tablename__ = "positions"

    id = Column(Integer)
    position_name = Column(Text, nullable=True)
    position_code = Column(Text, nullable=True)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.position_name.__str__(),
            "code": self.position_code.__str__(),
        }
