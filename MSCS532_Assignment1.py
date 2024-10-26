#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to sort a list in descending order using insertion sort
def sort_descending(data):
    # Iterate through each element in the list starting from the second element
    for idx in range(1, len(data)):
        current_element = data[idx]
        pos = idx

        # Shift elements of data[0..idx-1] that are smaller than current_element
        # to the right by one position
        while pos > 0 and data[pos - 1] < current_element:
            data[pos] = data[pos - 1]
            pos -= 1

        # Insert the current element at its correct position
        data[pos] = current_element

    return data


# In[2]:


# Entry point of the program
if __name__ == "__main__":
    # Step 1: Ask the user to input a series of numbers
    user_input = input("Enter a series of integers separated by spaces: ")

    # Step 2: Transform the input string into a list of integers
    numbers_list = [int(num) for num in user_input.split()]

    # Step 3: Call the sorting function to sort the list in descending order
    sorted_list = sort_descending(numbers_list)

    # Step 4: Display the sorted list
    print("Sorted list in descending order:")
    print(sorted_list)







