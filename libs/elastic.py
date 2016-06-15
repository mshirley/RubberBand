#!/usr/bin/env python

import ConfigParser
import elasticsearch


def countelastic(index):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read("rubberband.conf")
        es = elasticsearch.Elasticsearch(conf.get('elastic', 'server'))
        results = es.search(index=index, q='*')
        data = results['hits']
        return data['total']
    except Exception as e:
        print str(e)


def searchelastic(index, line):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read("rubberband.conf")
        size = countelastic(index)
        es = elasticsearch.Elasticsearch(conf.get('elastic', 'server'))
        results = es.search(index=index, size=size, q='{0}'.format(line))
        data = results['hits']
        return data
    except Exception as e:
        print str(e)
