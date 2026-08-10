'''
Question 5
'''

def most_common_word(story: tuple[str, ...]) -> str:
    word_counts = {}
    for part in story:
        words = part.lower().replace(".", "").replace(",", "").split()
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    winner_word = ""
    max_count = 0
    for word in word_counts:
        if word_counts[word] > max_count:
            max_count = word_counts[word]
            winner_word = word

    return f"\n{winner_word}\n{max_count} times"

print(most_common_word(("hello  world", "hello three .is sunday", "weekend .is fun",  "yes is it")))
story1 =(
    "The little fox saw the little bird and the little cat.",
    "The fox happy because the little bird sang, and the little cat jumped.",
    "The little fox, the little bird, and the little cat became friends."
)
print(most_common_word(story1))