numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

# Create a list of even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Display the original range and the list of even numbers
print('Original Range:', list(numbers))
print('Even Numbers:', even_numbers)