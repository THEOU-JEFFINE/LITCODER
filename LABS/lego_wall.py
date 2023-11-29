def legoWall(n, m):
    MOD = 1000000007

    # Check if a brick of type (1, 1, width) can be placed at a given position
    def isValid(j, width):
        return j + width <= m

    # Initialize the dp array with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: there is one way to build a wall of height 0 and any width
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill the dp array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Horizontal extension
            for width in range(1, 5):
                if isValid(j, width):
                    dp[i][j] += dp[i][j - width]
                    dp[i][j] %= MOD

            # Vertical extension
            dp[i][j] += dp[i - 1][j]
            dp[i][j] %= MOD

    return dp[n][m]

# Input values
n = int(input("Enter the height of the wall: "))
m = int(input("Enter the width of the wall: "))

# Calculate and print the result
result = legoWall(n, m)
print(result)
