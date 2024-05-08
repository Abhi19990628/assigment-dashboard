import json
from django.core.management.base import BaseCommand
from dashboard.models import DataPoint
import os

class Command(BaseCommand):
    help = 'Load data from JSON file into database'

    def handle(self, *args, **kwargs):
        # Define the path to the JSON file
        json_file_path = os.path.join('data', 'datapoint_fixture.json')

        # Check if JSON file exists
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR('JSON file does not exist'))
            return

        # Open and load JSON file with latin-1 encoding
        with open(json_file_path, 'r', encoding='utf-32') as f:
            data = json.load(f)


        # Iterate through JSON data and save to database
        for idx, item in enumerate(data, start=1):
            try:
                data_point = DataPoint(**item)
                data_point.save()
            except Exception as e:
                # Handle any exceptions
                self.stdout.write(self.style.ERROR(f'Error saving data at index {idx}: {e}'))
                self.stdout.write(self.style.ERROR(f'Failing row contains {item}'))

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
