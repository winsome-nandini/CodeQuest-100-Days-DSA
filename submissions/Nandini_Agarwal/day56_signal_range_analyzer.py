arr = list(map(int,input("Enter signal strengths (space-separated): ").split()))
no_query=int(input("Enter number of queries:"))
l=[]
for i in range(no_query):
    b=list(map(int,input(f"Query {i+1} - Enter range (start end):").split()))
    l.append(b)
for i in l:
    start = i[0] - 1  # Convert to 0-based indexing
    end = i[1]        # Python slicing is exclusive on the end

    sub = arr[start:end]
    s = sum(sub)

    print(f"Sum for range [ {i[0]}, {i[1]} ]:", end=" ")
    print(" + ".join(map(str, sub)), "=", s)