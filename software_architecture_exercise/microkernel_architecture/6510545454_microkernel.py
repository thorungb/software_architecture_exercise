class Microkernel:
    def __init__(self):
        self.plugins = {}  # to collect plugins

    def load_plugin(self, name, plugin):
        self.plugins[name] = plugin  # to add new plugin

    def run_plugin(self, name, a, b):
        if name in self.plugins:
            return self.plugins[name](a, b)  # to run plugin
        return f"Plugin '{name}' not found."

    def unload_plugin(self, name):
        self.plugins.pop(name, None)  # to remove plugin

# create plugin
def plugin_add(a, b):
    return a + b

def plugin_multiply(a, b):
    return a * b

def plugin_subtract(a, b):
    return a - b

def plugin_divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"


if __name__ == "__main__":
    kernel = Microkernel()
    # load plugins
    kernel.load_plugin("add", plugin_add)
    kernel.load_plugin("multiply", plugin_multiply)
    kernel.load_plugin("subtract", plugin_subtract)
    kernel.load_plugin("divide", plugin_divide)
    # use plugins
    print("Adding 10 and 5:", kernel.run_plugin("add", 10, 5))
    print("Multiplying 10 and 5:", kernel.run_plugin("multiply", 10, 5))
    print("Subtracting 10 from 5:", kernel.run_plugin("subtract", 5, 10))
    print("Dividing 10 by 5:", kernel.run_plugin("divide", 10, 5))
    # remove a plugin, and use it again
    kernel.unload_plugin("add")
    kernel.unload_plugin("multiply")
    kernel.unload_plugin("subtract")
    kernel.unload_plugin("divide")
    print("--------------------------------------")
    print("Running 'add' plugin after unloading:", kernel.run_plugin("add", 10, 5))
    print("Running 'multiply' plugin after unloading:", kernel.run_plugin("multiply", 10, 5))
    print("Running 'subtract' plugin after unloading:", kernel.run_plugin("subtract", 5, 10))
    print("Running 'divide' plugin after unloading:", kernel.run_plugin("divide", 10, 5))
