import math;

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}      # Creating a set and assigning values
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Initial it_company set:", it_companies)

    # Find the length of the set it_companies
print("Length of it_companies set: ", len(it_companies))    # Using the pre-defined len() method for finding the length of the set

    # Add 'Twitter' to it_companies
it_companies.add('Twitter')     # Using add function insert a company into the set it_companies
print("After adding Twitter company:", it_companies)

    # Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intel','Adobe'])      # Using update function for adding two comapanies to the set it_companies
print("After adding two comapnies:", it_companies)

    # Remove one of the companies from the set it_companies
it_companies.remove('Amazon')       # Using remove function to remove Amazon from it_companies set
print("After removing Amazon company:", it_companies)

    # Difference between remove and discard
print("Remove raises an error if the element is not in the set, discard doesn't.")

    # Join A and B
a_union_b = A.union(B)      # Using union operator to join two sets i.e., A and B
print("A union B:", a_union_b)

    # Find A intersection B
a_int_b = A.intersection(B)
print("A Intersection B:", a_int_b)     # Using intersection operator to get the common data from two sets A and B

    # Is A subset of B
print("Is A subset of B:", A.issubset(B))      # issubset operator returns boolean value whether A is a subset of B or not

    # DO A and B disjoint sets
print("Is A disjoint of B:", A.isdisjoint(B))      # The isdisjoint operator returns boolean value whether A is a subset of B or not

    # Join A with B and B with A
print("A join with B:", A.union(B))      # Using union to join A with B
print("A join with B:", B.union(A))     # Using union to join B with A

    # Symmetric difference between A and B
print("Symmetric Diff btw A and B:", A.symmetric_difference(B))        # Using the symmetric_difference operator for finding symmetric difference b/w A and B

    # Delete the sets completely
del it_companies    # Using del operator to delete it_companies set
del A       # Using del operator to delete A set
del B       # Using del operator to delete B set

    # Convert ages to a set and compare the length of the list and the set.
age_set = set(age)      # Using the set method to convert ages to a set
print("Diff between len_of_age_list and len_of_age_set is:", len(age) - len(age_set))