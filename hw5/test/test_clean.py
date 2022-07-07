import unittest
from pathlib import Path
import os, sys
from src.clean import valid_title,valid_time,valid_dict,valid_author,valid_cast_count,valid_tag,loads_dict

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
print(parentdir)

class CleanTest(unittest.TestCase):

    def setUp(self):
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
        self.fixture1_path = os.path.join(parentdir,'test','fixtures','test_1.json')
        self.fixture2_path = os.path.join(parentdir,'test','fixtures','test_2.json')
        self.fixture3_path = os.path.join(parentdir,'test','fixtures','test_3.json')
        self.fixture4_path = os.path.join(parentdir,'test','fixtures','test_4.json')
        self.fixture5_path = os.path.join(parentdir,'test','fixtures','test_5.json')
        self.fixture6_path = os.path.join(parentdir,'test','fixtures','test_6.json')

    def test_title(self):
        with open(self.fixture1_path, 'r', encoding='utf-8') as fixture_1:
            print("\nConstraint1: Posts that don’t have either “title” or “title_text” should be removed")
            line= fixture_1.readline()
            try:
                self.assertEqual(valid_title(line), False)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_1.close()

    def test_createAt(self):
        with open(self.fixture2_path, 'r', encoding='utf-8') as fixture_2:
            print("\nConstraint2: createdAt dates that don’t pass the ISO datetime standabe removed")
            line= fixture_2.readline()
            line = loads_dict(line)
            try:
                self.assertEqual(valid_time(line), False)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_2.close()

    def test_json_dict(self):
        with open(self.fixture3_path, 'r', encoding='utf-8') as fixture_3:
            print("\nConstraint3: Any lines that contain invalid JSON dictionaries should be ignored")
            line = fixture_3.readline()
            try:
                self.assertEqual(valid_dict(line), False)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_3.close()

    def test_author(self):
        with open(self.fixture4_path, 'r', encoding='utf-8') as fixture_4:
            print("\nConstraint4: Any lines for which author is null, N/A or empty should be ignored")
            line = fixture_4.readline()
            line = loads_dict(line)
            try:
                self.assertEqual(valid_author(line), False)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_4.close()

    def test_total_count(self):
        with open(self.fixture5_path, 'r', encoding='utf-8') as fixture_5:
            print("\nConstraint5: total_count is a string containing a cast-able number, total_count is cast to an int properly.")
            line = fixture_5.readline()
            line = loads_dict(line)
            try:
                self.assertEqual(valid_cast_count(line), False)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_5.close()

    def test_tag(self):
        with open(self.fixture6_path, 'r', encoding='utf-8') as fixture_6:
            print("\nConstraint6: the tags field gets split on spaces when given a tag containing THREE words")
            line = fixture_6.readline()
            line = loads_dict(line)
            try:
                output_tag=valid_tag(line)["tags"]
                self.assertEqual(len(output_tag), 4)
                print("OK! Got expected result.")
            except AssertionError:
                print("Fail.")
        fixture_6.close()

if __name__ == '__main__':
    unittest.main()
