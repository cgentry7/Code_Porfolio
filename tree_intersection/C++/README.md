# Tree Intersection

A C++ code for performing a basic tree intersection as part of a coding challenge problem

Version / Module Requirements
-----------------------------
- CMake Version 3.10 (minimum required)
- C++ 14 Standard (GNU Compiler)

User Instructions
------------------
To build the program from the tree_intersection root directory, execute the following:
```
cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug -G "Unix Makefiles"
make all
```

For command line execution, the user may call the main program `tree_intersection` along with an input file:
```
<tree_intersection_dir>/build/source/tree_intersection <input_file>
```

To run the unit & verification tests, simply execute the following:
```
<tree_intersection_dir>/build/tests/tree_intersection_tst
```

To Do
-------
- The CMake is a messy and doesn't update the main executable.  Need to fix.
- The verification test file comparison is kludgy, need to clean.
- Need to implement a const accessor to children if possible
