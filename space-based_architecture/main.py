from space_based_architecture import DataGrid, ProcessingUnit, LoadBalancer
import multiprocessing
import random


def simulate_space_based_architecture():
    data_size = 10
    num_nodes = 3

    data_grid = DataGrid(data_size)
    task_queue = multiprocessing.Queue()

    # create processing units (nodes)
    nodes = [ProcessingUnit(i, data_grid, task_queue) for i in range(num_nodes)]

    for node in nodes:
        node.start()

    load_balancer = LoadBalancer(num_nodes, task_queue)

    # simulate processing 10 tasks
    for _ in range(10):
        index = random.randint(0, data_size - 1)
        load_balancer.distribute_task(index)

    for _ in range(num_nodes):
        task_queue.put(None)

    for node in nodes:
        node.join()


if __name__ == "__main__":
    simulate_space_based_architecture()
