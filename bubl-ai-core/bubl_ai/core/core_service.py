class CoreService:
    """Core service with basic functionality"""

    def __init__(self):
        self.name = "CoreService"

    def validate(self, data):
        """Validate input data"""
        return data is not None

    def process(self, data, processor_func):
        """Process data with a function"""
        if not self.validate(data):
            raise ValueError("Invalid data")
        return processor_func(data)

    def get_info(self):
        """Get service information"""
        return {"service": self.name, "version": "1.0.0"}
