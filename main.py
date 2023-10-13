#Task_1
class Task1:
    
    def revers(self, input_word):
        if len(input_word) == 0:
            return
        else:
            print(input_word[-1], end='')
            self.revers(input_word[:-1])


#Task_2
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head and head.next:
        first_node = head
        second_node = head.next

        first_node.next = second_node.next
        second_node.next = first_node
        prev.next = second_node

        prev = first_node
        head = first_node.next

    return dummy.next

def create_linked_list(nodes):
    if not nodes:
        return None

    head = ListNode(nodes[0])
    current = head
    for val in nodes[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
        
        
#Task_3
class Task3:
    
    def __init__(self):
        self.result_arr = {}

    def calculate(self, n):
        if n in self.result_arr:
            return self.result_arr[n]

        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.calculate(n - 1) + self.calculate(n - 2)

        self.result_arr[n] = result
        return result
    
    
#Task_4
class Task4:
    def __init__(self):
        self.memo = {}  # Словник для збереження обчислених значень

    def countWays(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 1:
            result = 1
        elif n == 2:
            result = 2
        else:
            result = self.countWays(n - 1) + self.countWays(n - 2)

        self.memo[n] = result  # Зберігаємо результат в словарі
        return result
    
    
#Task_5
class Task5:
    def calculate_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.calculate_pow(x, -n)
        else:
            half = self.calculate_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

     

if __name__ == "__main__":
    print('Task N1:')
    task1 = Task1()
    task1.revers(input('Слово:'))
    
    print('\n\nTask N2:')
    input_list = input("Введіть числа через пробіл: ").split()
    input_list = [int(val) for val in input_list]
    head = create_linked_list(input_list)
    result_head = swapPairs(head)
    print_linked_list(result_head)
    
    print('\n\nTask N3:')
    n = int(input("Введіть число n: "))
    if n < 0:
        print("n має бути не менше 0")
    else:
        fibonacci = Task3()
        result = fibonacci.calculate(n)
        print(f"F({n}) = {result}")
        
    print('\n\nTask N4:')
    n = int(input("Введіть кількість кроків (n): "))
    if n < 1 or n > 45:
        print("Некоректне значення n. n має бути в діапазоні від 1 до 45.")
    else:
        climbing_stairs = Task4()
        unique_combinations = climbing_stairs.countWays(n)
        print(f"Кількість унікальних комбінацій для досягнення вершини: {unique_combinations}")
        
    print('\n\nTask N5:')
    x = float(input("Введіть x: "))
    n = int(input("Введіть n: "))
    if -100.0 < x < 100.0 and -2**31 <= n <= 2**31 - 1:
        custom_pow = Task5()
        result = custom_pow.calculate_pow(x, n)
        print(f"{x}^{n} = {result:.5f}")
    else:
        print("Некоректні значення x або n, не відповідають обмеженням.")
        
    input()