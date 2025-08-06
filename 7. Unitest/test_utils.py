# import unittest
# from utils import add
#
# class TestAddition(unittest.TestCase):
#
#     def test_addition(self):
#         self.assertEqual(add(4, 5), 9)
#         self.assertEqual(add(10, -7), 3)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(8, 4), 12)
#
#     # 10 - 5 = 5
#     # 6 - (-3) = 9
#
#
# if __name__=="__main__":
#     unittest.main()

# import pytest
# from utils import add, multiply, is_polindrome
# import utils
#
# # def test_addition():
# #     assert add(10, 5) == 15
# #     assert add(7, -3) == 4 # Error
# #     assert add(6, -7) == -1
# #
# # def test_mult():
# #     assert multiply(3, 4) == 13 # error
# #     assert multiply(0, 18) == 1 # error
#
# def test_add_positive_numbers():
#     assert add(2, 7) == 9
#
# def test_add_negative_numbers():
#     assert add(-3, -6) == -9
#
# def test_zero_add():
#     assert add(0, 8) == 8
#     assert add(-4, 0) == -4
#
# def test_add_float_numbers():
#     assert add(2.5, 3.5) == 6.0
#     assert add(4, 4.4) == 8.4
#     assert add(0.1, 0.3) == pytest.approx(0.4)
#
# def test_add_string():
#     with pytest.raises(TypeError):
#         add("3", "5")
#         add(3, "5")
#         add("3", 5)
#
#
# def test_polindrome():
#     assert utils.is_polindrome("madam") == True
#     assert utils.is_polindrome("Race car") == True
#     assert utils.is_polindrome("The big brown fox jumps over the lazy dog") == False
#     assert utils.is_polindrome("BreAD") == False
#
# def test_is_polindrome_empty_string():
#     assert is_polindrome("") == True
#
# def test_is_polindrome_single_char():
#     assert is_polindrome("a") == True
#
#
#
# @pytest.mark.parametrize("a, b, expected",
#                          [
#                              (2, 3, 6),
#                              (-1, 5, -5),
#                              (-3, -7, 21),
#                              (0, 10, 0),
#                              (2.5, 2.5, 6.25)
#                          ])
# def test_multiply_with_params(a, b, expected):
#     assert multiply(a, b) == expected
#
# @pytest.fixture
# def tmp_file(tmp_path):
#     file_path = tmp_path / "test_data.txt"
#     file_path.write_text("Its test data")
#     print(f"Create Fixture for temp file ({file_path})")
#     yield file_path
#     print(f"End Fixture. And deleted file ({file_path})")
#
# def test_read_temp_file(tmp_file):
#     print(f"Read form file {tmp_file}")
#     content = tmp_file.read_text()
#     assert "test" in content
#     assert len(content) > 0
#
# def test_write_to_tmp_file(tmp_file):
#     print(f"Write to file {tmp_file}")
#     tmp_file.write_text("New data from test_write")
#     content = tmp_file.read_text()
#     assert "New data from test_write" in content

import pytest
from utils import reverse_list

# [100, 200] -> [200, 100]

def test_reverse_list():
    assert reverse_list([100, 200]) == [200, 100]
    assert reverse_list(list(range(1, 10))) == list(range(9, 0, -1))

def test_empty_list():
    assert reverse_list([]) == []

def test_sequence_not_list():
    with pytest.raises(TypeError):
        assert reverse_list("1234")


















