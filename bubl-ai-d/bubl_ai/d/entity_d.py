import uuid
from datetime import datetime


class EntityD:
    """Independent Entity D - no inheritance"""

    def __init__(self, data, category="default", entity_id=None):
        self.id = entity_id or str(uuid.uuid4())
        self.data = data
        self.category = category
        self.created_at = datetime.now()
        self.independent = True

    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "data": self.data,
            "category": self.category,
            "created_at": self.created_at.isoformat(),
            "type": "EntityD",
            "independent": self.independent,
        }

    def update_data(self, new_data):
        """Update the data"""
        self.data = new_data

    def update_category(self, new_category):
        """Update the category"""
        self.category = new_category

    def __str__(self):
        return f"EntityD({self.id}, {self.category})"
