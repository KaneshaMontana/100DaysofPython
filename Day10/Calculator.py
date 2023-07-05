from art.py import logo 

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Pick the first number
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  should_continue = True

while should_continue:
  operation_symbol = input("Pick an operation: ") 
  next_num = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, next_num)
  
  print(f"{num1} {operation_symbol} {next_num} = {answer}")
  
  continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' for a new calculation.: ")
  if continue_calculation == 'y':
    should_continue = True
    num1 = answer
  elif continue_calculation == 'n':
    should_continue = False
    print(f"Your final answer is {answer} ")
    calculator()

calculator()
