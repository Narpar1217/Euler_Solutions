
**********************
* ~~ GENERAL INFO ~~ *
**********************

In this repository are my solutions to select problems from Project Euler.
Project Euler "is a website dedicated to a series of computational problems 
intended to be solved with computer programs" (from Wikipedia). 
The goal is to write a program for each problem, in any language, 
that solves it in less than one minute. 
More info about Project Euler is available at http://projecteuler.net

My personal goal is to solve each problem completely, 
i.e. with a solution being at minimum extremely highly probable, but 
ideally guaranteed, in under 1 second. My progress toward this goal
can be seen in Last_run.txt, contained in the same directory as this Readme.

As of 4/6/2013 I have solved 40 out of 421 problems, mostly in Python.
More solutions will be added here as they are reviewed, and as time permits.


**********************
* ~ INCLUDED FILES ~ *
**********************

Root directory:
  * This Readme
  * Last_run.txt
	The output of the last batch run of all solutions.
	For each problem, <WARNING> the answer </WARNING> and 
	the execution time are provided.

'src' directory:
  * Prob#.py (or .c, etc.)
	These are the source files for the solutions, 
	where # is the number of the problem as listed at
	http://projecteuler.net/problems

  * EulerUtility.py
	Any functions that are used in multiple solutions
	are located here.
  
  * CreateBatch_RunAll.py
	Running this script will create a batch file
	named run_all.bat that runs all solutions 
	and overwrites Last_run.txt.

'res' directory:
  * The files here are used by the problem(s) referenced in their filenames. 
    The data contained in them always comes from the problem statements
    as seen at http://projecteuler.net/problems 


**********************
* ~~~~~~ LEGAL ~~~~~ *
**********************

All code herein
Copyright (C) 2013 Adam Beagle - All Rights Reserved

You may use, distribute, and modify this code under the 
terms of the GNU General Public License, 
viewable at http://opensource.org/licenses/GPL-3.0

Please give credit to the author if you use any code
contained in this repository.
