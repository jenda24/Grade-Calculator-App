"""
This file contains the logic to write the grades to the
Grades.csv file. Default values will be stored as N/A


"""

import csv
import os


def create_csv_file() -> None:
    """
    Create the Grades.csv file with headers if it does nto exist

    :return: None
    """
    # headers for the CSV file
    headers = ["Name", "Final Grade", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6"]

    # check if the file exists + make csv
    if not os.path.isfile("Grades.csv"):
        with open("Grades.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def write_to_csv(student_name, final_grade, class_data) -> bool:
    """
    Next, write student grades to Grades.csv

    :param student_name (str): Name of the student
    :param final_grade (str): Calculated final grade
    :param class_data (list): List of tuples (class_name, class_grade) for each class
    :return: True if the function was successful
    """
    # check csv exists
    create_csv_file()

    row_data = [student_name, final_grade]

    # format class data as "Class: Grade" or "N/A" if not provided
    # used ai for lines 42 - 48 because I didn't know how to format this
    for i in range(6):
        if i < len(class_data) and class_data[i][0] and class_data[i][1]:
            # If both class name and grade are provided
            row_data.append(f"{class_data[i][0]}: {class_data[i][1]}")
        else:
            # If either class name or grade is missing
            row_data.append("N/A")

    # write the info to csv!!!
    with open("Grades.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_data)

    return True


def get_class_data_from_ui(ui_instance) -> list[tuple[str, str]]:
    """
    Used to get class data from UI elements

    :param ui_instance: Contains the class name and grade inputs
    :return: list of tuples (class_name, class_grade) for every class
    - I did this for a better format. It made way more sense than
      havign 12 columns designated for separate class names + grades
    """

    num_classes = int(ui_instance.num_classes.currentText())
    class_data = []

    for i in range(num_classes):
        class_name = ui_instance.class_name_inputs[i].text()
        class_grade = ui_instance.class_grade_inputs[i].text()
        class_data.append((class_name, class_grade))

    # fill remaining classes with default/empty data
    while len(class_data) < 6:
        class_data.append(("", ""))

    return class_data


def save_grades(ui_instance) -> tuple[bool, str]:
    """
    Saves student's grades to the Grades.csv when the submit button is clicked

    :param ui_instance: UI instance that contains all input fields
    :return: True or False (success or failure) along with a message
    indicating what happened
    """

    # get student name
    student_name = ui_instance.studentNameInput.text()
    if not student_name:
        return False, "Please enter a student name"

    # get final grade
    final_grade = ui_instance.finalgrade_output.text()
    if final_grade == "--":
        return False, "Please calculate the grade first"

    # get class data
    class_data = get_class_data_from_ui(ui_instance)

    # write itto CSV
    success = write_to_csv(student_name, final_grade, class_data)

    if success:
        return True, f"Grades for {student_name} saved to Grades.csv"
    else:
        return False, "Error saving to CSV"