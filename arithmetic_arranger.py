MAX_OPERAND_SIZE = 4

def arithmetic_arranger(problems, is_solve=False):

    result = ""
    problems_size = len(problems)
    if problems_size <= 5:
      operands = []
      operator = [] 

      for problem in problems:
        splitted_problem = problem.split()
        unverified_operands = [splitted_problem[0], splitted_problem[2]]
        is_valid, result = validate_problem(unverified_operands, splitted_problem[1])

        if is_valid == True:
          operands.append(unverified_operands)
          operator.append(splitted_problem[1])
        else:
          break      
    else:
      result = "Error: Too many problems."

    return result

def validate_problem(operands, operator):

  is_valid = True
  result = ""

  for operand in operands:
    if len(operand) > MAX_OPERAND_SIZE:
      result = "Error: Numbers cannot be more than four digits."
      is_valid = False
      break
    elif operand.isdigit() == False:
      result = "Error: Numbers must only contain digits."
      is_valid = False
      break

  if is_valid and operator != "+" and operator != "-":
    is_valid = False
    result = "Error: Operator must be '+' or '-'."

  return is_valid, result