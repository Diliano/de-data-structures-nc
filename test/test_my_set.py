from src.my_set import Set

class TestInstantiation():
    def test_new_instance_is_instance_of_set_class(self):
        test_set = Set()
        assert isinstance(test_set, Set)

    def test_creates_empty_set_given_empty_input(self):
        test_set = Set()
        assert test_set._elements == []

class TestAddMethod():
    def test_add_method_adds_an_item_to_the_set(self):
        # Arrange
        test_set = Set()
        # Act
        test_set.add("apple")   
        # Assert
        assert test_set._elements == ["apple"]

    def test_add_method_does_not_add_a_duplicate_to_the_set(self):
        # Arrange
        test_set = Set()
        # Act
        test_set.add("apple")   
        test_set.add("apple")   
        # Assert
        assert test_set._elements == ["apple"]

class TestUpdateMethod():
    def test_update_method_adds_multiple_items_from_an_iterable_to_the_set(self):
        # Arrange
        test_set = Set()
        # Act
        test_set.update(["apple", "banana", "orange"])   
        # Assert
        assert test_set._elements == ["apple", "banana", "orange"]

    def test_update_method_does_not_add_duplicates_from_an_iterable_to_the_set(self):
        # Arrange
        test_set = Set()
        # Act
        test_set.update(["apple", "apple", "banana", "orange", "apple", "banana"])   
        # Assert
        assert test_set._elements == ["apple", "banana", "orange"]