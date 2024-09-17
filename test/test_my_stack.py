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

def test_instance_is_instantiated_with_unlimited_max_size_given_no_arg():
    test_stack = Stack()
    assert test_stack.max_size is None

def test_push_method_adds_item_to_stack_storage():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    # Assert
    assert test_stack.storage == {0: "apple"}

def test_push_method_adds_multiple_items_to_stack_storage():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    test_stack.push("banana")
    # Assert
    assert test_stack.storage == {0: "apple", 1: "banana"}

def test_push_method_updates_quantity_property():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    # Assert
    assert test_stack.quantity == 1

    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    test_stack.push("banana")
    # Assert
    assert test_stack.quantity == 2

def test_push_method_returns_message_if_stack_full():
    # Arrange
    test_stack = Stack(1)
    # Act
    test_stack.push("apple")
    # Assert
    assert test_stack.push("banana") == "Stack storage is full"
    assert test_stack.storage == {0: "apple"}

def test_pop_method_removes_item_from_storage_and_returns_it():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    test_stack.push("banana")
    # Assert
    assert test_stack.pop() == "banana"
    assert test_stack.storage == {0: "apple"}

def test_pop_method_returns_message_if_stack_empty():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    test_stack.pop()
    # Assert
    assert test_stack.pop() == "Stack is empty"

def test_pop_method_updates_quantity():
    # Arrange
    test_stack = Stack()
    # Act
    test_stack.push("apple")
    # Assert
    assert test_stack.quantity == 1
    test_stack.pop()
    assert test_stack.quantity == 0

def test_is_empty_method_checks_storage_and_returns_boolean():
    test_stack = Stack()
    assert test_stack.is_empty() is True

    test_stack = Stack()
    test_stack.push("apple")
    assert test_stack.is_empty() is False

def test_is_full_method_checks_storage_and_returns_boolean():
    test_stack = Stack()
    test_stack.push("apple")
    assert test_stack.is_full() is False

    test_stack = Stack(1)
    test_stack.push("apple")
    assert test_stack.is_full() is True