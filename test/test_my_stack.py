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