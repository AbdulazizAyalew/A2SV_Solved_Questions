class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        length_counter = 0

        for word in words:
            counter_word = Counter(word)
            for w in counter_word:
                if w not in chars_count or counter_word[w] > chars_count[w]:
                    break
            else:
                length_counter += len(word)
        
        return length_counter
