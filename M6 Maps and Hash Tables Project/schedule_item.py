from dataclasses import dataclass

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

    def get_key(self):
        return f"{self.Subject}_{self.Catalog}_{self.Section}"

    def print(self):
        print(
            f"{self.Subject:<9}"
            f"{self.Catalog:<9}"
            f"{self.Section:<9}"
            f"{self.Component:<12}"
            f"{self.Session:<9}"
            f"{self.Units:>7}"
            f"{self.TotEnrl:>9}"
            f"{self.CapEnrl:>9}"
            f"{self.Instructor:<20}"
        )