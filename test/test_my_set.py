from src.my_set import Set

class TestInstantiation():
    def test_new_instance_is_instance_of_set_class(self):
        test_set = Set()
        assert isinstance(test_set, Set)

    def test_creates_empty_set_given_empty_input(self):
        test_set = Set()
        assert test_set._elements == []

    def test_instantiates_set_with_single_given_element(self):
        test_set = Set(["apple"])
        assert test_set._elements == ["apple"]

    def test_instantiates_set_with_given_iterable_elements(self):
        test_set = Set(["apple", "banana"])
        assert test_set._elements == ["apple", "banana"]

    def test_instantiates_set_without_adding_duplicates(self):
        test_set = Set(["apple", "banana", "apple", "banana"])
        assert test_set._elements == ["apple", "banana"]

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

class TestDiscardMethod():
    def test_discard_method_discards_specified_element_from_set(self):
        # Arrange
        test_set = Set(["apple", "banana"])
        # Act
        test_set.discard("banana")
        # Assert
        assert test_set._elements == ["apple"]

    def test_discard_method_does_nothing_if_element_does_not_exit(self):
        test_set = Set(["apple", "banana"])
        test_set.discard("orange") # No error thrown 
        assert test_set._elements == ["apple", "banana"]

class TestUnionMethod():
    def test_union_method_returns_set_containing_elements_from_original_set_and_given_set(self):
        # Arrange
        test_set = Set(["apple", "banana"])
        test_input = ["orange", "pear"]
        expected = ["apple", "banana", "orange", "pear"]
        # Act
        result = test_set.union(test_input) 
        # Assert 
        assert isinstance(result, Set)
        assert result._elements == expected

    def test_union_method_returns_set_without_duplicates(self):
        # Arrange
        test_set = Set(["apple", "banana"])
        test_input = ["orange", "pear", "apple"]
        expected = ["apple", "banana", "orange", "pear"]
        # Act
        result = test_set.union(test_input)
        # Assert
        assert isinstance(result, Set)
        assert result._elements == expected

class TestIntersectionMethod():
    def test_intersection_method_returns_set_containing_elements_that_appear_in_both_original_and_given_iterable(self):
        # Arrange
        test_set = Set(["apple", "banana", "orange", "pear"])
        test_input = ["apple", "kiwi", "orange", "grape"]
        expected = ["apple", "orange"]
        # Act
        result = test_set.intersection(test_input)
        # Assert
        assert isinstance(result, Set)
        assert result._elements == expected   

    def test_intersection_method_returns_empty_set_if_there_are_no_common_elements(self):
        # Arrange
        test_set = Set(["apple", "banana"])
        test_input = ["orange", "grape"]
        expected = []
        # Act
        result = test_set.intersection(test_input)
        # Assert
        assert isinstance(result, Set)
        assert result._elements == expected   