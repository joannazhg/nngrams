# Welcome to the Nonogram Puzzle Automation read.me

This program contains an implementation of a Nonogram solver using depth-limited depth-first search (DFS) and a genetic algorithm.

# Installation 

# clone the repository
git clone https://github.com/yourusername/NonogramSolver.git

# navigate to the project directory
cd NonogramSolver

# if necessary, install requirements
pip install -r requirements.txt

# Usage
In this project, the solver function in the solver.py script uses a depth-limited DFS to solve the Nonogram. The depth limit can be modified as needed. There's also an implementation of a genetic algorithm for solving Nonogram puzzles in geneticAlgo.py.

Run the main.py script to use the program with default parameters. You can modify the constraints in constraints.py.

Copy code
python main.py
Testing
Run the test.py script for a series of performance tests.

Copy code
python test.py
Explanation of Files
main.py: This file is the main entry point of the program.
solver.py: Contains the depth-limited DFS implementation for solving Nonogram.
geneticAlgo.py: Contains the genetic algorithm implementation for solving Nonogram.
constraints.py: This is where you can define the constraints for the Nonogram puzzle.
heuristic.py: This file is where heuristic functions for the genetic algorithm are defined.
test.py: Contains a series of performance tests.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
MIT
