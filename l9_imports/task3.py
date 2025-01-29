import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# Import the function `multiply` from `l2_functions` module
# to make the script work without errors
from l2_functions.task6 import multiply

# Do not modify the code below
if __name__ == "__main__":
    assert multiply(2, 2) == 4