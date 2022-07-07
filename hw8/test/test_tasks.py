import unittest
from pathlib import Path
import os, sys
from src.compile_word_counts import create_dict
from src.compute_pony_lang import compute_score
import json

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')


    def test_task1(self):
        # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        #self.assertTrue(True)
        print("\nTest for Task #1:")
        output_word_count=create_dict(self.mock_dialog)
        with open(self.true_word_counts, 'r', encoding='utf-8') as file:
            data = json.load(file)
            try:
                self.assertEqual(len(output_word_count), len(data))
                for pony in data:
                    try:
                        self.assertEqual(len(output_word_count[pony]), len(data[pony]))
                        for word in data[pony]:
                            try:
                                a=output_word_count[pony][word]
                                b=data[pony][word]
                                try:
                                    self.assertEqual(a,b)
                                except AssertionError:
                                    print("Fail! Task1 output json count word with wrong frequency")
                                    return
                            except KeyError:
                                print("Fail! Task1 output json miss some words from a pony")
                                return
                    except AssertionError:
                        print("Fail! Task1 output json compute incorrect # of words")
                        return
                print("OK! Got expected result!")
            except AssertionError:
                print("Fail! Task1 output json not include all the pony names")
                return

    def test_task2(self):
        # use self.true_word_counts self.true_tf_idfs; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        #self.assertTrue(True)
        print("\nTest for Task #2:")
        output_word_dic= compute_score(self.true_word_counts,2)
        with open(self.true_tf_idfs, 'r', encoding='utf-8') as file:
            data = json.load(file)
            try:
                self.assertEqual(len(output_word_dic), len(data))
                for pony in data:
                    try:
                        self.assertEqual(len(output_word_dic[pony]), 2)
                        for word in data[pony]:
                            try:
                                output_word_dic[pony].index(word)
                            except ValueError:
                                print("Fail! Task2 output compute words list that include incorrect word")
                                return
                    except AssertionError:
                        print("Fail! Task2 output compute words list with incorrect # of words")
                        return
                print("OK! Got expected result!")
            except AssertionError:
                print("Fail! Task1 output json not include all the pony names")
                return
        
    
if __name__ == '__main__':
    unittest.main()