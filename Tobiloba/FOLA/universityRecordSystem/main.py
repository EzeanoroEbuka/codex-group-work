from FOLA.universityRecordSystem.university_record_system import add_student_to_university_record, \
    create_student_record, display_university_record, display_student_offered_courses, display_student_city, \
    display_student_zip_code, add_new_course, remove_course, update_name_age_city_zip_code, \
    display_overall_number_of_students, display_university_courses


def main_menu():
    menu = """
        -------------- SK UNIVERSITY ------------
        1. Create Student Record
        2. Display Student Record
        3. View Student Information
        4. Add Course
        5. Remove Course
        6. Update Student Details
        7. Display All Students 
        0. Exit
        ------------------------------------
        """
    return menu


def student_info_menu():
    menu = """
    ------------ VIEW STUDENT INFORMATION  ------------
    1. Display Student's Course(s)
    2. Display Student's City
    3. Display Student's Zip Code
    0. Exit
    ----------------------------------------------------
    """
    return menu


is_Running = True

while is_Running:
    print('-----------WELCOME TO SK UNIVERSITY RECORD SYSTEM------------\n')
    print(main_menu())
    print()
    is_also_Running = True

    option = input('Enter your option: ')
    match option:
        case '1':
            print('------------ CREATE STUDENT RECORD  ------------\n')
            name = input('Enter Student Name: ')
            age = input('Enter Student Age: ')
            city = input('Enter Student City: ')
            zip_code = input('Enter Student Zip Code: ')
            add_student_to_university_record(name, create_student_record(name, age, city, zip_code))

        case '2':
            print('------------ DISPLAY STUDENT RECORD  ------------\n')
            name = input('Enter Student Name: ')
            display_university_record(name)

        case '3':
            while is_also_Running:
                print(student_info_menu())
                print()

                option = input('Enter your option: ')
                match option:
                    case '1':
                        print('------------ STUDENT\'S COURSE(S) ------------\n')
                        name = input('Enter Student Name: ')
                        display_student_offered_courses(name)

                    case '2':
                        print('------------ STUDENT\'S CITY ------------\n')
                        name = input('Enter Student Name: ')
                        display_student_city(name)

                    case '3':
                        print('------------ STUDENT\'S ZIP CODE ------------\n')
                        name = input('Enter Student Name: ')
                        display_student_zip_code(name)

                    case '0':
                        is_also_Running = False

                    case _:
                        print('Invalid Option')

        case '4':
            print('------------ ADD COURSE ------------\n')
            name = input('Enter Student Name: ')
            display_university_courses()
            course = input('Enter Course Name: ')
            add_new_course(name, course.title())

        case '5':
            print('------------ REMOVE COURSE ------------\n')
            name = input('Enter Student Name: ')
            course = input('Enter Course Name: ')
            remove_course(name, course.title())

        case '6':
            print('------------ UPDATE STUDENT DETAILS ------------\n')
            name = input('Enter Student Name: ')
            updated_name = input('Enter Updated Student Name: ')
            updated_age = input('Enter Updated Student Age: ')
            updated_city = input('Enter Updated Student City: ')
            updated_zip_code = input('Enter Updated Student Zip Code: ')
            update_name_age_city_zip_code(name, updated_name, updated_age, updated_city, updated_zip_code)

        case '7':
            print('------------ ALL STUDENTS ------------\n')
            print(f'There are {display_overall_number_of_students()} Students in SK University')

        case '0':
            print('THANK YOU FOR BANKING WITH US >>>>>>>>>>>>')
            print('PROGRAM TERMINATED')
            is_Running = False

        case _:
            print('Invalid Option')
