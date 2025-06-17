from card_agent.constant import DATA_PATH
import json

class load_card_data:
    def __init__(self, data_path=DATA_PATH):
        self.data_path = data_path

    def load_data(self):
        """Load card data from the specified JSON file."""
        with open(self.data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data