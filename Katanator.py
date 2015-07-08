#!/usr/bin/env python

"""
 Katanator - Random practice problem selector
 Chris Leighton
 2015-02-01
"""

import JsonFileReader
import os
from random import choice

class Katanator:
    def __init__(self):
        pass

    def make_selection(self):
        """
        make the selection
        :return: string to output to user containing language and problem
        """
        curr_dir = os.path.dirname(__file__)
        problems = JsonFileReader.JsonFileReader.parse_file(os.path.join(curr_dir, 'problems.json'))
        languages = JsonFileReader.JsonFileReader.parse_file(os.path.join(curr_dir, 'languages.json'))

        problem = choice(problems)
        language = choice(languages)

        print "Language: {}, Problem: {}".format(language, problem)


if __name__ == '__main__':
    katanator = Katanator()
    katanator.make_selection()
