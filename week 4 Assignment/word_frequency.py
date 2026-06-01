#Question 4 — Word Frequency Counter
def word_frequency(text):

    text = text.lower()

    for ch in ",.!?":
        text = text.replace(ch, "")

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    top_words = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return top_words

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

result = word_frequency(text)

print("Top 3 words:")
for word, count in result:
    print(f"{word} - {count} times")