# -*- coding: utf-8 -*-

import json
class TrainPipeline(object):

    def __init__(self):
        self.file = open('./Beauty.jl','w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item
