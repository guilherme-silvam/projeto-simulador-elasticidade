import json
from .elasticity import DemandModel

class ScenarioManager:
    def __init__(self, data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_scenarios(self):
        return list(self.data.keys())

    def get_segments(self, scenario):
        return list(self.data[scenario]['segments'].keys())

    def get_scenario_info(self, scenario):
        return self.data[scenario]['info']

    def get_segment_info(self, scenario, segment):
        return self.data[scenario]['segments'][segment]['info']

    def get_price_range(self, scenario):
        return self.data[scenario]['price_range']

    def get_default_price(self, scenario):
        return self.data[scenario]['default_price']

    def get_model(self, scenario, segment):
        params = self.data[scenario]['segments'][segment]['params']
        return DemandModel(**params)

    def get_all_models(self, scenario):
        return {
            seg: self.get_model(scenario, seg)
            for seg in self.get_segments(scenario)
        }
