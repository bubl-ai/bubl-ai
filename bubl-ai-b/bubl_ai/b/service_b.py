from bubl_ai_core import CoreService


class ServiceB:
    """Service B using core functionality"""

    def __init__(self):
        self.core = CoreService()
        self.name = "ServiceB"

    def analyze_data(self, data):
        """Analyze data using core service"""

        def analyzer(input_data):
            return {
                "original": input_data,
                "analysis": {
                    "type": type(input_data).__name__,
                    "length": len(str(input_data)),
                    "analyzed_by": "service_b",
                },
            }

        return self.core.process(data, analyzer)

    def batch_process(self, items):
        """Process multiple items"""
        results = []
        for item in items:
            try:
                result = self.analyze_data(item)
                results.append(result)
            except Exception as e:
                results.append({"error": str(e), "item": item})
        return results

    def get_info(self):
        """Get service info"""
        return {
            "service": self.name,
            "depends_on": ["core"],
            "core_info": self.core.get_info(),
        }
