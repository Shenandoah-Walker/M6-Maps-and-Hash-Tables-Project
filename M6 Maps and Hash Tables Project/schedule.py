import csv

from schedule_item import ScheduleItem

class Schedule:
    def __init__(self, filename):
        self.dictionary = {}

    def add_entry(self, item: ScheduleItem):
        key = item.get_key()
        self.dictionary[key] = item

    def print_header(self):