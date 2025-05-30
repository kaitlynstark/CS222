def studentInfo():
    try:
        studentList = {}
        fileInput = open("studentsInfo.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
        
        for s in students:
            parts = s.strip().split(',')
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]

        while True:
            print("\nChoose an option:")
            print("1) Search by Last Name")
            print("2) Search by Major")
            print("3) Quit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                lastName = input("Enter last name to search for: ")
                found = False
                fileOutput = open("output.txt", 'a')
                for id, info in studentList.items():
                    if info[0].lower() == lastName.lower():
                        result = f"{id}, {info[0]}, {info[1]}, {info[2]}, {info[3]}"
                        print(result)
                        fileOutput.write("Search by Last Name: " + result + "\n")
                        found = True
                if not found:
                    print("No students found with that last name.")
                    fileOutput.write("Search by Last Name: No results found for " + lastName + "\n")
                fileOutput.close()
            
            elif choice == '2':
                major = input("Enter major to search for: ")
                found = False
                fileOutput = open("output.txt", 'a')
                for id, info in studentList.items():
                    if info[2].lower() == major.lower():
                        result = f"{id}, {info[0]}, {info[1]}, {info[2]}, {info[3]}"
                        print(result)
                        fileOutput.write("Search by Major: " + result + "\n")
                        found = True
                if not found:
                    print("No students found with that major.")
                    fileOutput.write("Search by Major: No results found for " + major + "\n")
                fileOutput.close()

            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    except FileNotFoundError:
        print("File not found")

studentInfo()