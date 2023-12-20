def countPalindromicSubsequence(s):
    # Initialize array for min accurence and max accurence
    min_occurence = [float('inf')]*26
    max_occurence = [float('-inf')]*26

    # Iterate to find min and
    for i in range(len(s)):
        char_index = ord(s[i]) - ord('a')
        min_occurence[char_index] = min(min_occurence[char_index], i)
        max_occurence[char_index] = max(max_occurence[char_index], i)

    count = 0 # Count number of solutions

    for i in range(26):
        if min_occurence[i] == float('inf') or max_occurence[i] == float('-inf'):
            continue

        # Initialize set to contain unique char between first and last index
        unique_char = set()

        for j in range(min_occurence[i] + 1, max_occurence[i]):
            unique_char.add(s[j])

        count += len(unique_char)
    
    return count
print(countPalindromicSubsequence('bbcbaba'))