import re

pattern = r'Valve (?P<name>.+) has flow rate=(?P<flow_rate>\d+); tunnels? leads? to valves? (?P<connections>.+)'    

class Node:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections

nodes = dict()
distances = dict()

A_steps = 30
B_steps = 26

def dijkstra(node):
    dist = {}
    infinity = 9999
    Q = []
    for n in nodes:
        dist[n] = infinity
        Q.append(n)
    dist[node.name] = 0

    while True:
        if len(Q) == 0:
            return dist
        
        u = None
        for q in Q:
            if u == None:
                u = q
                continue
            if dist[q] < dist[u]:
                u = q
        Q.remove(u)

        for c in nodes[u].connections:
            if c not in Q:
                continue
            alt = dist[u] + 1
            if alt < dist[c]:
                dist[c] = alt

with open('input', 'r') as input:
    for line in input:
        re_resut = re.search(pattern, line)
        [name, flow_rate, connections] = re_resut.groups()
        flow_rate = int(flow_rate)
        connections = [connection.strip() for connection in connections.split(',')]
        new_node = Node(name, flow_rate, connections)
        nodes[name] = new_node

    for node_name in nodes:
        distances[node_name] = dijkstra(nodes[node_name])
        
    current_node = nodes['AA']

    worth_visiting = [nodes[node_name] for node_name in nodes if nodes[node_name].flow_rate > 0]
    valve_status = []

    def traverse(current, step_value, total, step, max_steps):
        global worth_visiting
        if step == max_steps:
            return (total, None)
        best = total + step_value * (max_steps - step)
        iter_worth_visiting = worth_visiting[:]
        best_to_visit_path = []
        child_best_to_visit_path = None
        best_to_visit = None
        for to_visit in iter_worth_visiting:
            distance = distances[current.name][to_visit.name]
            if step + distance + 1 > max_steps:
                continue
            worth_visiting.remove(to_visit)
            visit_value, child_to_visit_path = traverse(to_visit, step_value + to_visit.flow_rate, total + step_value * (distance + 1), step + distance + 1, max_steps)
            worth_visiting.append(to_visit)
            if visit_value > best:
                best = visit_value
                best_to_visit = to_visit
                child_best_to_visit_path = child_to_visit_path

        if best_to_visit != None:
            best_to_visit_path.append(best_to_visit)
        if child_best_to_visit_path != None:
            best_to_visit_path.extend(child_best_to_visit_path)
        return (best, best_to_visit_path)

    task_a_result, _ = traverse(current_node, 0, 0, 0, A_steps)
    task_b_result, task_b_result_path = traverse(current_node, 0, 0, 0, B_steps)
    for it in task_b_result_path: # ! Works only as long as you & elephant visit and open at most all non-zero flow rate nodes - otherwise elephant "waits" idle which won't give best solution (see sample data for this task)
        worth_visiting.remove(it)
    el_task_b_result, el_task_b_result_path = traverse(current_node, 0, 0, 0, B_steps)

    # Task A
    print(task_a_result)

    # Task B
    print(task_b_result + el_task_b_result)