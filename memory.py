import random
from typing import List


class Processor:
    def __init__(self, words_count, bits_count):
        self.__associative_memory: List[str] = []
        self.bits_count: int = bits_count
        self.fill(words_count, bits_count)

    @property
    def associative_memory(self) -> List[str]:
        return self.__associative_memory

    def fill(self, words_count: int, bits_count: int) -> None:
        for element in range(words_count):
            new_word = ''.join(str(random.randint(0, 1)) for _ in range(bits_count))
            self.__associative_memory.append(new_word)

    @staticmethod
    def get_g_value(prev_g_value: int, a_value: int, s_value: int, prev_l_value: int) -> int:
        g_value = bool(prev_g_value) or ((not bool(a_value) and bool(s_value)) and not bool(prev_l_value))
        return 1 if g_value else 0

    @staticmethod
    def get_l_value(prev_l_value, a_value, s_value, prev_g_value):
        l_value = bool(prev_l_value) or ((bool(a_value) and not bool(s_value)) and not bool(prev_g_value))
        return 1 if l_value else 0

    def compare(self, word: str, argument: str) -> int:
        prev_l_value: int = 0
        prev_g_value: int = 0
        for bit in range(self.bits_count):
            g_value: int = self.get_g_value(prev_g_value, int(argument[bit]), int(word[bit]), prev_l_value)
            l_value: int = self.get_l_value(prev_l_value, int(argument[bit]), int(word[bit]), prev_g_value)
            prev_l_value = l_value
            prev_g_value = g_value
        return 1 if prev_g_value > prev_l_value else (-1 if prev_g_value < prev_l_value else 0)

    def sort_min_to_max(self) -> List[str]:
        memory_content = list(self.__associative_memory)
        min_words: List[str] = []
        max_words: List[str] = []
        while len(memory_content) > 0:
            min_word = self.find_min_word(memory_content)
            max_word = self.find_max_word(memory_content)
            if min_word == max_word:
                min_words.extend([min_word] * memory_content.count(min_word))
                break
            min_words.extend([min_word] * memory_content.count(min_word))
            memory_content: List[str] = [word for word in memory_content if word != min_word]
            max_words: List[str] = [max_word] * memory_content.count(max_word) + max_words
            memory_content: List[str] = [word for word in memory_content if word != max_word]
        memory_content.clear()
        memory_content.extend(min_words)
        memory_content.extend(max_words)
        return memory_content

    def sort_max_to_min(self) -> List[str]:
        memory_content: List[str] = list(self.sort_min_to_max())
        memory_content.reverse()
        return memory_content

    def find_min_word(self, scope: List[str]) -> str:
        iteration: int = len(scope) - 1
        min_word: str = scope[iteration]
        while iteration >= 0:
            comparison_result: int = self.compare(scope[iteration], min_word)
            if comparison_result >= 0:
                iteration -= 1
                continue
            min_word: str = scope[iteration]
            iteration -= 1
        return min_word

    def find_max_word(self, scope: List[str]) -> str:
        iteration: int = len(scope) - 1
        max_word: str = scope[iteration]
        while iteration >= 0:
            comparison_result = self.compare(scope[iteration], max_word)
            if comparison_result <= 0:
                iteration -= 1
                continue
            max_word: str = scope[iteration]
            iteration -= 1
        return max_word

    def find_nearest_value(self, index: int, reverse: bool = False) -> str:
        self.sort_min_to_max()
        if 0 < index < len(self.__associative_memory) - 1:
            return self.__associative_memory[index + 1] if reverse else self.__associative_memory[index - 1]
        else:
            raise IndexError("List index out of range")

    @staticmethod
    def to_boolean(number) -> bool:
        return number != 0

    @staticmethod
    def to_int(character) -> int:
        return ord(character) - ord('0')
