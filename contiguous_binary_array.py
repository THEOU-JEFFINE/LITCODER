def findMaxLength(nums):
    # Initialize a HashMap to store the running sum and its index
    sum_index_map = {0: -1}
    max_length = 0
    current_sum = 0

    for index, num in enumerate(nums):
        # Update the running sum based on the current element
        current_sum += 1 if num == 1 else -1

        # Check if the current sum has been seen before
        if current_sum in sum_index_map:
            # Update the maximum length if a valid subarray is found
            max_length = max(max_length, index - sum_index_map[current_sum])
        else:
            # If the current sum is not seen before, add it to the HashMap
            sum_index_map[current_sum] = index

    return max_length


# Get user input for the binary array
user_input = input("Enter a binary array (e.g., 0 1 0 1): ")
input_nums = list(map(int, user_input.split()))

# Call the function with the user-provided input
result = findMaxLength(input_nums)

# Display the result
print(f"Output: {result}")
