def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 15]
target = 7
result = binary_search(arr, target)

print(f"Element found at index {result}" if result != -1 else "Element not found")
