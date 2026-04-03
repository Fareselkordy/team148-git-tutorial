# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    """Compute the result of a simple arithmetic expression string."""
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    print('unknown operator!')
    return None

expression = input("Enter an expression (e.g. 5 + 8): ")
result = compute(expression)
if result is not None:
    print(f"Result: {result}")
