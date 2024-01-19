# Time Complexity: O(1)
# Space Complexity: O(1)

# ALGO
# If 'N' is prime, the only divisors are 1 and 'N' itself. 
# The player can only choose x = 1, and after that, 'N' becomes 'N' - 1. 
# Now, the other player will face 'N' - 1, and he can choose whatever will be winning for him.
# So, to determine the winner, you just need to check if 'N' is a prime number. 
# If it is, then the player who started with 'N' is the loser; 
# otherwise, they are the winner.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def ninjaFight(n):
	if is_prime(n):
		return 2
	else:
		return 1
