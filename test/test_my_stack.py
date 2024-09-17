from src.my_stack import Stack

def test_creates_instance_of_class():
    test_stack = Stack()
    assert isinstance(test_stack, Stack)

def test_instance_is_instantiated_with_quantity_property_0():
    test_stack = Stack()
    assert test_stack.quantity == 0

def test_instance_is_instantiated_with_empty_dict_storage_property():
    test_stack = Stack()
    assert test_stack.storage == {}

def test_instance_is_instantiated_with_given_max_size_property():
    test_stack = Stack(5)
    assert test_stack.max_size == 5

def test_instance_is_instantiated_with_0_max_size_given_no_arg():
    test_stack = Stack()
    assert test_stack.max_size == 0