import re
from threading import Thread

pattern = r'Blueprint (?P<blueprint_id>\d+): Each ore robot costs (?P<ore_ore>\d+) ore\. Each clay robot costs (?P<clay_ore>\d+) ore\. Each obsidian robot costs (?P<obs_core>\d+) ore and (?P<obs_clay>\d+) clay\. Each geode robot costs (?P<geode_ore>\d+) ore and (?P<geode_obs>\d+) obsidian\.'

TIME_STEPS = 24
NUM_OF_WORKERS = 10

def problem(blueprint_id, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs, results):
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
        # if robot_type == "clay":
        #     return (TIME_STEPS - step) * (robots["clay"] + 1) + collection["clay"] > robots_costs["obs"]["clay"]
        # elif robot_type == "obs":
        #     return (TIME_STEPS - step) * (robots["obs"] + 1) + collection["obs"] > robots_costs["geode"]["obs"]
        # elif step < TIME_STEPS:
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

    max_value_and_step = [0, 0]

    def solve(collection, robots, step, previously_not_builded):
        step_collection = evaluate(collection, robots)
        if max_value_and_step[0] < step_collection["geode"] and step <= max_value_and_step[1]:
            max_value_and_step[0] = step_collection["geode"]
            max_value_and_step[1] = step
        
        if step - max_value_and_step[1] > 5 and max_value_and_step[0] > step_collection["geode"]:
            return step_collection["geode"]
        if step == TIME_STEPS:
            return step_collection["geode"]
        best_value = None
        if collection["ore"] >= max_ore and collection["clay"] >= robots_costs["obs"]["clay"] and collection["obs"] >= robots_costs["geode"]["obs"]:
            pass
        else:
            new_previously_not_builded = []
            for robot_type in ["ore", "clay", "obs", "geode"]:
                if can_build(robot_type, collection):
                    new_previously_not_builded.append(robot_type)
            best_value = solve(step_collection, robots, step + 1, new_previously_not_builded)
        for robot_type in reversed(["ore", "clay", "obs", "geode"]):
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
                    # break
                
        if best_value == None:
            print(step_collection)
            print(robots_costs)
            raise ValueError("Best value should not be none at this point")
        return best_value
    
    blueprint_id = int(blueprint_id)
    results[blueprint_id - 1] = solve(init_collection, init_robots, 1, [])


with open('input', 'r') as input_file:
    
    to_process = []
    for line in input_file:
        to_process.append(re.search(pattern, line).groups())
        
    results = [None] * len(to_process)
    def get_next_batch():
        i = 0
        while i < len(to_process) / NUM_OF_WORKERS:
            yield to_process[i*NUM_OF_WORKERS:(i+1)*NUM_OF_WORKERS] 
            i += 1

    for batch in get_next_batch():
        threads = []
        for task in batch:
            thread = Thread(target=problem, args=(task + (results,)))
            thread.start()
            threads.append(thread)

        print("Waiting for %s" % (', '.join([task[0] for task in batch])))
        for i in range(len(threads)):
            threads[i].join()
    
    task_a_result = 0
    for r in range(len(to_process)):
        task_a_result += (r+1)*results[r]
    
    # Task A
    print(task_a_result)
    print(results)