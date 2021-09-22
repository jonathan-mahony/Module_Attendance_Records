#Author: Jonathan Mahony
#Attendance Project
print("Module Record System")
print("---------------------")
def login():
    supplied_username = input("Username:")
    supplied_password = input("Password:")
    with open('Login_details.txt', 'r') as login_file:
        for line in login_file:
            username, password = line.split(',')
            if username == supplied_username and password == supplied_password:
                print("       ")
                print(f"Welcome {supplied_username}")

            else:
                print("Wrong Details")
                login()
def options():
    print("Module  Record System: Options")
    print("-------------------------------")
    option_1 = print("1) Record Attendance- ")
    option_2 = print("2) Generate stats- ")
    option_3 = print("3) Exit-")
    option_choice = input(">")
    if option_choice == '1':
        print(attendance())
    elif option_choice == '2':
        print(stats())
    elif option_choice == '3':
        exit()
    else:
        print("Invalid Choice")



def attendance():
    print("Module Record System(Attendance) - Choose a Module")
    module_file = open('modules.txt','r')
    print("1)", module_file.readline())
    print("2)", module_file.readline())
    module_choice = input(">>")

    if module_choice == '1':
        print("Module Record System(Attendance) SOFT_6017 ")
        print("------------------------------------------")
        print("There are 3 students enrolled.")
        big_list = []
        with open("SOFT_6017.txt", "r") as f:
            x = 0
            students = len(open('SOFT_6017.txt').readlines())
            while students > x:
                for line in f.readlines():
                    new_line = line.strip().split(",")
                    for i in range(1,4):
                        new_line[i] = int(new_line[i])

                    print("Student=",new_line[0])
                    print("1) Present")
                    print("2)Absent")
                    print("3)Excused")
                    lecture_input = int(input(">"))
                    x += 1
                    f.readlines()
                    new_line[lecture_input] += 1
                    big_list.append(new_line)

        with open("SOFT_6017.txt", 'w') as of:
            for item in big_list:
                of.write(str(item).replace("[", "").replace("]", "") + "\n")
        options()

    elif module_choice == '2':
        print("Module Record System(Attendance) SOFT_6018 ")
        print("------------------------------------------")
        print("There are 2 students enrolled.")
        big_list = []
        with open("SOFT_6018.txt", "r") as f:
            x = 0
            students = len(open('SOFT_6018.txt').readlines())
            while students > x:
                for line in f.readlines():
                    new_line = line.strip().split(",")
                    for i in range(1,3):
                        new_line[i] = int(new_line[i])

                    print("Student=",new_line[0])
                    print("1) Present")
                    print("2)Absent")
                    print("3)Excused")
                    lecture_input = int(input(">"))
                    x += 1
                    f.readlines()
                    new_line[lecture_input] += 1
                    big_list.append(new_line)

        with open("SOFT_6018.txt", 'w') as of:
            for item in big_list:
                of.write(str(item).replace("[", "").replace("]", "") + "\n")
        options()
    else:
        print("Error In module Choice")
        attendance()



def stats():
    print("Module Record System(Statistics) - Choose a Module ")
    module_file = open('modules.txt', 'r')
    print("1)", module_file.readline())
    print("2)", module_file.readline())
    module_choice = input(">>")
    if module_choice == '1':
        print("Module = SOFT_6017 Modular Programming")
        file = open("SOFT_6017.txt", "r")
        count = 0
        students = file.read()
        CoList = students.split("\n")
        for i in CoList:
            if i:
                count += 1
        print("Number of students:", count)
        f = open('SOFT_6017.txt', 'r')
        content = f.read()
        f.close()
        wordList = content.split(',')
        total = 0
        for item in wordList:
            if item.isnumeric():
                total += int(item)
        print("Number of classes:", int(total/3))

        number_list = []
        with open("SOFT_6017.txt", 'r') as f:
            for line in f:
                number_list.append(line.split(",")[1])
                number_list = [int(i) for i in number_list]
                total = sum(number_list)/3
            print("Average Attendance:", (total))
            attendance_list = []
            f = open('SOFT_6017.txt', 'r')
            for line in f:
                attendance_list.append(line.strip().split(","))
            print("Lowest Attender(s):", min(attendance_list)[0])
            print("Best Attender(s):", max(attendance_list)[0])
            print("Non Attenders:", attendance_list[1][0])
            options()


    elif module_choice == '2':
        print("Module = SOFT_6018 Programming Fundamentals")
        file = open("SOFT_6018.txt", "r")
        count = 0
        students = file.read()
        CoList = students.split("\n")
        for i in CoList:
            if i:
                count += 1
        print("Number of students:", count)
        f = open('SOFT_6018.txt', 'r')
        content = f.read()
        f.close()
        wordList = content.split(',')
        total = 0
        for item in wordList:
            if item.isnumeric():
                total += int(item)
        print("Number of classes:", int(total / 2))

        number_list = []
        with open("SOFT_6018.txt", 'r') as f:
            for line in f:
                number_list.append(line.split(",")[1])
                number_list = [int(i) for i in number_list]
                total = sum(number_list) / 2
            print("Average Attendance:", (total))
            attendance_list = []
            f = open('SOFT_6018.txt', 'r')
            for line in f:
                attendance_list.append(line.strip().split(","))
            print("Lowest Attender(s):", min(attendance_list)[0])
            print("Best Attender(s):", max(attendance_list)[0])
            print(attendance_list)
            print("Non Attenders:",)
            options()
    else:
        print("Error")
    



def main():
    login()
    options()

main()