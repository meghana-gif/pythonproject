from abc import ABC, abstractmethod
class ItemReport(ABC):
    def __init__(self, item_name, description, location, date, owner_name):
        self.__item_name = item_name
        self.__description = description
        self.__location = location
        self.__date = date
        self.__owner_name = owner_name
        self.__status = "Active"
    # Encapsulation - Getter methods
    def get_item_name(self):
        return self.__item_name
    def get_description(self):
        return self.__description
    def get_location(self):
        return self.__location
    def get_date(self):
        return self.__date
    def get_owner_name(self):
        return self.__owner_name
    def get_status(self):
        return self.__status
    # Encapsulation - Setter method
    def set_status(self, status):
        self.__status = status
    # Abstract method
    @abstractmethod
    def display_details(self):
        pass
class LostItem(ItemReport):
    def display_details(self):
        print("\n========== LOST ITEM ==========")
        print("Item Name   :", self.get_item_name())
        print("Description :", self.get_description())
        print("Location    :", self.get_location())
        print("Date        :", self.get_date())
        print("Owner       :", self.get_owner_name())
        print("Status      :", self.get_status())
class FoundItem(ItemReport):
    def display_details(self):
        print("\n========== FOUND ITEM ==========")
        print("Item Name   :", self.get_item_name())
        print("Description :", self.get_description())
        print("Location    :", self.get_location())
        print("Date        :", self.get_date())
        print("Finder     :", self.get_owner_name())
        print("Status      :", self.get_status())
class LostLink:
    def __init__(self):
        self.__reports = []
    # Add a report
    def add_report(self, report):
        self.__reports.append(report)
        print("\nReport added successfully!")
    # Display all reports
    def display_all_reports(self):
        if len(self.__reports) == 0:
            print("\nNo reports available.")
            return
        print("\n========== ALL REPORTS ==========")
        for report in self.__reports:
            report.display_details()
    # Search item
    def search_item(self, item_name):
        found = False
        for report in self.__reports:
            if report.get_item_name().lower() == item_name.lower():
                report.display_details()
                found = True
        if found == False:
            print("\nItem not found.")
    # Mark item as returned
    def mark_as_returned(self, item_name):
        found = False
        for report in self.__reports:
            if report.get_item_name().lower() == item_name.lower():
                report.set_status("Returned")
                print("\nItem marked as returned successfully.")
                found = True
        if found == False:
            print("\nItem not found.")
    # Match lost and found items
    def match_items(self):
        lost_items = []
        found_items = []
        for report in self.__reports:
            if isinstance(report, LostItem):
                lost_items.append(report)
            elif isinstance(report, FoundItem):
                found_items.append(report)
        print("\n========== POSSIBLE MATCHES ==========")
        match_found = False
        for lost in lost_items:
            for found in found_items:
                if (
                    lost.get_item_name().lower()
                    == found.get_item_name().lower()
                    and
                    lost.get_location().lower()
                    == found.get_location().lower()
                ):
                    print("\nPossible Match Found!")
                    print("Lost Item :", lost.get_item_name())
                    print("Found Item:", found.get_item_name())
                    print("Location  :", lost.get_location())
                    match_found = True
        if match_found == False:
            print("\nNo matching items found.")
# MAIN PROGRAM
lostlink = LostLink()
while True:
    print("\n")
    print("====================================")
    print("       LOSTLINK CAMPUS SYSTEM")
    print("====================================")
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. View All Reports")
    print("4. Search Item")
    print("5. Find Possible Matches")
    print("6. Mark Item as Returned")
    print("7. Exit")
    print("====================================")
    choice = input("Enter your choice: ")
    # Report Lost Item
    if choice == "1":
        print("\n----- REPORT LOST ITEM -----")
        item_name = input("Enter item name: ")
        description = input("Enter description: ")
        location = input("Enter lost location: ")
        date = input("Enter date: ")
        owner_name = input("Enter owner name: ")
        lost_item = LostItem(
            item_name,
            description,
            location,
            date,
            owner_name
        )
        lostlink.add_report(lost_item)
    # Report Found Item
    elif choice == "2":
        print("\n----- REPORT FOUND ITEM -----")
        item_name = input("Enter item name: ")
        description = input("Enter description: ")
        location = input("Enter found location: ")
        date = input("Enter date: ")
        finder_name = input("Enter finder name: ")
        found_item = FoundItem(
            item_name,
            description,
            location,
            date,
            finder_name
        )
        lostlink.add_report(found_item)
    # View all reports
    elif choice == "3":
        lostlink.display_all_reports()
    # Search item
    elif choice == "4":
        item_name = input("Enter item name to search: ")
        lostlink.search_item(item_name)
    # Match items
    elif choice == "5":
        lostlink.match_items()
    # Mark returned
    elif choice == "6":
        item_name = input("Enter returned item name: ")
        lostlink.mark_as_returned(item_name)
    # Exit
    elif choice == "7":
        print("\nThank you for using LostLink!")
        break
    else:
        print("\nInvalid choice. Please try again.")