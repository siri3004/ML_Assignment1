import math;

    # Create a tuple that contain names of your sisters and brothers (imaginary siblings are fine)
sisters = ("Emma", "Emily", "Elena");
brothers = ("Sam", "Dean", "Stefan");

    # Join brothers and sisters tuples and assign it to the siblings
siblings = sisters + brothers;     # Using + operator to join the siblings
print("Siblings are:", siblings);

    # Total number of siblings
num_of_siblings = len(siblings);    # Using pre-defined len() method to find the length of the siblings
print("Number of siblings:", num_of_siblings);

    # Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Justin", "Enola");   # Modyfing the siblings tuple by adding the family members to  siblings tuple and assigning it to family_members tuple
print("Family members:", family_members);