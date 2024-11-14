# This file should provided functionality to
# Submodule2 itself and
# ParentModules that include this submodule2

class SubModule1:
    name: str = "SubModule2"

    def say_hello(self):
        print("Hello, I'm the " + name + ".")

if __name__ == "__main__":
    # Instantiate SubModule2
    sub_module = SubModule2()

    # Hello from all modules
    sub_module.say_hello()
