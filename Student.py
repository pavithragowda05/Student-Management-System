class Student:

    def AddStudent(self):
        file = open(r"C:\projects\Student-Management-System\Studentdata.txt", "a")

        usn = input("USN: ")
        name = input("Name: ")
        year = input("Academic Year: ")
        cgpa = input("CGPA: ")

        file.write(usn + "," + name + "," + year + "," + cgpa + "\n")

        print("Record added successfully.")
        file.close()

    def updateStudent(self):
        file = open(r"C:\projects\Student-Management-System\Studentdata.txt", "r")

        record = input("Enter USN you want to update: ")

        data = file.readlines()
        file.close()

        newlist = []

        for line in data:
            row = line.strip().split(",")
            newlist.append(row)

        found = False

        for row in newlist:
            if row[0] == record:
                row[3] = input("Enter new CGPA: ")
                found = True
                print("Updated successfully.")
                break

        if not found:
            print("Student not found.")

        file = open(r"C:\projects\Student-Management-System\Studentdata.txt", "w")

        for row in newlist:
            file.write(",".join(row) + "\n")

        file.close()

    def DisplayData(self):
        file = open(r"C:\projects\Student-Management-System\Studentdata.txt", "r")

        data = file.readlines()

        print("\nStudent Records")
        print("-" * 40)

        for line in data:
            row = line.strip().split(",")
            print(f"USN : {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Year: {row[2]}")
            print(f"CGPA: {row[3]}")
            print("-" * 40)

        file.close()


print("===== Student Management System =====")
print("1. Add Student")
print("2. Update Student")
print("3. Display Students")

choice = int(input("Enter your choice: "))

obj = Student()

match choice:
    case 1:
        obj.AddStudent()
    case 2:
        obj.updateStudent()
    case 3:
        obj.DisplayData()
    case _:
        print("Invalid Choice")