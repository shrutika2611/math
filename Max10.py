# Step 1: Initialize an empty list to store numbers
numbers = []

# Step 2: Prompt the user to enter up to 10 numbers
print("Enter up to 10 numbers. Type 'done' when you're finished.")

while len(numbers) < 10:
    user_input = input(f"Enter number {len(numbers) + 1}: ")
    
    if user_input.lower() == 'done':
        break
    
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

# Step 3: Check if any numbers were entered
if numbers:
    # Step 4: Find the maximum number
    max_number = max(numbers)
    # Step 5: Display the result
    print(f"The maximum number you entered is: {max_number}")
else:
    print("No numbers were entered.")
