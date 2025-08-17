from bubl_ai_core import BaseEntity


class EntityB(BaseEntity):
    """Entity B extending base entity"""

    def __init__(self, title, tags=None, entity_id=None):
        super().__init__(entity_id)
        self.title = title
        self.tags = tags or []

    def to_dict(self):
        """Convert to dictionary with B-specific fields"""
        base_dict = super().to_dict()
        base_dict.update(
            {
                "title": self.title,
                "tags": self.tags,
                "tag_count": len(self.tags),
                "processed_by": "service_b",
            }
        )
        return base_dict

    def add_tag(self, tag):
        """Add a tag"""
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        """Remove a tag"""
        if tag in self.tags:
            self.tags.remove(tag)
