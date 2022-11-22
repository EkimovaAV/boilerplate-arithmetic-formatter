import re
def arithmetic_arranger(problems, getanswer=False):
    # too many problems

    if len(problems) > 5:
        return "Error: Too many problems."

    firstNum = ""
    secondNum = ""
    lines = ""
    result = ""
    for item in problems:
            if re.search("[^\s0-9.+-]", item):
                if re.search(["/*"], item) :
                    return "Error: Operator must be '+' or '-'."
                return "Error: Numbers must only contain digits."
    return arranged_problems
