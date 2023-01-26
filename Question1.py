import math;
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24];    # Assign values to ages list
ages.sort();    # Using the pre-defined method sort() to sort the ages
print("Sorted list:", ages);

    # Finding Min and Max ages of the list
print("Minimum Age is:", min(ages));    # Using the pre-defined method min() for finding the minimum age in the list
print("Maximum Age is:", max(ages));    # Using the pre-defined method min() for finding the minimum age in the list

    # Finding the Median age of the list
MiddleIndex = (len(ages)-1)//2;  # Finding the middle index of the list ages
print("Middle Index is:", MiddleIndex);
if MiddleIndex % 2 != 0:    # If middle index is having two items, then sum of the items is divided by 2 is the median
    median = (ages[MiddleIndex] + ages[~MiddleIndex])/2;
else:
    median = ages[MiddleIndex];    # If middle index is having single item, then the median is the same item
print("Median Age is:", median);

    #Finding the Average age of the list
sum_of_ages = sum(ages);    # Using the pre-defined sum method for finding the sum of ages list.
avg_of_ages = sum_of_ages / len(ages);    # The sum of ages is divided by length of the ages list to get the average
print("Average of ages:", avg_of_ages);

    #Finding the Range of ages
min_age = min(ages);    # Using the pre-defined min method to find the min value of ages list
max_age = max(ages);    # Using the pre-defined max method to find the max value of ages list
Range = max_age - min_age;
print("Range of Ages list is:", Range);