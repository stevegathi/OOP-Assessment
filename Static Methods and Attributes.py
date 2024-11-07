class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Demonstration
result1 = Calculator.add(5, 10)
result2 = Calculator.add(3, 7)
print("Addition Results:", result1, result2)
print("Add method called:", Calculator.count, "times")