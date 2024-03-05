# реализация с использованием списка:
class CircularBufferArray:
    def __init__(self, capacity):
        # создаем список заданной емкости, инициализируем переменные
        self.buffer = [None] * capacity
        self.capacity = capacity  # емкость буфера
        self.size = 0  # текущий размер буфера
        self.head = 0  # указатель на начало буфера
        self.tail = 0  # указатель на конец буфера

    def enqueue(self, item):
        # проверяем, не переполнен ли буфер
        if self.size == self.capacity:
            raise Exception("buffer overflow")
        # добавляем элемент в конец буфера
        self.buffer[self.tail] = item
        # обновляем указатель на конец буфера
        self.tail = (self.tail + 1) % self.capacity
        # увеличиваем размер буфера
        self.size += 1

    def dequeue(self):
        # проверяем, не пуст ли буфер
        if self.size == 0:
            raise Exception("buffer underflow")
        # получаем элемент из начала буфера
        item = self.buffer[self.head]
        # обновляем указатель на начало буфера
        self.head = (self.head + 1) % self.capacity
        # уменьшаем размер буфера
        self.size -= 1
        return item


# реализация с использованием связанного списка:
class Node:
    def __init__(self, data):
        # создаем узел с данными и ссылкой на следующий узел
        self.data = data
        self.next = None

class CircularBufferLinkedList:
    def __init__(self, capacity):
        # инициализируем переменные
        self.capacity = capacity  # емкость буфера
        self.size = 0  # текущий размер буфера
        self.head = None  # указатель на начало буфера
        self.tail = None  # указатель на конец буфера

    def enqueue(self, item):
        # проверяем, не переполнен ли буфер
        if self.size == self.capacity:
            raise Exception("buffer overflow")
        # создаем новый узел с данными
        new_node = Node(item)
        # если буфер пуст, новый узел становится началом и концом буфера
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # иначе новый узел добавляется в конец буфера
            self.tail.next = new_node
            self.tail = new_node
        # увеличиваем размер буфера
        self.size += 1

    def dequeue(self):
        # проверяем, не пуст ли буфер
        if self.size == 0:
            raise Exception("buffer underflow")
        # получаем элемент из начала буфера
        item = self.head.data
        # перемещаем указатель на начало буфера на следующий узел
        self.head = self.head.next
        # уменьшаем размер буфера
        self.size -= 1
        return item


"""
плюсы и минусы

реализация с использованием списка:
плюсы:
использование списка делает код простым и понятным
быстродействие при доступе по индексу сложность O(1)
удобно управлять размером буфера.
минусы:
при увеличении емкости буфера может потребоваться перераспределение памяти и копирование данных
при удалении элементов могут быть проблемы с границами списка

реализация с использованием связанного списка:
плюсы:
гибкость в изменении размера буфера
меньшая вероятность перекрытия границ буфера
минусы:
большее количество оперативной памяти
более сложная реализация

сравнение быстродействия:
обе реализации имеют методы `enqueue` и `dequeue` со сложностью O(1)
при использовании связанного списка метод `dequeue` может быть более эффективной
в реализации со списком методы `enqueue` и `dequeue` могут быть более эффективны при доступе по индексу. 
В целом, выбор между этими реализациями зависит от конкретных требований проекта:
если необходима гибкость в изменении размера буфера и нет ограничений на использование дополнительной памяти, то связанный список
если важен прямой доступ к элементам по индексу и оптимальное использование памяти, то подходит реализация со списком
"""