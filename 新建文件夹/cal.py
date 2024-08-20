import sys

def calculate(operation, numbers):
    if operation == 'add':
        return sum(numbers)
    elif operation == 'minus':
        return numbers[0] - sum(numbers[1:])
    elif operation == 'multiply':
        result = 1
        for number in numbers:
            result *= number
        return result
    elif operation == 'divide':
        result = numbers[0]
        for number in numbers[1:]:
            if number == 0:
                return "Error: Division by zero"
            result /= number
        return result
    else:
        return "Error: Unknown operation"

def main():
    if len(sys.argv) < 3:
        print("Usage: cal-<operation> <filename>")
        sys.exit(1)

    operation = sys.argv[1].split('-')[1]
    filename = sys.argv[2]

    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: File '{filename}' contains non-numeric values.")
        sys.exit(1)

    result = calculate(operation, numbers)
    print(result)

if __name__ == '__main__':
    main()