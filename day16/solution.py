import re

class Node:
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = []
    def add_connection(self, node):
        self.connections.append(node)

class PartialSolution:
    def __init__(self, node, opened_valves, came_from, solution_value):
        self.node = node
        self.opened_valves = opened_valves
        self.came_from = came_from
        self.solution_value = solution_value

nodes = []
flow_rate_dict = {}
distances = {}

steps = 30

pattern = r'Valve (?P<name>.+) has flow rate=(?P<flow_rate>\d+); tunnels? leads? to valves? (?P<connections>.+)'

with open('input', 'r') as input_file:
    for line in input_file:
        re_resut = re.search(pattern, line)
        [name, flow_rate, connections] = re_resut.groups()
        flow_rate = int(flow_rate)
        connections = [connection.strip() for connection in connections.split(',')]
        new_node = Node(name, flow_rate)
        nodes.append(new_node)
        flow_rate_dict[name] = flow_rate
        for connection in connections:
            for node in nodes:
                if node.name == connection:
                    node.add_connection(new_node)
                    new_node.add_connection(node)

    distances_to_calculate = []
    for node in nodes:
        distances[node.name] = {node.name: 0}
        for connection in node.connections:
            distances_to_calculate.append([node, connection])

    
    i = 1
    while distances_to_calculate:
        current_distances_to_calcuate = distances_to_calculate[:]
        distances_to_calculate = []
        for [src_node, target_node] in current_distances_to_calcuate:
            if target_node.name not in distances[src_node.name].keys():
                distances[src_node.name][target_node.name] = i
                for connection in target_node.connections:
                    distances_to_calculate.append([src_node, connection])
        i += 1

    # def find_shortest_paths(curr):
    #     dists = {}
    #     prevs = {}
    #     for n in nodes:
    #         dists[n.name] = 999
    #         prevs[n.name] = None
    #     dists[curr.name] = 0
    #     Q = nodes[:]
    #     while len(Q) > 0:
    #         u = Q[0]
    #         for n in Q:
    #             if dists[n.name] < dists[u.name]:
    #                 u = n
    #         Q.remove(u)
    #         for v in u.connections:
    #             if dists[v.name] > dists[u.name] + 1:
    #                 dists[v.name] = dists[u.name] + 1
    #                 prevs[v.name] = u
        
    #     return prevs

    # paths = {}
    # for node in nodes:
    #     paths[node.name] = find_shortest_paths(node)

    to_visit_all = [node for node in nodes if node.flow_rate > 0]
    # to_visit_all = [nodes[1], nodes[2], nodes[3]]

    current_node = None
    for node in nodes:
        if node.name == 'AA':
            current_node = node
            break
    
    bests = []

    best_depth = 0
    best_traversed = []
    best_route = 0
    route_values = []

    def calc_route_value(route):
        route_value = 0
        for node in route:
            route_value += node[0].flow_rate * (steps - node[1])
        route_values.append(route_value)
        return route_value

    def traverse(current, to_visit, traversed, depth = 0):
        global best_traversed
        global best_depth
        global best_route
        if len(to_visit) == 0 or depth == steps:
            route_value = calc_route_value(traversed)
            if route_value > best_route:
                best_route = route_value
                best_traversed = traversed
        for next_node in to_visit:
            traverse_cost = distances[current.name][next_node.name]
            if depth + traverse_cost > steps:
                continue
            new_to_visit = to_visit[:]
            new_to_visit.remove(next_node)
            new_traversed = traversed[:]
            new_traversed.append([next_node, depth + traverse_cost + 1])
            traverse(next_node, new_to_visit, new_traversed, depth + traverse_cost + 1)
    
    result = traverse(current_node, to_visit_all, [], 0)
    # print(best_route)
    # print([node[0].name for node in best_traversed])
    # print([node[0].flow_rate for node in best_traversed])
    # print([node[1] + 1 for node in best_traversed])

    
    print(best_route)
    
    #print(result)
    # closed_nodes = [node for node in nodes]
    # opened_nodes = []



    # def find_best_cost(curr, i):
    #     best_node = None
    #     best_cost = -1
    #     for node in closed_nodes:
    #         cost = (steps - (i + distances[curr.name][node.name])) * (node.flow_rate - distances[curr.name][node.name])
    #         if cost > best_cost and cost > 0:
    #             best_node = node
    #             best_cost = cost
    #     return best_node

    # current_solution = 0
    # current_solution_value = 0
    # current_node = None
    # for node in nodes:
    #     if node.name == 'AA':
    #         current_node = node
    #         break
    
    # path = []
    # target_node = None
    # target_node = find_best_cost(current_node, i)
    # paths = find_shortest_paths(current_node)
    # next_node = target_node
    # for i in range(steps + 1):
    #     current_solution += current_solution_value
    #     if next_node == None:
    #         continue
    #     if next_node == current_node:
    #         current_node = target_node
    #     if current_node == target_node:
    #         closed_nodes.remove(current_node)
    #         current_solution_value += current_node.flow_rate
    #         target_node = find_best_cost(current_node, i)
    #         next_node = target_node
    #         paths = find_shortest_paths(current_node)
    #         path.append(current_node)
    #         opened_nodes.append(current_node)
    #         new_node = None
    #     else:
    #         next_node = paths[next_node.name]
    #     # print(str(i + 1) + ' ' + str(current_solution) + ' : ' + ', '.join([node.name for node in opened_nodes]))

    
    # print(current_solution)

        
    # best_solution = None
    # initial = PartialSolution(start_node, [], [], 0)
    # partial_solutions = [initial]
    # best_solution = initial

    # def shortest_path(node):


    # for i in range(0, 30):
    #     new_partial_solutions = []
    #     for partial_solution in partial_solutions:
    #         step_value = partial_solution.solution_value + sum([node.flow_rate for node in partial_solution.opened_valves])
    #         did_anything = False
    #         if partial_solution.node not in partial_solution.opened_valves and partial_solution.node.flow_rate > 0:
    #             opened_valves = partial_solution.opened_valves[:] + [partial_solution.node]
    #             valve_value = partial_solution.node.flow_rate
    #             sol = PartialSolution(partial_solution.node, opened_valves, partial_solution.came_from, step_value)
    #             new_partial_solutions.append(sol)
    #             did_anything = True
    #         else:
    #             came_from = partial_solution.came_from
    #             for connection in partial_solution.node.connections:
    #                 came_from_value_for_connection = partial_solution.node.name + ' -> ' + connection.name
    #                 if came_from_value_for_connection not in came_from:
    #                     new_came_from = came_from[:] + [came_from_value_for_connection]
    #                     sol = PartialSolution(connection, partial_solution.opened_valves, new_came_from, step_value)
    #                     new_partial_solutions.append(sol)
    #                     did_anything = True
    #         if not did_anything:
    #             sol = PartialSolution(partial_solution.node, partial_solution.opened_valves, partial_solution.came_from, step_value)
    #             new_partial_solutions.append(sol)

    #     for sol in partial_solutions:
    #         if best_solution.solution_value < sol.solution_value:    
    #             best_solution = sol
    #     opened_valves = [node.name for node in best_solution.opened_valves]
    #     opened_valves.sort()
    #     print('%d => %d, [%s]' % (i, best_solution.solution_value, ', '.join(opened_valves)))
    #     partial_solutions = new_partial_solutions


    # # Task A
    # for v in best_solution.opened_valves:
    #     print(v.name)
    # print(best_solution.solution_value)