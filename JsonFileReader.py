#!/usr/bin/env python

import json

class JsonFileReader:
    def __init__(self):
        pass

    @staticmethod
    def parse_file(file_name_and_path):

        """
        Reads json file in Katanator's expected format
        """
        ret = []
        with open(file_name_and_path, 'r') as fp:
            data = json.load(fp)
            for key in data:
                weight = int(key['weight'])
                print weight
                for i in range(weight):
                    ret.append(str(key['key']).strip())
        print ret
        return ret
