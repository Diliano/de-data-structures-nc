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