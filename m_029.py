from rich import print


class Jar:
    capacity: int

    def __init__(self, capacity: int):
        self.capacity = capacity

    def __repr__(self):
        return f"Jar: {self.capacity}"


class JarState:
    state: dict[Jar, int]
    neighbors: dict["str", "JarState"]

    def __init__(self, _state):
        self.state = _state
        self.neighbors = {}

    def __repr__(self):
        return "_".join(map(str, self.state.values()))

    def __eq__(self, other):
        return self.state == other.state

    @staticmethod
    def key(state):
        return str(state)


class Route:
    start: JarState
    end: JarState
    title: str

    def __init__(self, start, end, title):
        self.start = start
        self.end = end
        self.title = title

    def __repr__(self):
        return f"{self.start} ---{self.title}--- {self.end}"


class Graph:
    def __init__(self):
        pass

    def find_best_route(self, cap_1, cap_2, cap):
        jar_1 = Jar(cap_1)
        jar_2 = Jar(cap_2)

        state = JarState({jar_1: 0, jar_2: 0})
        todo_list = [state]
        checklist = set()
        routes = []
        all_states = {JarState.key(state.state): state}

        while len(todo_list) != 0:

            state = todo_list.pop(0)
            if JarState.key(state) in checklist:
                continue

            new_state, title = self.fill_one_jar(all_states, state, jar_1, "1")
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            new_state, title = self.fill_one_jar(all_states, state, jar_2, "2")
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            new_state, title = self.fill_from_jar_to_another_jar(
                all_states, state, jar_1, jar_2, "1_2"
            )
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            new_state, title = self.fill_from_jar_to_another_jar(
                all_states, state, jar_2, jar_1, "2_1"
            )
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            new_state, title = self.empty_jar(all_states, state, jar_1, "1")
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            new_state, title = self.empty_jar(all_states, state, jar_2, "2")
            if state != new_state:
                self.add_to_neighbors(state, new_state, title)
                self.add_to_todo_list(new_state, todo_list, checklist)
                self.add_to_routes(routes, state, new_state, title)
            if any(v == cap for v in new_state.state.values()):
                return routes

            checklist.add(JarState.key(state))

    def add_to_todo_list(self, new_state, todo_list, checklist):
        if JarState.key(new_state) not in checklist:
            todo_list.append(new_state)

    def add_to_routes(self, routes, state, new_state, title):
        # FIXME: maybe previous route has less route length!
        # previous_checked = [r for r in routes for _r in r if _r.start == new_state]
        # if previous_checked:
        #     return

        found_routes = [r for r in routes if r[-1].end == state]
        if found_routes:
            for r in found_routes:
                routes.append([*r, Route(state, new_state, title)])
        else:
            routes.append([Route(state, new_state, title)])

    def add_to_neighbors(self, state, new_state, title):
        if title not in state.neighbors:
            state.neighbors[title] = new_state

    def fill_one_jar(self, all_states, state, jar, extra_title):
        title = f"fill_one_jar_{extra_title}"
        current = state.state[jar]
        after_fill = min(current + jar.capacity, jar.capacity)
        new_state_dict = state.state | {jar: after_fill}

        key = JarState.key(new_state_dict)
        if key in all_states:
            return all_states[key], title
        return all_states.setdefault(key, JarState(new_state_dict)), title

    def fill_from_jar_to_another_jar(
        self, all_states, state, jar_1, jar_2, extra_title
    ):
        title = f"fill_from_jar_to_another_jar_{extra_title}"
        current_1 = state.state[jar_1]
        current_2 = state.state[jar_2]

        empty_space_2 = jar_2.capacity - current_2
        transfer = min(current_1, empty_space_2)

        after_1 = current_1 - transfer
        after_2 = current_2 + transfer

        new_state_dict = state.state | {jar_1: after_1, jar_2: after_2}
        key = JarState.key(new_state_dict)
        if key in all_states:
            return all_states[key], title
        return all_states.setdefault(key, JarState(new_state_dict)), title

    def empty_jar(self, all_states, state, jar, extra_title):
        title = f"empty_jar_{extra_title}"

        new_state_dict = state.state | {jar: 0}
        key = JarState.key(new_state_dict)
        if key in all_states:
            return all_states[key], title
        return all_states.setdefault(key, JarState(new_state_dict)), title


def main():
    def check(r, cap):
        return any(x == cap for x in r[-1].end.state.values())

    self = Graph()
    jar_1_cap = 4
    jar_2_cap = 21
    cap = 3
    routes = self.find_best_route(jar_1_cap, jar_2_cap, cap)
    routes = sorted(
        [r for r in routes if check(r, cap)], key=lambda r: len(r), reverse=True
    )
    print(routes)


if __name__ == "__main__":
    main()
