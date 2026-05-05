#Test program for M6 Maps and Hash Tables Project

from schedule import Schedule

schedule = Schedule("courses.csv")

print("This program contains the VPCC STEM 2022 Summer Schedule of Classes.")
print()

while True:
    print("Menu:")
    print("Please select from the options below. Enter the number of your choice.")
    print("1. Display all (print the full course schedule)")
    print("2. Search by subject")
    print("3. Search by subject/catalog")
    print("4. Search by instructor last name")
    print("5. Quit")

    print()
    choice = input("Please enter your choice: ")

    if (choice == "1"):
        schedule.print()

    elif (choice == "2"):
        subject = input("Please enter the subject to search for (it should be in the following format: BIO): ")
        results = schedule.find_by_subject(subject)

        if not results:
            print("There are no courses with that subject.")

        else:
            schedule.print_header()
            for item in results:
                item.print()
            print()

    elif (choice == "3"):
        subject = input("Please enter the subject to search for (it should be in the following format: BIO): ")
        catalog = input("Please enter the catalog number to search for (it should be in the following format: 101): ")
        results = schedule.find_by_subject_catalog(subject, catalog)
        if not results:
            print("There are no courses with that subject and catalog number.\n")
        else:
            schedule.print_header()
            for item in results:
                item.print()
            print()


    elif (choice == "4"):
        last_name = input("Please enter the instructor's last name to search for (it should be in the following format: Smith): ")
        results = schedule.find_by_instructor_last_name(last_name)

        if not results:
            print("There are no courses with that instructor.")
        else:
            schedule.print_header()
            for item in results:
                item.print()
            print()

    elif (choice == "5"):
        print("End of program.")
        break

    else:
        print("Invalid choice. Choice must be a number between 1 and 5, inclusive.")
