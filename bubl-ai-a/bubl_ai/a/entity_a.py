from bubl_ai_core import BaseEntity


class EntityA(BaseEntity):
    """Entity A extending base entity"""

    def __init__(self, name, value, entity_id=None):
        super().__init__(entity_id)
        self.name = name
        self.value = value

    def to_dict(self):
        """Convert to dictionary with A-specific fields"""
        base_dict = super().to_dict()
        base_dict.update(
            {
                "name": self.name,
                "value": self.value,
                "processed_by": "service_a",
            }
        )
        return base_dict

    def update_value(self, new_value):
        """Update the value"""
        self.value = new_value
