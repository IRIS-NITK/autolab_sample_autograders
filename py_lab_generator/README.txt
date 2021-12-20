# About lab
 - Creates a lab which runs students submission and compares its output with that of 'soln.py'
 - Input to program is given by storing it across 3 files input-{0..2}.txt
 - 5 marks are awarded for compilation
 - 15 marks are awarded for matching output on each testcase file

# How to use C Lab generator

 1. Install Make(if not already installed)
   `sudo apt-get -y install make`

 2. Run 'make clean' to remove all stale files from old labs

 3. Create a file 'soln.py' with expected solution

 4. Store input testcases across the 3 textfiles, input-0.txt, input-1.txt, input-2.txt

 5. [Optional] Make any changes to evaluation_script.py/autograder-Makefile

 6. execute make by running the 'make' in the py_lab_generator directory, this will create the autograder-Makefile and autograde.tar file

 7. upload the files on Autolab


