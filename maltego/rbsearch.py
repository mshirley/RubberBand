#!/usr/bin/env

import ConfigParser
from MaltegoTransform import *
from libs.elastic import searchelastic
import sys

conf = ConfigParser.ConfigParser()
conf.read("rubberband.conf")

m = MaltegoTransform()


def maltegosearch(term):
    try:
        data = searchelastic('*', term)
        if data['total'] > 0:
            for d in data:
                print d
        else:
            m.addUIMessage("No results found: {0}".format(term))

    except Exception as e:
        m.addUIMessage(str(e))

    m.returnOutput()

if __name__ == '__main__':
    maltegosearch(sys.argv[1])



