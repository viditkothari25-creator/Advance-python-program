s1 = "ABC"
s2 = "AC"

match = 1
mismatch = -1
gap = -2

m = len(s1)
n = len(s2)

# Create DP table
dp = [[0] * (n + 1) for i in range(m + 1)]

# Initialize first row
for j in range(1, n + 1):
    dp[0][j] = dp[0][j - 1] + gap

# Initialize first column
for i in range(1, m + 1):
    dp[i][0] = dp[i - 1][0] + gap

# Fill DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s1[i - 1] == s2[j - 1]:
            score = match
        else:
            score = mismatch

        diagonal = dp[i - 1][j - 1] + score
        top = dp[i - 1][j] + gap
        left = dp[i][j - 1] + gap

        dp[i][j] = max(diagonal, top, left)

# Print DP table
print("DP Table:")

for row in dp:
    print(row)

print("Maximum Alignment Score:", dp[m][n])

# Traceback
i = m
j = n

align1 = ""
align2 = ""

while i > 0 or j > 0:

    # Diagonal move
    if i > 0 and j > 0:

        if s1[i - 1] == s2[j - 1]:
            score = match
        else:
            score = mismatch

        if dp[i][j] == dp[i - 1][j - 1] + score:
            align1 += s1[i - 1]
            align2 += s2[j - 1]

            i -= 1
            j -= 1
            continue

    # Up / Top move
    if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
        align1 += s1[i - 1]
        align2 += "-"

        i -= 1

    # Left move
    elif j > 0:
        align1 += "-"
        align2 += s2[j - 1]

        j -= 1

# Reverse alignments
align1 = align1[::-1]
align2 = align2[::-1]

print("Sequence 1:", align1)
print("Sequence 2:", align2)