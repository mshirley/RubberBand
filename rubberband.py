#!/usr/bin/env python

import cmd
import elasticsearch
import json
from libs.colours import Colours
import ConfigParser

index = '*'


class RubberBand(cmd.Cmd):
    prompt = Colours.B + 'rubberband >> ' + Colours.N
    intro = Colours.O + "ElasticSearch Simple Search Engine" + Colours.N

    def do_search(self, line):
        try:
            conf = ConfigParser.ConfigParser()
            conf.read("rubberband.conf")
            es = elasticsearch.Elasticsearch(conf.get('elastic', 'server'))
            results = es.search(index=index, q='{0}'.format(line))
            data = results['hits']
            print Colours.B + '[-] Number of hits: {0}'.format(data['total']) + Colours.N
            print Colours.B + '[-] Search Query: {0}'.format(line) + Colours.N
            if data['total'] > 0:
                for d in data['hits']:
                    print json.dumps(d['_source'], sort_keys=True, indent=4)
            else:
                print Colours.R + 'No results found' + Colours.N
        except Exception as e:
            print Colours.R + '[!] Search Error: {0}'.format(str(e)) + Colours.N

    def do_index(self, eindex):
        global index
        index = eindex
        print Colours.G + '[-] Index set to: {0}'.format(index) + Colours.N

    def do_exit(self, line):
        print Colours.R + '[!] Exiting...' + Colours.N
        return True

if __name__ == '__main__':
    RubberBand().cmdloop()
