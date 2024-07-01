from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Move all elements except the last one to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Pop the last element from q1
        result = self.q1.popleft()
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        # Move all elements except the last one to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Get the last element
        result = self.q1[0]
        # Move it to q2
        self.q2.append(self.q1.popleft())
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        return not self.q1

# Example usage:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())  # Output: 2
# print(obj.pop())  # Output: 2
# print(obj.empty())  # Output: False
