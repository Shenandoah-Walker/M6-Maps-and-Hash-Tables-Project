from dataclasses import dataclass

#Class: ScheduleItem
#Purpose: Represents a single course offering with its details.
@dataclass
class ScheduleItem:
    Subject: str
    Catalog: str
    Section: str
    Component: str
    Session: str
    Units: int
    TotEnrl : int
    CapEnrl: int
    Instructor: str

    #Method: get_key
    #Purpose: Generates a unique key for the course offering based on its subject, catalog number, and section.
    #Parameters: None
    #Returns: A string key in the format "Subject_Catalog_Section".
    #Preconditions: The Subject, Catalog, and Section attributes must be properly initialized.
    #Postconditions: Returns a string that can be used as a unique identifier for the course offering.
    def get_key(self):
        return f"{self.Subject}_{self.Catalog}_{self.Section}"
    
    #Method: print
    #Purpose: Prints the details of the course offering in a formatted manner.
    #Parameters: None
    #Returns: None
    #Preconditions: All attributes must be properly initialized.
    #Postconditions: The course offering details are printed to the console.
    def print(self):
        print(
            f"{self.Subject:<9}"
            f"{self.Catalog:<9}"
            f"{self.Section:<9}"
            f"{self.Component:<12}"
            f"{self.Session:<9}"
            f"{self.Units:^7}"
            f"{self.TotEnrl:^9}"
            f"{self.CapEnrl:^9}"
            f"{self.Instructor:<30}"
        )