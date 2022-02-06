import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline=' ') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Roll No.", "Contact number" "Email ID"])
            
        writer.writerow(info.list)
        
if name == 'main':
    condition = True
    student_num = 1
    
    while(condition):
        student_info = input("Enter student information for student #{} in the format (Name Age Roll No. Contact number Email ID):")
        
        student_info_list = student_info.split("")
        
        print("\nThe entered information is -\nName: {}\nAge: {}\nRoll No.: {}\nContact number {}\nEmail ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2],student_info_list[3], student_info_list[4]))
              
        choice_check = input("Is the enetered information correct? (yes/no)")
        
        if choice_check == "yes":
            write_into_csv(student_info_list)
            
            condition_check = input("Enter (yes/no) if you want to enter information for another student:")
            if condition == "yes":
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease enter the correct information")
