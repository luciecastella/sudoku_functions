# Functions for a sudoku solver

Copyright 2020 Lucie Castella

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Here are the basic functions (slightly modified) I used a few weeks ago in algorithms I needed to implement to solve sudokus (9x9). This was made for the course "Problem Solving and Search in Artificial Intelligence" at the TU Wien. 

The aim of those 3 functions is to check that a specific number can be added in a cell. 
The functions check that the number in a particular cell (position i,j in the grid 9x9) is not in conflict with other number -> one function to check the 3x3 sub-square, one for the line, one for the column.
