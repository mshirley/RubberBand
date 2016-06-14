#!/usr/bin/env python

import ConfigParser
import elasticsearch


def searchelastic(index, line):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read("rubberband.conf")
        es = elasticsearch.Elasticsearch(conf.get('elastic', 'server'))
        results = es.search(index=index, q='{0}'.format(line))
        data = results['hits']
        return data
    except Exception as e:
        print str(e)
