import re
from threading import Thread

pattern = r'Blueprint (?P<blueprint_id>\d+): Each ore robot costs (?P<ore_ore>\d+) ore\. Each clay robot costs (?P<clay_ore>\d+) ore\. Each obsidian robot costs (?P<obs_core>\d+) ore and (?P<obs_clay>\d+) clay\. Each geode robot costs (?P<geode_ore>\d+) ore and (?P<geode_obs>\d+) obsidian\.'

A_TIME_STEPS = 24
B_TIME_STEPS = 32
A_NUM_OF_WORKERS = 10
B_NUM_OF_WORKERS = 3

def problem(blueprint_id, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs, steps_limit, results):
    robots_costs = {
        "ore": {
            "ore": int(ore_ore)
        },
        "clay": {
            "ore": int(clay_ore)
        },
        "obs": {
            "ore": int(obs_ore),
            "clay": int(obs_clay)
        },
        "geode": {
            "ore": int(geode_ore),
            "obs": int(geode_obs)
        }
    }

    max_ore = max(int(ore_ore), int(clay_ore), int(obs_ore), int(geode_ore))

    def can_build(robot_type, collection):
        for ore_type in robots_costs[robot_type]:
            if robots_costs[robot_type][ore_type] > collection[ore_type]:
                return False
        return True
    
    def build_robot(robot_type, collection, robots):
        new_collection = dict(collection)
        new_robots = dict(robots)
        for ore_type in robots_costs[robot_type]:
            new_collection[ore_type] -= robots_costs[robot_type][ore_type]
        new_robots[robot_type] += 1
        return (new_collection, new_robots)

    def is_profitable(robot_type, collection, robots, step):
        if robot_type == "clay":
            if robots["clay"] + collection["clay"] / (steps_limit - step) >= robots_costs["obs"]["clay"]:
                return False
            return True
        elif robot_type == "ore":
            if robots["ore"] + collection["ore"] / (steps_limit - step) >= max_ore:
                return False
            return True
        else:
            return True
        
    def hash_step(step, robots, collection, to_build, previously_not_builded):
        robots_str = ','.join([str(robots[robot_key]) for robot_key in robots])
        collection_str = ','.join([str(collection[collection_key]) for collection_key in collection])
        prev_not_builded = ','.join(previously_not_builded)
        return '%d_%s_%s_%s_%s' % (step, robots_str, collection_str, to_build, prev_not_builded)

    init_collection = {
        "ore": 0,
        "clay": 0,
        "obs": 0,
        "geode": 0
    }

    init_robots = {
        "ore": 1,
        "clay": 0,
        "obs": 0,
        "geode": 0
    }

    partial_results = {}

    def evaluate(collection, robots):
        new_collection = dict(collection)
        for robot_key in robots:
            new_collection[robot_key] += robots[robot_key]
        return new_collection

    min_value_per_step = [0, 0]

    def solve(collection, robots, step, previously_not_builded):
        step_collection = evaluate(collection, robots)
        if min_value_per_step[0] < step_collection["geode"] and step <= min_value_per_step[1]:
            min_value_per_step[0] = step_collection["geode"]
            min_value_per_step[1] = step
        
        if step - min_value_per_step[1] > 5 and min_value_per_step[0] > step_collection["geode"]:
            return step_collection["geode"]
        if step == steps_limit:
            return step_collection["geode"]
        best_value = step_collection["geode"]
        if not (collection["ore"] >= max_ore and collection["clay"] >= robots_costs["obs"]["clay"] and collection["obs"] >= robots_costs["geode"]["obs"]):
            new_previously_not_builded = []
            for robot_type in ["ore", "clay", "obs", "geode"]:
                if can_build(robot_type, collection):
                    new_previously_not_builded.append(robot_type)
            best_value = solve(step_collection, robots, step + 1, new_previously_not_builded)
        robots_to_try_to_build = ["geode", "obs", "clay", "ore"]
        for robot_type in robots_to_try_to_build:
            if can_build(robot_type, collection) and is_profitable(robot_type, step_collection, robots, step) and robot_type not in previously_not_builded:
                step_robot_hash = hash_step(step, robots, collection, robot_type, previously_not_builded)
                if step_robot_hash in partial_results:
                    build_robot_step_value = partial_results[step_robot_hash]
                else:
                    new_collection, new_robots = build_robot(robot_type, step_collection, robots)
                    build_robot_step_value = solve(new_collection, new_robots, step + 1, [])
                    partial_results[step_robot_hash] = build_robot_step_value
                
                if best_value == None or build_robot_step_value > best_value:
                    best_value = build_robot_step_value
                
        if best_value == None:
            raise ValueError("Best value should not be none at this point")
        return best_value
    
    blueprint_id = int(blueprint_id)
    results[blueprint_id - 1] = solve(init_collection, init_robots, 1, [])


with open('input', 'r') as input_file:
    
    to_process = []
    for line in input_file:
        to_process.append(re.search(pattern, line).groups())
        
    a_results = [None] * len(to_process)
    def get_task_a_next_batch():
        i = 0
        while i < len(to_process) / A_NUM_OF_WORKERS:
            yield to_process[i*A_NUM_OF_WORKERS:(i+1)*A_NUM_OF_WORKERS] 
            i += 1
    for batch in get_task_a_next_batch():
        threads = []
        for task in batch:
            thread = Thread(target=problem, args=(task + (A_TIME_STEPS, a_results,)))
            thread.start()
            threads.append(thread)

        for i in range(len(threads)):
            threads[i].join()
    
    task_a_result = 0
    for r in range(len(to_process)):
        task_a_result += (r+1)*a_results[r]

    # Task A
    print(task_a_result)

    task_b_to_process = to_process[0:3]
    b_results = [None] * 3
    threads = []
    for task in task_b_to_process:
        thread = Thread(target=problem, args=(task + (B_TIME_STEPS, b_results,)))
        thread.start()
        threads.append(thread)
    for i in range(len(threads)):
        threads[i].join()

    # Task B
    print(b_results[0] * b_results[1] * b_results[2])  

