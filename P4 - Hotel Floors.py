# Time_Complexity: O(n)
# Space_Complexity: O(1)

#ALGO
# count = 0
# TRAVERSE queries
# IF i-th element starts with '+', count++
# RETURN count 

def hotelBookings(queries):
    count = 0
    for i in queries:
        if i and i[0]=='+':
            count += 1
    return count
