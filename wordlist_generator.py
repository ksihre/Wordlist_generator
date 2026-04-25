def generate_wordlist():
    words = input("Enter words separated by commas (e.g., admin,1234,password): ").split(',')
    filename = input("Enter filename to save the wordlist (e.g., wordlist.txt): ")

    combinations = []

    # Combine words in different ways
    for word in words:
        for word2 in words:
            combinations.append(word.strip() + word2.strip())
            combinations.append(word2.strip() + word.strip())

    # Save to a file
    with open(filename, 'w') as f:
        for combo in set(combinations):  # remove duplicates
            f.write(combo + '\n')

    print(f"Wordlist saved to {filename}")

if __name__ == "__main__":
    generate_wordlist()
