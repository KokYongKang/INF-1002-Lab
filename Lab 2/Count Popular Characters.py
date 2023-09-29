import sys


def calculate_top_5_characters(input_words):
    input_words = input_words.lower()
    word_frequency = {}

    for word in input_words:
        if word.isalpha():
            word_frequency[word] = word_frequency.get(word, 0) + 1

    sorted_words = sorted(word_frequency.items(), key=lambda x: (-x[1], x[0]))
    top_5_chars = sorted_words[:5]

    return ','.join([f'{word}:{count}' for word, count in top_5_chars])


input_words = sys.argv[1]
result = calculate_top_5_characters(input_words)
print(result)
