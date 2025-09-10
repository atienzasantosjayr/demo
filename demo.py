arr = list(map(int, input("Enter numbers separated by space: ").split()))
if not arr:
    print("No numbers entered.")
else:
    current_sum = best_sum = arr[0]
    for x in arr[1:]:
        # Update current_sum to max of starting new at x or extending
        current_sum = max(x, current_sum + x)
        # Update best_sum if we found a better sum
        best_sum = max(best_sum, current_sum)
    print("Maximum contiguous subarray sum:", best_sum)
