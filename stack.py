# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.

class Stack:
    def __init__(self, capacity) -> None:
        self.stack = []
        #для 2 задания убрать поле
        self.capacity = capacity

    def push(self, value):
        #для 2 задания убрать проверку
        if len(self.stack) < self.capacity:
            if isinstance(value, str):
                self.stack.append(value)
            else:
                raise ValueError("Incorrect value")
        else:
            raise Exception("stack is full")
    
    def pop(self):
        if self.stack:
            item = self.stack.pop()
            return item
        else:
            print("stack is already clear")
            return None
        
    def length(self):
        return len(self.stack)
    
    def isEmpty(self):
        return not bool(self.stack)
    
    # для 2 задания убрать функцию
    def isFull(self):
        return len(self.stack) == self.capacity
    
    def clear(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

stack_capacity = 5
stack = Stack(stack_capacity)
for i in range(stack_capacity):
    stack.push(str(i))

print(stack.peek())

print(stack.peek())
print(stack.isEmpty())
print(stack.isFull())
stack.clear()
print(stack.peek())