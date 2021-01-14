MAX_OPERAND_SIZE = 4

def arithmetic_arranger(problems, is_solve=False):

    result = ""
    problems_size = len(problems)
    if problems_size <= 5:
      num_line = ""
      den_line = ""
      sep_line = "" 

      for i, problem in enumerate(problems):
        splitted_problem = problem.split()
        operands = [splitted_problem[0], splitted_problem[2]]
        is_valid, result = validate_problem(operands, splitted_problem[1])

        if is_valid == True:
          line_length = get_line_length(operands)
          num_line = num_line + operands[0].rjust(line_length)
          den_line = den_line + splitted_problem[1] + " " + operands[1].rjust(line_length-2)
          for j in range(line_length):
            sep_line = sep_line + "-"

          if i < (problems_size-1):
            num_line = num_line + "    "
            den_line = den_line + "    "
            sep_line = sep_line + "    "

        else:
          break
      
      if is_valid == True:
        result = num_line + "\n" + den_line + "\n" + sep_line

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

def get_line_length(operands):
  line_length = 0
  for operand in operands:
    if len(operand) > line_length:
      line_length = len(operand)

  return line_length+2 #give space for the operator and space