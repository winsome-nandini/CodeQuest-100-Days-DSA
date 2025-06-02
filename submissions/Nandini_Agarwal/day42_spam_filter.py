l1=input("Enter email subjects (comma-separated): ").split('", "')
l2=input("Enter spam keywords (comma-separated): ").split(',')
l1[0] = l1[0].lstrip('"')       
l1[-1] = l1[-1].rstrip('"')     
for i in l2:
    for j in l1:
        if i in j:
            l1.remove(j)
print("Filtered Emails:\n-","\n- ".join(l1))