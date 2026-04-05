"""
 Random Number Analyzer
 ---------------------------------
 Author: Luis Henrique Carmanhan

 Features:
 - Asks the user if they want to play
 - Generates random numbers
 - Displays statistics (max, min, average)
 - Shows numbers in sorted order
---------------------------------
"""
from random import randint
from time import sleep

# --- MAIN LOOP ---
while True:
    
    # Ask user if they want to start
    start = input('Do you want to play? (yes/no): ').strip().upper()
    
    if start == 'YES':
        
        # Ask how many numbers to generate
        qnt = int(input('How many numbers do you want to generate? '))
        
        if qnt <= 0:
            print('Invalid quantity of numbers.')
            continue
        
        # Define initial value
        intv_initial = 1
        
        # Ask for maximum range
        intv_final = int(input('Up to which number should the random values go? '))
        
        if intv_final <= 0:
            print('Invalid upper limit.')
            continue
        
        # --- RANDOM NUMBER GENERATION ---
        numbers = tuple(randint(intv_initial, intv_final) for _ in range(qnt))
        
        # --- DASHBOARD HEADER ---
        print("-" * 50)
        print(f"{'NUMERICAL ANALYSIS DASHBOARD':^50}")
        print("-" * 50)
        
        # --- DISPLAY GENERATED NUMBERS ---
        print("Generated numbers: ", end="")
        for n in numbers:
            print(f"[{n}]", end="")
            sleep(0.5)
        
        # --- ANALYSIS ---
        print(f"\n\nMAX value: {max(numbers)}")
        print(f"MIN value: {min(numbers)}")
        print(f"AVERAGE:   {sum(numbers) / len(numbers):.2f}")
        
        # --- SORTED VALUES ---
        print(f"Sorted values: {sorted(numbers)}")
        
        print("-" * 50)
        print('Thank you for using the program!')
    
    elif start == 'NO':
        print('Okay, see you next time!')
        break
    
    else:
        print('Invalid answer.')
        