import math;

    # Create an empty dictionary named dog
dog = {};

    # Adding name, color, breed, legs, age to the dog dictionary
dog = {"name": "Jonny", "color": "Black", "breed": "Great Dane", "legs": 4, "age": 6}

    # Creating a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name": "Sireesha", "last_name": "P", "gender": "Female", "age": 25, "marital_status": "Married", "skills": ["Python","SQL"], "country": "INDIA", "city": "Khammam", "address": "Church Road, Khammam"}

    # Get the length of the student dictionary
print("Student Dictionary length is:", len(student));

    # Get the value of skills and check the data type, it should be a list
skills = student['skills'];
print("Student skills is:", student['skills']);
print(type(skills));

    # Modify the skills values by adding one or two skills
student['skills'].append("AWS")     # Modified the skills list using append method
student['skills'].append("JavaScript")
print("Updated Skills list is:", student['skills']);

    # Get the dictionary keys as a list
keys_list = list(student.keys());   # Using the predefined keys() to return all the keys to a list
print("Keys list is:",keys_list);

    # Get the dictionary values as a list
values_list = list(student.values());      # Using the predefined values() to return all the keys to a list
print("Values list is:", values_list);
