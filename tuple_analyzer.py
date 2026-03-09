"""
Tuple Analyzer - Advanced Version
---------------------------------
Author: Luis Henrique Carmanhan

Features:
- Creates a tuple with 4 numbers provided by the user.
- Allows the user to check if a number exists in the tuple.
- Counts how many times the number appears.
- Displays the smallest and largest numbers.
- Demonstrates tuple operations without using lists.
"""

# --- USER INPUT ---
# Here we create the tuple using values entered by the user
numbers =(
    int(input('Númber 1: ')),
    int(input('Númber 2: ')),
    int(input('Númber 3: ')),
    int(input('Númber 4: ')),
)

# Example result: (4, 2, 7, 2)

# --- DISPLAY THE CREATED TUPLE ---
print('\nTuple:', numbers)

# --- NUMBER CHECK SYSTEM ---
# Ask the user if they want to analyze a specific number
choice = input('Do you want to check a number? (Yes/No): ').upper().strip()
if choice == 'YES':
    
    # Ask which number the user wants to check
    target = int(input('Which number do you want to check? '))
    
    # Check if the number exists in the tuple
    if target in numbers:
        print(f'The number {target} appears {numbers.count(target)} times.')
    
    else:
        print('This number does not appear in the tuple.')

# --- EVEN NUMBER ANALYSIS ---
# This section checks which numbers in the tuple are even
print("Even numbers in the tuple:")

for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')


# --- TUPLE ANALYSIS ---
# Show smallest and largest values in the tuple
print("Smallest number: ", min(numbers))
print("Largest number", max(numbers))

# --- FINAL MESSAGE ---
print("\nThank you for using Tuple_Analyzer_Advanced!")