from .base import BaseTask
class Fibonacci0(BaseTask):
    def __init__(self):
        super().__init__(taskID=208, taskName='Fibonacci0')
    def exec(self, inputData):
        n = inputData['n']
        print(inputData)
        if n < 0:
            print("incorrect input")
            return 0
        
        a = 0
        b = 1
        result = []

        for _ in range(n):
            result.append(b)
            a, b = b, a + b

        inputData['result'] = result
        return inputData