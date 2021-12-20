# helper function Runs cmd in bash env and returns stdout
def run_bash(cmd):
    from subprocess import Popen, PIPE, STDOUT
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    return p.stdout.read().decode()
                                     

# Empty dictionary to store scores
scores = {}

# compile submission and grade for compilation
if 'error:' not in run_bash("gcc handin.c"):
    scores["Compilation"] = 5
else:
    scores["Compilation"] = 0

# Compile solution(editorial) program
run_bash("gcc soln.c -o soln")

# Grade Submission
scores["Output"] = 0

# loop over 3 testcases
for i in range(3):
    
    # Run program by streaming input from file to SDTIN
    # file named input-[0, 1, 2].txt contains 1st 2nd and 3rd testcases
    submited_op = run_bash("./a.out <input-%d.txt" % i).strip(' \n\t\r')
    expected_op = run_bash("./soln <input-%d.txt" % i).strip(' \n\t\r')
    print("Program OP")
    print(submited_op)
    
    print("Expected) O/P")
    print(expected_op)

    # Compare the contents of expected output and submission output 
    # and give marks
    if submited_op == expected_op:
        print("  ** Test Case %d Passed ** \n\n" % i)
        scores["Output"] += 15

import json

# Return a json string conatining scores of the format
# { 'scores': {'question_name': marks, 'question_name': marks ...} }
# Here we use JSON library to convert our python dictionary to JSON
print(json.dumps({'scores': scores}))
