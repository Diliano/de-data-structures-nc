from src.my_set import Set

class TestInstantiation():
    def test_new_instance_is_instance_of_set_class(self):
        test_set = Set()
        assert isinstance(test_set, Set)

    def test_creates_empty_set_given_empty_input(self):
        test_set = Set()
        assert test_set._elements == []