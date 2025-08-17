from bubl_ai_core import CoreService
from bubl_ai_b import ServiceB


class ServiceC:
    """Service C using both core and service B"""

    def __init__(self):
        self.core = CoreService()
        self.service_b = ServiceB()
        self.name = "ServiceC"

    def complex_process(self, data):
        """Complex processing using both core and service B"""
        # First analyze with service B
        analyzed = self.service_b.analyze_data(data)

        # Then enhance with service C logic
        def enhancer(input_data):
            return {
                "service_b_result": input_data,
                "service_c_enhancement": {
                    "enhanced": True,
                    "processing_chain": ["core", "service_b", "service_c"],
                },
            }

        return self.core.process(analyzed, enhancer)

    def orchestrate_batch(self, items):
        """Orchestrate batch processing using service B"""
        b_results = self.service_b.batch_process(items)

        enhanced_results = []
        for result in b_results:
            if "error" not in result:
                enhanced = self.complex_process(result)
                enhanced_results.append(enhanced)
            else:
                enhanced_results.append(result)

        return enhanced_results

    def get_info(self):
        """Get service info"""
        return {
            "service": self.name,
            "depends_on": ["core", "service_b"],
            "core_info": self.core.get_info(),
            "service_b_info": self.service_b.get_info(),
        }
