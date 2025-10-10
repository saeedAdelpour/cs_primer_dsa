import json
import re
import time

from rich import print
from spellchecker import SpellChecker

spell = SpellChecker()


def get_new_words(word, checklist=[]):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(word)):
        for c in chars:
            new_word = word[:i] + c + word[i + 1 :]
            new_word_correction = spell.correction(new_word)
            is_new_word_correct = new_word == new_word_correction
            if is_new_word_correct and new_word != word and new_word not in checklist:
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
    neighbors: "dict[str, Node]"

    def __init__(self, data):
        self.data = data
        self.neighbors = {}

    def __repr__(self):
        return f"Node: {self.data}"

    def __eq__(self, other):
        return self.data == other.data


class Tail:
    pass


class Graph:
    nodes: dict[str, Node]

    def __init__(self):
        self.nodes = dict()

    def check_exists_in_tails(self, word, new_word):
        word_node = self.nodes.setdefault(word, Node(word))
        new_word_node = self.nodes.setdefault(new_word, Node(new_word))

        new_word_node_found = word_node.neighbors.get(new_word)
        if new_word_node_found is None:
            word_node.neighbors[new_word] = new_word_node
            new_word_node.neighbors[word] = word_node

    def create_cluster(self, word):
        self.nodes = {}
        todo_list = set()
        checklist = set()
        if len(todo_list) == 0:
            todo_list.add(word)

        while len(todo_list) != 0:
            _word = todo_list.pop()
            if _word not in checklist:
                words = list(get_new_words(_word, checklist))
                for new_word in words:
                    self.check_exists_in_tails(_word, new_word)
                    todo_list.add(new_word)

            checklist.add(_word)

    def find_best_route(self, word1, word2):

        routes = []
        checklist = set()
        todo_list = []

        node1 = self.nodes[word1]
        node2 = self.nodes[word2]

        if len(todo_list) == 0:
            todo_list.append(word1)

        while len(todo_list) != 0:
            _word1 = todo_list.pop(0)
            if _word1 not in checklist:
                _node1 = self.nodes[_word1]

                for __word1 in _node1.neighbors.keys():
                    self.add_to_routes(_word1, __word1, word2, routes)
                    todo_list.append(__word1)

                checklist.add(_word1)
        return routes

    def add_to_routes(self, word1, word2, dest_word, routes):
        found_similar_routes_idx = [
            [i, r]
            for i, r in enumerate(routes)
            if r and r[-1] == word2 and r[-1] != dest_word
        ]
        found_similar_routes = [r[1] for r in found_similar_routes_idx]
        routes_with_last_node = [
            r for r in routes if r and r[-1] == word1 and word2 not in r
        ]
        x = self.get_min(found_similar_routes)
        y = self.get_min(routes_with_last_node)
        last_node_route_is_smaller = x is not None and y is not None and x > y
        should_add_route = (not found_similar_routes) or last_node_route_is_smaller
        if last_node_route_is_smaller:
            for i, _ in found_similar_routes_idx:
                routes[i] = []

        if should_add_route:

            if routes_with_last_node:
                for r in routes_with_last_node:
                    routes.append([*r, word2])
            else:
                routes.append([word1, word2])

    def get_min(self, routes):
        if not routes:
            return None
        return min([len(r) for r in routes])

    def write(self, data, path):
        with open(path, "w") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)


def main():
    word1 = "altar"
    word2 = "upset"
    self = Graph()

    self.create_cluster(word1, set(), set())
    # print(self.nodes)
    # x = self.find_best_route(word2, word1, [], set())
    # routes = sorted([r for r in x if r and r[-1] == word1], key=len, reverse=True)
    # print(routes)


if __name__ == "__main__":
    main()
