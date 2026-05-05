import csv

from schedule_item import ScheduleItem

#Class: Schedule
#Purpose: Manages a collection of ScheduleItem objects, allowing for loading from a CSV file, adding entries, and searching based on various criteria.
class Schedule:
    #Method: __init__
    #Purpose: Initializes the Schedule object by loading data from a specified CSV file.
    #Parameters: - str filename: The name of the CSV file containing the course schedule data.
    #Returns: None
    #Preconditions: The CSV file must exist and be properly formatted.
    #Postconditions: The Schedule object is initialized with data from the CSV file.
    def __init__(self, filename):
        self.dictionary = {}
        self.load_data(filename)

    #Method: add_entry
    #Purpose: Adds a ScheduleItem to the Schedule's internal dictionary.
    #Parameters: - ScheduleItem item: The ScheduleItem object to be added to the schedule.
    #Returns: None
    #Preconditions: The ScheduleItem must be properly initialized.
    #Postconditions: The ScheduleItem is added to the schedule's internal dictionary, using its unique key.
    def add_entry(self, item: ScheduleItem):
        key = item.get_key()
        self.dictionary[key] = item

    #Method: print_header
    #Purpose: Prints the header for the schedule display, showing the column names for the course details.
    #Parameters: None
    #Returns: None
    #Preconditions: None
    #Postconditions: The header for the schedule display is printed to the console.
    def print_header(self):
        print(
            f"{'Subject':<9}"
            f"{'Catalog':<9}"
            f"{'Section':<9}"
            f"{'Component':<12}"
            f"{'Session':<9}"
            f"{'Units':^7}"
            f"{'TotEnrl':^9}"
            f"{'CapEnrl':^9}"
            f"{'Instructor':<30}"
        )

    #Method: print
    #Purpose: Prints the full schedule of courses, including the header and details of each course offering.
    #Parameters: None
    #Returns: None
    #Preconditions: The schedule must have been initialized with course data.
    #Postconditions: The full schedule of courses is printed to the console.
    def print(self):
        self.print_header()
        for item in self.dictionary.values():
            item.print()

    #Method: find_by_subject
    #Purpose: Searches for courses in the schedule based on the subject code.
    #Parameters: - str subject: The subject code to search for.
    #Returns: A list of ScheduleItem objects that match the specified subject code.
    #Preconditions: The schedule must have been initialized with course data.
    #Postconditions: A list of ScheduleItem objects matching the subject code is returned.
    def find_by_subject(self, subject):
        subject = subject.upper()
        return [item for item in self.dictionary.values() if item.Subject == subject]

    #Method: find_by_subject_catalog
    #Purpose: Searches for courses in the schedule based on both the subject code and catalog number.
    #Parameters: - str subject: The subject code to search for.
    #            - str catalog: The catalog number to search for.
    #Returns: A list of ScheduleItem objects that match the specified subject code and catalog number.
    #Preconditions: The schedule must have been initialized with course data.
    #Postconditions: A list of ScheduleItem objects matching the subject code and catalog number is returned.
    def find_by_subject_catalog(self, subject, catalog):
        subject = subject.upper()
        catalog = catalog.upper()
        return [item for item in self.dictionary.values() if item.Subject == subject and item.Catalog == catalog]

    #Method: find_by_instructor_last_name
    #Purpose: Searches for courses in the schedule based on the instructor's last name.
    #Parameters: - str last_name: The last name of the instructor to search for.
    #Returns: A list of ScheduleItem objects that match the specified instructor's last name.
    #Preconditions: The schedule must have been initialized with course data, and the Instructor field in ScheduleItem must be properly formatted (e.g., "LastName, FirstName").
    #Postconditions: A list of ScheduleItem objects matching the instructor's last name is returned.
    def find_by_instructor_last_name(self, last_name):
        last_name = last_name.upper()
        return [item for item in self.dictionary.values() if item.Instructor.split(",")[0].upper() == last_name]

    #Method: load_data
    #Purpose: Loads course schedule data from a specified CSV file and populates the schedule's internal dictionary with ScheduleItem objects.
    #Parameters: - str filename: The name of the CSV file containing the course schedule data.
    #Returns: None
    #Preconditions: The CSV file must exist and be properly formatted, with columns corresponding to the attributes of ScheduleItem.
    #Postconditions: The schedule's internal dictionary is populated with ScheduleItem objects created from the data in the CSV file.
    def load_data(self, filename):
        with open(filename, encoding="utf-8-sig", newline="") as csvfile:
            entries = csv.DictReader(csvfile)

            for entry in entries:
                item = ScheduleItem(
                    Subject=entry["Subject"],
                    Catalog=entry["Catalog"],
                    Section=entry["Section"],
                    Component=entry["Component"],
                    Session=entry["Session"],
                    Units=int(entry["Units"]),
                    TotEnrl=int(entry["TotEnrl"]),
                    CapEnrl=int(entry["CapEnrl"]),
                    Instructor=entry["Instructor"]
                )
                self.add_entry(item)


