from bubl_ai_core import BaseEntity
from bubl_ai_b import EntityB


class EntityC(BaseEntity):
    """Entity C that can work with EntityB"""

    def __init__(self, name, related_entities=None, entity_id=None):
        super().__init__(entity_id)
        self.name = name
        self.related_entities = related_entities or []  # List of EntityB

    def to_dict(self):
        """Convert to dictionary with C-specific fields"""
        base_dict = super().to_dict()
        base_dict.update(
            {
                "name": self.name,
                "related_count": len(self.related_entities),
                "related_entities": [
                    entity.to_dict() for entity in self.related_entities
                ],
                "processed_by": "service_c",
            }
        )
        return base_dict

    def add_related(self, entity_b):
        """Add a related EntityB"""
        if isinstance(entity_b, EntityB):
            self.related_entities.append(entity_b)

    def get_all_tags(self):
        """Get all tags from related EntityB instances"""
        all_tags = []
        for entity in self.related_entities:
            all_tags.extend(entity.tags)
        return list(set(all_tags))  # Remove duplicates
