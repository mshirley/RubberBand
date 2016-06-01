#!/usr/bin/env python

import cmd
import elasticsearch
import json


class RubberBand(cmd.Cmd):
    prompt = 'rubberband: '
    intro = "ElasticSearch Simple Search Engine"

    def do_search(self, line):
        es = elasticsearch.Elasticsearch('192.168.2.143')
        results = es.search(index='test', q='{0}'.format(line))
        data = results['hits']
        if data['total'] > 0:
            for d in data['hits']:
                print json.dumps(d['_source'], sort_keys=True, indent=4)
        else:
            print 'No results found'


if __name__ == '__main__':
    RubberBand().cmdloop()
