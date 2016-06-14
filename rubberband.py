#!/usr/bin/env python

import cmd
import json
from libs.colours import Colours
from libs.elastic import searchelastic


# ElasticSearch CLI Project by Adam Maxwell (@catalyst256)
# Thanks to LaNMaSteR53 for the inspiration and code tips from recon-ng

index = '*'


class RubberBand(cmd.Cmd):
    prompt = Colours.B + 'rubberband >> ' + Colours.N
    intro = Colours.O + "ElasticSearch Simple Search Engine" + Colours.N

    def emptyline(self):
        # disables running of last command when no command is given
        # return flag to tell interpreter to continue
        return 0

    def do_search(self, line):
        try:
            data = searchelastic(index, line)
            print Colours.B + '[-] Number of hits: {0}'.format(data['total']) + Colours.N
            if data['total'] > 0:
                for d in data['hits']:
                    print json.dumps(d['_source'], sort_keys=True, indent=4)
            else:
                print Colours.R + 'No results found' + Colours.N
            print Colours.B + '[-] Search Query: {0}'.format(line) + Colours.N
        except Exception as e:
            print Colours.R + '[!] Search Error: {0}'.format(str(e)) + Colours.N

    def do_set(self, params):
        if not params:
            self.help_create()
            return
        params = params.split()
        arg = params.pop(0).lower()
        if arg == 'index':
            global index
            index = params[0]
            print Colours.G + '[-] Index set to: {0}'.format(index) + Colours.N

    def do_exit(self, line):
        print Colours.R + '[!] Exiting...' + Colours.N
        return True

    # Various help functions
    def help_search(self):
        print(Colours.O + 'Usage: search [query] - Queries ElasticSearch using Lucene Queries' + Colours.N)

    def help_set(self):
        print(Colours.O + 'Usage: set index [index] - Sets the default ElasticSearch index' + Colours.N)

    def help_exit(self):
        print(Colours.O + 'Usage: exit - Exits rubberband' + Colours.N)


if __name__ == '__main__':
    RubberBand().cmdloop()
