def analyze_and_print(data):
    char_counts = {}
    max_count = 1
    
    for char in data:
        char = char.strip()
        if char in char_counts:
            char_counts[char] += 1
            max_count = max(max_count, char_counts[char])
        else:
            char_counts[char] = 1
    
    unique_chars = sorted(set(char_counts.keys()))

    for i in range(max_count, 0, -1):
        line = ''.join('#' if char_counts.get(char, 0) >= i else ' ' for char in unique_chars)
        print(line)

    for char in unique_chars:
        print(char, end=' ')

if __name__ == '__main__':
    user_input = input()
    analyze_and_print(user_input)