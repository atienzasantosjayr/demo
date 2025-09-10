# Ask the user for numbers
user_input = input("Enter numbers separated by spaces: ")

# Check if the input is empty or only spaces
only_spaces = True
for ch in user_input:
    if ch != " ":
        only_spaces = False
        break

if user_input == "":
    print("No numbers entered.")
else:
    # Split input into pieces manually (like "10 20 -5" -> ["10","20","-5"])
    parts = user_input.split()

    # Convert strings to integers using a normal loop
    arr = []
    for p in parts:
        arr.append(int(p))

    # Initialize current_sum and max_sum
    current_sum = arr[0]
    max_sum = arr[0]

    # Go through the array starting from the second element
    i = 1
    while i < len(arr):
        num = arr[i]

        # Decide: start new sum or extend the old sum
        if num > current_sum + num:
            current_sum = num
        else:
            current_sum = current_sum + num

        # Update max_sum if needed
        if current_sum > max_sum:
            max_sum = current_sum

        i = i + 1  # move to the next number

    # Show the answer
    print("Maximum contiguous subarray sum:", max_sum)
