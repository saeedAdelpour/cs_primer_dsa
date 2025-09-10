from rich import print
from spellchecker import SpellChecker

spell = SpellChecker()


def get_new_words(word):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(word)):
        for c in chars:
            new_word = word[:i] + c + word[i + 1 :]
            new_word_correction = spell.correction(new_word)
            is_new_word_correct = new_word == new_word_correction
            if is_new_word_correct and new_word != word:
                yield new_word


def check_exist_in_tails(word, new_word, tails):
    for tail in tails:
        if (tail[0] == word and tail[1] == new_word) or (
            tail[0] == new_word and tail[1] == word
        ):
            return True
    return False


class Node:
    data: str

    def __init__(self, data):
        self.data = data


class Tail:
    node1: Node
    node2: Node

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


class Graph:
    tails: list[Tail]
    checklist: list[str]

    def __init__(self):
        self.tails = []
        self.checklist = []

    def check_exists_in_tails(self, word, new_word):
        for tail in self.tails:
            if (tail.node1.data == word and tail.node2.data == new_word) or (
                tail.node1.data == new_word and tail.node2.data == word
            ):
                return True
        return False

    def append_tail(self, word, new_word):
        tail = Tail(Node(word), Node(new_word))
        self.tails.append(tail)

    def create_cluster(self, word, level=0):
        self.checklist.append(word)

        for new_word in get_new_words(word):

            if not self.check_exists_in_tails(word, new_word):
                self.append_tail(word, new_word)

            if not self.is_word_checked(new_word):
                self.create_cluster(new_word, level + 1)

    def is_word_checked(self, new_word):
        return new_word in self.checklist

    def find_best_route(self, word):
        self.tails[0]


def main():
    word1 = "pig"
    word2 = "sty"
    graph = Graph()

    graph.create_cluster(word1)
    print(graph.tails)


if __name__ == "__main__":
    main()
