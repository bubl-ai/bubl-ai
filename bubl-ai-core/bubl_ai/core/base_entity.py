import uuid
from datetime import datetime


class BaseEntity:
    """Base class for all entities"""

    def __init__(self, entity_id=None):
        self.id = entity_id or str(uuid.uuid4())
        self.created_at = datetime.now()

    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "type": self.__class__.__name__,
        }

    def __str__(self):
        return f"{self.__class__.__name__}({self.id})"
