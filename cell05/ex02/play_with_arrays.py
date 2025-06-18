original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [number + 2 for number in original_array if number + 2 > 5]
print("Original array:", original_array)
print("Filtered new array (+2 > 5):", new_array)