patients = []

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    illness = input("Enter patient illness: ")
    patient = {"name": name, "age": age, "illness": illness}
    patients.append(patient)
    print(f"Patient {name} added successfully.")

def display_patients():
    if not patients:
        print("No patients found.")
    else:
        print("Patient details:")
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient():
    name = input("Enter patient name to search: ")
    for patient in patients:
        if patient["name"].lower() == name.lower():
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print(f"Patient {name} not found.")

def remove_patient():
    name = input("Enter patient name to remove: ")
    for i, patient in enumerate(patients):
        if patient["name"].lower() == name.lower():
            removed_patient = patients.pop(i)
            print(f"Patient {removed_patient['name']} removed successfully.")
            return
    print(f"Patient {name} not found.")

while True:
    print("\nHospital Patient Management System")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Remove Patient")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        remove_patient()
    elif choice == "5":
        print("Exiting Hospital Patient Management System...")
        break
    else:
        print("Invalid choice. Please try again.")