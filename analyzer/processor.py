from collections import Counter

class TextProcessor:
    """
    Klass för att bearbeta textdata.
    """
    def __init__(self, lines):
        self.lines = lines

    def count_lines(self):
        return len(self.lines)

    def count_words(self):
        return sum(len(line.split()) for line in self.lines)

    def most_common_word(self):
        words = []
        for line in self.lines:
            words.extend(line.split())
        if not words:
            return None
        counter = Counter(words)
        return counter.most_common(1)[0][0]
