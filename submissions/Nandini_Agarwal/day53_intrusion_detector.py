arr = list(map(int, input("Enter sorted response times: ").split()))
n = len(arr)

# Use the most likely correct difference (between first two elements)
expected_diff = arr[1] - arr[0]

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    # Check difference with previous and next elements
    if mid > 0 and arr[mid] - arr[mid - 1] != expected_diff:
        print(f"Anomalous response time detected: {arr[mid]}")
        break
    elif mid < n - 1 and arr[mid + 1] - arr[mid] != expected_diff:
        print(f"Anomalous response time detected: {arr[mid + 1]}")
        break