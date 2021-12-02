from subprocess import Popen, PIPE, STDOUT

scores = {}
compile_cmd = "gcc p1.c"
compile_proc = Popen(compile_cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

if 'error:' not in compile_proc.stdout.read().decode():
    scores["Compilation"] = 20
else:
    scores["Compilation"] = 0

exec_cmd = "./a.out"
exec_proc = Popen(exec_cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

if 'Hello World!' in exec_proc.stdout.read().decode():
    scores["Output"] = 30
else:
    scores["Output"] = 0

import json
print(json.dumps({'scores': scores}))
