import re
def arithmetic_arranger(problems, getanswer=False):
    # too many problems
    arranged_problems=''
    if len(problems) > 5:
        return "Error: Too many problems."

    firstNum = ""
    secondNum = ""

    oneline=''
    secondline=''
    poloski=''
    answer=''
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
                if len(leftOper) >=len(rightOper):
                    length=len(leftOper)-len(rightOper)
                    lines=len(leftOper)
                    #разница между 1 и 2 оператором?
                    oneline += f"  {leftOper}    "
                    secondline +=  f"{operator}"+ (length)*' '+' ' +(rightOper)+"    "
                    poloski+=lines*'-'+'--    '
                else:
                    length=len(rightOper)-len(leftOper)
                    lines=len(rightOper)
                    oneline+=(length)*' '+ f"  {leftOper}    "
                    secondline+=f"{operator} {rightOper}    "
                    poloski+=lines*'-'+'--    '

    arranged_problems+= oneline+"\n"+secondline+"\n"+poloski
    return arranged_problems
