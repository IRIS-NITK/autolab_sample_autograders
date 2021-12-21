from handin import *
scores = {}

try:
    add_nums
except NameError:
    scores["Output"] = 0
else:
    # Award 5 marks if function exists and matches expected name
    scores["Output"] = 5
    
    # Evaluate on 3 test cases
    # We wrap function calls in 
    # 'try' blocks to prevent errors
    # made by student from causing issues with evaluation script
    try:
        op = add_nums(3, 2)
    except:
        print("Test Case 1 Failed due to runtime error")
    else:
        if op == 5:
            scores["Output"] += 15
        else:
            print("Test Case 1 failed wrong O/P")
    
    try:
        op = add_nums(-20, 54)
    except:
        print("Test Case 2 Failed due to runtime error")
    else:
        if op == 34:
            scores["Output"] += 15
        else:
            print("Test Case 2 failed wrong O/P")


    try:
        op = add_nums(100,  20)
    except:
        print("Test Case 3 Failed due to runtime error")
    else:
        if op == 120:
            scores["Output"] += 15
        else:
            print("Test Case 3 failed wrong O/P")
finally:
    # Return a json string conatining scores of the format
    # { 'scores': {'question_name': marks, 'question_name': marks ...} }
    # Here we use JSON library to convert our python dictionary to JSON
    import json
    print(json.dumps({'scores': scores}))




