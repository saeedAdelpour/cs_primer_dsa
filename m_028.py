import json

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

    def create_cluster(self, word, level=0, checklist=set()):
        checklist.add(word)

        for new_word in get_new_words(word):

            self.check_exists_in_tails(word, new_word)

            if not self.is_word_checked(new_word, checklist):
                self.create_cluster(new_word, level + 1, checklist)
        # return level

    def is_word_checked(self, new_word, checklist=[], directions={}):
        return new_word in checklist

    def find_best_route(self, word1, word2, routes=[], checklist=set(), level=0):
        if word1 in checklist:
            return routes

        # print("*" * 40, word1, word2)
        # print({"routes": routes})
        # if level > 1:
        #     return routes
        node1 = self.nodes[word1]
        node2 = self.nodes[word2]

        if node2.data in node1.neighbors:
            print("end", word1, word2)
            self.add_to_routes(word1, word2, word2, routes, do_print=True)
            return routes

        for _n1 in node1.neighbors.values():
            # print(
            #     {
            #         "_n1": _n1,
            #         "node1": node1,
            #         "routes": routes,
            #         "checklist": checklist,
            #     }
            # )
            # input("continue?")

            self.add_to_routes(node1.data, _n1.data, word2, routes)

        checklist.add(word1)

        for _n1 in node1.neighbors.values():

            self.find_best_route(_n1.data, word2, routes, checklist, level + 1)
            checklist.add(_n1.data)
            # print({"routes": routes, "checklist": checklist})
        return routes

    def add_to_routes(self, word1, word2, dest_word, routes, do_print=False):
        # if word1 in (
        #     # "sta",
        #     "stu",
        # ):
        #     do_print = True

        # do_print = True
        # do_print = False

        if do_print:
            log_job = self.write
        else:
            log_job = lambda *args, **kwargs: ...

        # if word1 == "stu":
        #     self.write(routes, "routes.json")

        # log_job("-" * 40, word1, word2)
        found_similar_routes = [r for r in routes if word2 in r and r[-1] != dest_word]
        log_job(
            {"found_similar_routes": found_similar_routes},
            "found_similar_routes_{}_{}.json".format(word1, word2),
        )
        if not found_similar_routes:
            routes_with_last_node = [r for i, r in enumerate(routes) if r[-1] == word1]
            log_job(
                {
                    "step": "before",
                    "len(routes)": len(routes),
                    "routes_with_last_node": routes_with_last_node,
                    "routes": routes,
                },
                "{}_{}.json".format(word1, word2),
            )

            if routes_with_last_node:
                for r in routes_with_last_node:
                    routes.append([*r, word2])
            else:
                routes.append([word1, word2])

            # if routes_with_last_node:
            #     for r in routes_with_last_node:
            #         r.append(word2)
            # else:
            #     routes.append([word1, word2])

    def write(self, data, path):
        with open(path, "w") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)


# init
word1 = "pig"
word2 = "sty"
routes = []
checklist = []


def main():
    word1 = "pig"
    word2 = "sty"
    self = Graph()

    self.create_cluster(word1)
    print(self.tails)


if __name__ == "__main__":
    main()
