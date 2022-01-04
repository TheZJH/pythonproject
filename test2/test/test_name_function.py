import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('tom', 'zjh')
        # 断言方法用来核实得到的结果和预期的结果是否一致
        self.assertEqual(formatted_name, 'tom zjh')


if __name__ == '__main__':
    unittest.main()
