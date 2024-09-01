# STUDENT-MANAGEMENT-SYSTEM USING 'PYTHON' :

# PYTHON-MODULE'S :
import pandas
import sys

# DATA-STRUCTURE (LIST) :
student_name = []
student_age = []
student_class = []
student_roll_number = []
student_mobile_number = []
student_address = []
student_parent_name = []
student_parent_mobile_number = []
student_unique_id = []
student_past_qualification = []

# CLASS (STUDENT-MANAGEMENT-SYSTEM) :
class student_management_system:
    """
    /* >>> STUDENT-MANAGEMENT-SYSTEM (METHOD'S) :
       => ADD-STUDENT-DATA
       => UPDATE-STUDENT-DATA
       => DELETE-STUDENT-DATA
       => INSERT-STUDENT-DATA
       => DISPLAY-STUDENT-DATA
    */
    """

    # ADD-STUDENT-DATA (FUNCTION) :
    @staticmethod
    def add_student_data():
        try:
            name = str(input("\n\t>>> ENTER, STUDENT-NAME : ")).upper()
            age = str(input("\t>>> ENTER, STUDENT-AGE : ")).upper()
            class_name = str(input("\t>>> ENTER, STUDENT-CLASS : ")).upper()
            roll = str(input("\t>>> ENTER, STUDENT-ROLL-NUMBER : ")).upper()
            mobile = str(input("\t>>> ENTER, STUDENT-MOBILE-NUMBER : ")).upper()
            address = str(input("\t>>> ENTER, STUDENT-ADDRESS : ")).upper()
            parent_name = str(input("\t>>> ENTER, STUDENT-PARENT-NAME : ")).upper()
            parent_mobile = str(input("\t>>> ENTER, PARENT-MOBILE-NUMBER : ")).upper()
            unique_id = str(input("\t>>> ENTER, STUDENT UNIQUE-ID : ")).upper()
            past_qualification = str(input("\t>>> ENTER, STUDENT PAST-QUALIFICATION :")).upper()

            if (len(name) == 0 or len(age) == 0 or len(class_name) == 0 or len(roll) == 0 or len(mobile) == 0
                    or len(address) == 0 or len(parent_name) == 0 or len(parent_mobile) == 0) or len(unique_id) == 0 or len(past_qualification) == 0:
                print("\n\t>>> ----- OOPS ! DON'T PROVIDE 'EMPTY-DATA', TRY AGAIN ! -----")
                sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
            else:
                if len(mobile) < 10 or len(mobile) > 10:
                    print("\n\t>>> ----- OOPS ! PLZ, PROVIDE AN 'VALID-MOBILE-NUMBER -----")
                    sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
                elif len(parent_mobile) < 10 or len(parent_mobile) > 10:
                    print("\n\t>>> ----- OOPS ! PLZ, PROVIDE AN 'VALID-MOBILE-NUMBER -----")
                    sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
                else:
                    # HERE, WE WILL CHANGE, DATA-TYPE OF 'INTEGER-VARIABLE' :
                    age = int(age)
                    roll = int(roll)
                    mobile = int(mobile)
                    parent_mobile = int(parent_mobile)
                    unique_id = int(unique_id)

                    # NOW, WE WILL UPDATE, STUDENT (DATA-STRUCTURE) :
                    student_name.append(name)
                    student_age.append(age)
                    student_class.append(class_name)
                    student_roll_number.append(roll)
                    student_mobile_number.append(mobile)
                    student_address.append(address)
                    student_parent_name.append(parent_name)
                    student_parent_mobile_number.append(parent_mobile)
                    student_unique_id.append(unique_id)
                    student_past_qualification.append(past_qualification)

                    # DISPLAY, STATUS :
                    print("\n\t>>> ----- YA, STUDENT-DATA (ADDED) - SUCCESSFULLY ! -----")
        except ValueError:
            print("\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA, TRY AGAIN !" + ValueError)
            sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")

    # UPDATE, STUDENT-DATA :
    @staticmethod
    def update_student_database():
        # CHECK, WEATHER 'DATABASE' => EMPTY OR NOT :
        if (len(student_name) == 0 or len(student_age) == 0 or len(student_class) == 0 or len(student_roll_number) == 0 or len(student_mobile_number) == 0
                or len(student_address) == 0 or len(student_parent_name) == 0 or len(student_parent_mobile_number) == 0 or len(student_unique_id) == 0 or len(student_past_qualification) == 0):
            print("\n\t>>> ----- OOPS, SEEMS LIKE 'STUDENT-MANAGEMENT' DATABASE IS, 'EMPTY' ! -----")
        else:
            # UPDATE, DATABASE (INFINITY-LOOP) - MENU :
            while True:
                print("\n\t>>> ----- UPDATE 'STUDENT-DATABASE' - (MENU) ----- \n")
                print("\t>>> PRESS (1) : UPDATE-NAME")
                print("\t>>> PRESS (2) : UPDATE-AGE")
                print("\t>>> PRESS (3) : UPDATE-CLASS")
                print("\t>>> PRESS (4) : UPDATE-ROLL-NUMBER")
                print("\t>>> PRESS (5) : UPDATE-STUDENT-MOBILE-NUMBER")
                print("\t>>> PRESS (6) : UPDATE-ADDRESS")
                print("\t>>> PRESS (7) : UPDATE-PARENT-NAME")
                print("\t>>> PRESS (8) : UPDATE-PARENT-MOBILE-NUMBER")
                print("\t>>> PRESS (9) : UPDATE-UNIQUE-ID")
                print("\t>>> PRESS (10) : UPDATE-PAST-QUALIFICATION")
                print("\t>>> PRESS (0) : EXIT")

                # USER, INPUT-CHOICE :
                option = str(input("\n\t>>> ENTER, YOUR 'CHOICE', TO UPDATE : "))

                # CHECK, WEATHER 'OPTION-VARIABLE' EMPTY OR NOT :
                if len(option) == 0:
                    print("\n\t>>> ----- SORRY, PLEASE PROVIDE AN 'OPTION-CHOICE' TRY AGAIN ! -----")
                    sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
                else:
                    # CONVERT, DATA-TYPE TO, INTEGER :
                    option = int(option)

                    # HERE, WE WILL TAKE 'ROLL-NUMBER' AS INDEX-VALUE :
                    roll_number = str(input("\n\t>>> ENTER, STUDENT ROLL-NUMBER : "))
                    # CHECK, WEATHER ROLL-NUMBER 'EMPTY OR NOT' :
                    if len(roll_number) == 0:
                        print("\n\t>>> ----- PLEASE, PROVIDE AN 'ROLL-NUMBER', TRY AGAIN !")
                        sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
                    else:
                        try:
                            # HERE, WE WILL TAKE 'STUDENT-ROLL-NUMBER' & THEIR ==> 'INDEX-VALUE' :
                            roll_number = int(roll_number)
                            # HERE, WE HAVE 'INDEX-VALUE' FROM STUDENT-ROLL-NUMBER (LIST) :
                            index_value = student_roll_number.index(roll_number)

                            # HERE, UPDATE-STUDENT-DATABASE (MENU) :
                            if option == 1:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'NAME' -----")
                                # LET'S TAKE NEW-NAME :
                                new_name = str(input("\n\t>>> ENTER, 'NEW-NAME' : "))
                                if len(new_name) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'NAME' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    student_name[index_value] = new_name
                                    print("\n\t>>> ----- YA, 'NEW-NAME' UPDATED ! SUCCESSFULLY -----")
                            elif option == 2:
                                print("n\t>>> ----- OK, LET'S UPDATE 'AGE' -----")
                                # LET'S TAKE NEW-AGE :
                                new_age = str(input("\n\t>>> ENTER, 'NEW-AGE' : "))
                                if len(new_age) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'AGE' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    new_age = int(new_age)
                                    student_age[index_value] = new_age
                                    print("\n\t>>> ----- YA, 'NEW-AGE' UPDATED ! SUCCESSFULLY -----")
                            elif option == 3:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'CLASS' -----")
                                # LET'S TAKE NEW-CLASS :
                                new_class = str(input("\n\t>>> ENTER, 'NEW-CLASS' : "))
                                if len(new_class) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'CLASS' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    student_class[index_value] = new_class
                                    print("\n\t>>> ----- YA, 'NEW-CLASS' UPDATED ! SUCCESSFULLY -----")
                            elif option == 4:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'ROLL-NUMBER' -----")
                                # LET'S TAKE NEW-ROLL-NUMBER :
                                new_roll = str(input("\n\t>>> ENTER, 'NEW-ROLL-NUMBER' : "))
                                if len(new_roll) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'ROLL-NUMBER' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    new_roll = int(new_roll)
                                    student_roll_number[index_value] = new_roll
                                    print("\n\t>>> ----- YA, 'NEW-ROLL-NUMBER' UPDATED ! SUCCESSFULLY -----")
                            elif option == 5:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'MOBILE-NUMBER' -----")
                                # LET'S TAKE NEW-MOBILE-NUMBER :
                                new_mobile = str(input("\n\t>>> ENTER, 'NEW-MOBILE-NUMBER' : "))
                                if len(new_mobile) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'MOBILE-NUMBER' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    if len(new_mobile) < 10 or len(new_mobile) > 10:
                                        print("\n\t>>> ----- SORRY, PLEASE PROVIDE AN VALID 'MOBILE-NUMBER' -----")
                                        sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                    else:
                                        new_mobile = int(new_mobile)
                                        student_mobile_number[index_value] = new_mobile
                                        print("\n\t>>> ----- YA, 'NEW-MOBILE-NUMBER' UPDATED ! SUCCESSFULLY -----")
                            elif option == 6:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'ADDRESS' -----")
                                # LET'S TAKE NEW-ADDRESS :
                                new_address = str(input("\n\t>>> ENTER, 'NEW-ADDRESS' : "))
                                if len(new_address) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'ADDRESS' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    student_address[index_value] = new_address
                                    print("\n\t>>> ----- YA, 'NEW-ADDRESS' UPDATED ! SUCCESSFULLY -----")
                            elif option == 7:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'PARENT-NAME' -----")
                                # LET'S TAKE NEW-ADDRESS :
                                new_parent_name = str(input("\n\t>>> ENTER, 'NEW-PARENT-NAME' : "))
                                if len(new_parent_name) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'PARENT-NAME' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    student_parent_name[index_value] = new_parent_name
                                    print("\n\t>>> ----- YA, 'NEW-PARENT-NAME' UPDATED ! SUCCESSFULLY -----")
                            elif option == 8:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'PARENT-MOBILE-NUMBER' -----")
                                # LET'S TAKE NEW-ADDRESS :
                                new_parent_mobile = str(input("\n\t>>> ENTER, 'NEW-PARENT-MOBILE-NUMBER' : "))
                                if len(new_parent_mobile) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'MOBILE-NUMBER' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    if len(new_parent_mobile) < 10 or len(new_parent_mobile) > 10:
                                        print("\n\t>>> ----- SORRY, PLEASE PROVIDE AN VALID 'MOBILE-NUMBER' -----")
                                        sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                    else:
                                        new_parent_mobile = int(new_parent_mobile)
                                        student_parent_mobile_number[index_value] = new_parent_mobile
                                        print("\n\t>>> ----- YA, 'NEW-PARENT-MOBILE-NUMBER' UPDATED ! SUCCESSFULLY -----")
                            elif option == 9:
                                print("\n\t>>> ----- OKE, LET'S UPDATE 'UNIQUE-ID' -----")
                                # LET'S TAKE NEW-UNIQUE-ID :
                                new_unique_id = str(input("\n\t>>> ENTER, 'NEW-UNIQUE-ID' : "))
                                if len(new_unique_id) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'UNIQUE-ID' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    new_unique_id = int(new_unique_id)
                                    student_unique_id[index_value] = new_unique_id
                                    print("\n\t>>> ----- YA, 'NEW-UNIQUE-ID' UPDATED ! SUCCESSFULLY -----")
                            elif option == 10:
                                print("\n\t>>> ----- OK, LET'S UPDATE 'NEW-PAST-QUALIFICATION' -----")
                                # LET'S TAKE NEW-ADDRESS :
                                new_qualification = str(input("\n\t>>> ENTER, 'QUALIFICATION' : "))
                                if len(new_qualification) == 0:
                                    print("\n\t>>> ----- OOPS ! PLEASE PROVIDE AN 'QUALIFICATION' -----")
                                    sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                                else:
                                    student_past_qualification[index_value] = new_qualification
                                    print("\n\t>>> ----- YA, 'NEW-QUALIFICATION' UPDATED ! SUCCESSFULLY -----")
                            elif option == 0:
                                sys.exit("\n\t>>> ----- ALRIGHT, SEE YOU SOON ! -----")
                        except ValueError:
                            print("\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID'-ROLL-NUMBER, TRY AGAIN !" + ValueError)
                            sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")



    # DELETE, STUDENT-DATA :
    @staticmethod
    def delete_student_data():
        if (len(student_name) == 0 or len(student_age) == 0 or len(student_class) == 0 or len(student_roll_number) == 0 or len(student_mobile_number) == 0
                or len(student_address) == 0 or len(student_parent_name) == 0 or len(student_parent_mobile_number) == 0 or len(student_unique_id) == 0 or len(student_past_qualification) == 0):
            print("\n\t>>> ----- OOPS, SEEMS LIKE 'STUDENT-MANAGEMENT' DATABASE IS, 'EMPTY' ! -----")
        else:
            while True:
                print("\n\t>>> ----- OH, SEEMS LIKE YOU WANT 'DELETE-STUDENT-DATA' -----")

                # HERE, WE WILL TAKE 'ROLL-NUMBER' AS INDEX-VALUE :
                roll_number = str(input("\n\t>>> ENTER, STUDENT 'ROLL-NUMBER' : "))
                # CHECK, WEATHER ROLL-NUMBER 'EMPTY OR NOT' :
                if len(roll_number) == 0:
                    print("\n\t>>> ----- PLEASE, PROVIDE AN 'ROLL-NUMBER', TRY AGAIN !")
                    sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
                else:
                    try:
                        # HERE, WE WILL TAKE 'STUDENT-ROLL-NUMBER' & THEIR ==> 'INDEX-VALUE' :
                        roll_number = int(roll_number)
                        # HERE, WE HAVE 'INDEX-VALUE' FROM STUDENT-ROLL-NUMBER (LIST) :
                        index_value = student_roll_number.index(roll_number)

                        # NOW, WE WILL DELETE-DATA :
                        name = student_name[index_value]
                        age = student_age[index_value]
                        class_name = student_class[index_value]
                        roll = student_roll_number[index_value]
                        mobile = student_mobile_number[index_value]
                        address = student_address[index_value]
                        parent_name = student_parent_name[index_value]
                        parent_mobile = student_parent_mobile_number[index_value]
                        unique_id = student_unique_id[index_value]
                        past_q = student_past_qualification[index_value]

                        # NOW, WE WILL REMOVE-DATA AT 'PARTICULAR-INDEX' :
                        student_name.remove(name)
                        student_age.remove(age)
                        student_class.remove(class_name)
                        student_roll_number.remove(roll)
                        student_mobile_number.remove(mobile)
                        student_address.remove(address)
                        student_parent_name.remove(parent_name)
                        student_parent_mobile_number.remove(parent_mobile)
                        student_unique_id.remove(unique_id)
                        student_past_qualification.remove(past_q)

                        print("\n\t>>> ----- YA, 'STUDENT-DATA' DELETED - SUCCESSFULLY ! -----")
                    except ValueError:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID'-ROLL-NUMBER, TRY AGAIN !" + ValueError)
                        sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")

    # DISPLAY, STUDENT-DATABASE :
    @staticmethod
    def display_database():
        # CHECK, WEATHER 'DATABASE' => EMPTY OR NOT :
        if (len(student_name) == 0 or len(student_age) == 0 or len(student_class) == 0 or len(student_roll_number) == 0 or len(student_mobile_number) == 0
                or len(student_address) == 0 or len(student_parent_name) == 0 or len(student_parent_mobile_number) == 0 or len(student_unique_id) == 0 or len(student_past_qualification) == 0):
            print("\n\t>>> ----- OOPS, SEEMS LIKE 'STUDENT-MANAGEMENT' DATABASE IS, 'EMPTY' ! -----")
        else:
            print("\n\t>>> ----- WELCOME, 'STUDENT-MANAGEMENT-SYSTEM' (DATABASE) : -----")
            database = {
                "STUDENT-ROLL-NUMBER": student_roll_number,
                "STUDENT-UNIQUE-ID": student_unique_id,
                "STUDENT-NAME": student_name,
                "STUDENT-AGE": student_age,
                "STUDENT-CLASS": student_class,
                "STUDENT-MOBILE-NUMBER": student_mobile_number,
                "STUDENT-ADDRESS": student_address,
                "STUDENT-PARENT-NAME": student_parent_name,
                "PARENT-MOBILE-NUMBER": student_parent_mobile_number,
                "STUDENT-PAST-QUALIFICATION": student_past_qualification
            }
            # PRINT, DATA-FRAME :
            dataframe = pandas.DataFrame(database)
            print(dataframe.head())


if __name__ == '__main__':
    # OBJECT, OF CLASS (STUDENT-MANAGEMENT-SYSTEM) :
    stud = student_management_system()

    # INFINITY-LOOP :
    while True:
        print("\n\t----- WELCOME TO, 'STUDENT-MANAGEMENT-SYSTEM' ----- \n")
        print("\t>>> PRESS (1) : ADD-STUDENT-DATA")
        print("\t>>> PRESS (2) : UPDATE-STUDENT-DATA")
        print("\t>>> PRESS (3) : DELETE-STUDENT-DATA")
        print("\t>>> PRESS (4) : DISPLAY-STUDENT-DATABASE")
        print("\t>>> PRESS (5) : EXIT-DATABASE")

        choice = str(input("\n\t>>> ENTER, YOUR CHOICE : "))

        try:
            if len(choice) == 0:
                print("\n\t>>> ----- SORRY, PLZ PROVIDE AN CHOICE ! -----")
                sys.exit("\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
            else:
                # CONVERT, DATA-TYPE TO 'INTEGER' :
                choice = int(choice)

                # CHECK, USER-CHOICE :
                if choice == 1:
                    # ADD, STUDENT-DATA :
                    print("\n\t>>> ALRIGHT, LET'S 'ADD' STUDENT-DATA !")
                    stud.add_student_data()
                elif choice == 2:
                    # UPDATE, STUDENT-DATA :
                    stud.update_student_database()
                    print("\n\t>>> OK, LET'S 'UPDATE' STUDENT-DATA !")
                elif choice == 3:
                    # DELETE, STUDENT-DATA :
                    stud.delete_student_data()
                    print("\n\t>>> OHH, OK LET'S 'DELETE' STUDENT-DATA !")
                elif choice == 4:
                    # DISPLAY, STUDENT-DATABASE :
                    print("\n\t>>> HERE, STUDENT-MANAGEMENT-SYSTEM (DATABASE) !")
                    stud.display_database()
                elif choice == 5:
                    # EXIT :
                    sys.exit("\t>>> ----- ALRIGHT, SEE YOU SOON AGAIN ! -----")
                else:
                    # IN-VALID CHOICE :
                    print("\n\t>>> PLEASE, CHOOSE AN 'CORRECT-CHOICE', TRY AGAIN !")
                    
        except ValueError:
            print("\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA, TRY AGAIN !" + ValueError)
            sys.exit("\n\t>>> ----- SOME-THING WENT WRONG, TRY AGAIN ! -----")
