import csv

from schedule_item import ScheduleItem

class Schedule:
    def __init__(self, filename):
        self.dictionary = {}

    def add_entry(self, item: ScheduleItem):
        key = item.get_key()
        self.dictionary[key] = item

    def print_header(self):
        print(
            f"{'Subject':<9}"
            f"{'Catalog':<9}"
            f"{'Section':<9}"
            f"{'Component':<12}"
            f"{'Session':<9}"
            f"{'Units':>7}"
            f"{'TotEnrl':>9}"
            f"{'CapEnrl':>9}"
            f"{'Instructor':<20}"
        )

    def print(self):
        self.print_header()
        for item in self.dictionary.values():
            item.print()

    def find_by_subject(self, subject):
        subject = subject.upper()
        return [item for item in self.dictionary.values() if item.Subject == subject]

    def find_by_subject_catalog(self, subject, catalog):
        subject = subject.upper()
        catalog = catalog.upper()
        return [item for item in self.dictionary.values() if item.Subject == subject and item.Catalog == catalog]

    def find_by_instructor_last_name(self, last_name):
        last_name = last_name.upper()
        return [item for item in self.dictionary.values() if item.Instructor.split(",")[0].upper() == last_name]

