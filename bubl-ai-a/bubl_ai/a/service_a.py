from bubl_ai_core import CoreService


class ServiceA:
    """Service A using core functionality"""

    def __init__(self):
        self.core = CoreService()
        self.name = "ServiceA"

    def process_list(self, items):
        """Process a list using core service"""

        def add_index(data):
            return [{"index": i, "item": item} for i, item in enumerate(data)]

        return self.core.process(items, add_index)

    def get_info(self):
        """Get service info including core"""
        return {
            "service": self.name,
            "depends_on": ["core"],
            "core_info": self.core.get_info(),
        }
