# helper function Runs cmd in bash env and returns stdout
def run_bash(cmd):
    from subprocess import Popen, PIPE, STDOUT
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    return p.stdout.read().decode()
                                     

# Empty dictionary to store scores
scores = {}

# Check Files for Syntax errors
import ast, traceback
with open("handin.py") as f:
    source = f.read()
try:
    ast.parse(source)
except SyntaxError:
    print("Syntax Error in Submitted file.")
    scores["Syntax"] = 0
else:
    print("Syntax is valid.")
    scores["Syntax"] = 5




# Initialise the grade
scores["Output"] = 0

# loop over 3 testcases
for i in range(3):
    
    # Run program by streaming input from file to SDTIN
    # file named input-[0, 1, 2].txt contains 1st 2nd and 3rd testcases
    submited_op = run_bash("python3 handin.py<input-%d.txt" % i).strip(' \n\t\r')
    expected_op = run_bash("python3 soln.py<input-%d.txt" % i).strip(' \n\t\r')
    
    # Print the Program output to STDOUT
    print("Program OP")
    print(submited_op)
    
    # Print the Expected output to STDOUT
    print("Expected) O/P")
    print(expected_op)

    # Compare the contents of expected output and submission output 
    # and give marks
    # Give 15 marks per correct answer
    if submited_op == expected_op:
        print("  ** Test Case %d Passed ** \n\n" % i)
        scores["Output"] += 15

import json

# Return a json string conatining scores of the format
# { 'scores': {'question_name': marks, 'question_name': marks ...} }
# Here we use JSON library to convert our python dictionary to JSON
print(json.dumps({'scores': scores}))
