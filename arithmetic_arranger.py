import re
def arithmetic_arranger(problems, getanswer=False):
    # too many problems
    arranged_problems=''
    if len(problems) > 5:
        return "Error: Too many problems."

    firstNum = ""
    secondNum = ""

    
    for i in range(len(problems)):
            if re.search("[^\s0-9.+-]", problems[i]):
                if re.search(["/*"], problems[i]) :
                    return "Error: Operator must be '+' or '-'."
                return "Error: Numbers must only contain digits."

            k=problems[i].split()
            leftOper = k[0]
            rightOper = k[2]
            operator = k[1]
            if len(leftOper) > 4 or len(rightOper) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if leftOper >rightOper:
                    length=len(leftOper)-len(rightOper)
                    lines=len(leftOper)
                    #разница между 1 и 2 оператором?
                else:
                    length=len(rightOper)-len(leftOper)
                    lines=len(rightOper)
                    arranged_problems+= (length)*' '+ f" {leftOper}   \n{operator} {rightOper}    \n"+lines*'-'+'--    '
    return arranged_problems
