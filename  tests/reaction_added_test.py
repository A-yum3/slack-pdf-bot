import json
import unittest

from app import reaction_add


class ReactionAddedTest(unittest.TestCase):

    def test(self):
        with open('./dummies/reaction_added.json', 'r') as f:
            json_data = json.load(f)
        print(json_data)
        reaction_add(json_data, None)


if __name__ == '__main__':
    unittest.main()
