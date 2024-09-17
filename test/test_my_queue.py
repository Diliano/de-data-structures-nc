from src.my_queue import Queue

class TestInstantiation:
    def test_instance_is_instance_of_class_queue(self):
        test_queue = Queue()
        assert isinstance(test_queue, Queue)

    def test_max_size_property_instantiated_with_given_arg(self):
        test_queue = Queue(5)
        assert test_queue.max_size == 5

    def test_instance_is_instantiated_with_front_property(self):
        test_queue = Queue(5)
        assert test_queue._front == 0

    def test_instance_is_instantiated_with_back_property(self):
        test_queue = Queue(5)
        assert test_queue._back == 0

    def test_instance_is_instantiated_with_storage_property(self):
        test_queue = Queue(5)
        assert test_queue._storage == {}

class TestEnqueueMethod:
    def test_enqueue_method_adds_item_to_back_of_queue(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple")
        # Assert
        assert test_queue._storage == {0: "apple"}

    def test_enqueue_method_updates_back_position(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple")
        # Assert
        assert test_queue._back == 1

    def test_enqueue_method_adds_multiple_items_to_back_of_queue(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple")
        test_queue.enqueue("banana")
        test_queue.enqueue("orange")
        # Assert
        assert test_queue._storage == {0: "apple", 1: "banana", 2: "orange"}
        assert test_queue._back == 3

    def test_enqueue_method_only_adds_item_if_queue_is_not_full(self):
        # Arrange
        test_queue = Queue(2)
        # Act
        test_queue.enqueue("apple")
        test_queue.enqueue("banana")
        # Assert
        assert test_queue.enqueue("orange") == "Queue is full"

class TestDequeueMethod:
    def test_dequeue_method_removes_item_from_front_of_queue(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple")
        test_queue.enqueue("banana")
        test_queue.dequeue()
        # Assert
        assert test_queue._storage == {1: "banana"}

    def test_dequeue_method_updates_front_position(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple") 
        test_queue.enqueue("banana") 
        test_queue.dequeue()  
        # Assert
        assert test_queue._front == 1

    def test_dequeue_method_removes_multiple_items_from_front_of_queue(self):
        # Arrange
        test_queue = Queue()
        # Act
        test_queue.enqueue("apple") 
        test_queue.enqueue("banana") 
        test_queue.enqueue("orange") 
        test_queue.dequeue()
        test_queue.dequeue()
        # Assert
        assert test_queue._storage == {2: "orange"}

    def test_dequeue_method_returns_message_if_queue_is_empty(self):
        test_queue = Queue()
        assert test_queue.dequeue() == "Queue is empty"