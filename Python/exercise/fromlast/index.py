def fromLast(list, n):
    slow = list.head
    fast = list.head

    for i in range(n):
        fast = fast.next
    
    # slow ~ fast distance = n 
    # if slow = 0 -> fast = n 

    while (fast.next):
        slow = slow.next 
        fast = fast.next
    return slow 