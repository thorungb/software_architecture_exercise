import multiprocessing
import random
import time


class DataGrid:
    def __init__(self, size):
        self.size = size
        self.shared_memory = multiprocessing.Array('i', [random.randint(1, 10) for _ in range(size)])

    def read_data(self, index):
        return self.shared_memory[index]

    def write_data(self, index, value):
        self.shared_memory[index] = value


class ProcessingUnit(multiprocessing.Process):
    def __init__(self, id, data_grid, task_queue):
        super().__init__()
        self.id = id
        self.data_grid = data_grid
        self.task_queue = task_queue

    def run(self):
        while True:
            index = self.task_queue.get()
            if index is None:
                break

            old_value = self.data_grid.read_data(index)
            new_value = old_value + random.randint(5, 10)
            self.data_grid.write_data(index, new_value)
            print(f"Node {self.id} processing data at index {index}: {old_value} -> {new_value}")
            time.sleep(random.uniform(0.5, 1.5))


class LoadBalancer:
    def __init__(self, num_nodes, task_queue):
        self.num_nodes = num_nodes
        self.task_queue = task_queue
        self.current_node = 0

    def distribute_task(self, index):
        self.task_queue.put(index)
        self.current_node = (self.current_node + 1) % self.num_nodes
