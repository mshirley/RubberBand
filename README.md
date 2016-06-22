# RubberBand
ElasticSearch Engine (Python)

Simple command line Elasticsearch search tool.  

Change rubberband.conf to point at your Elasticsearch server (default port is 9200)

rubberband>>> help (lists available commands)  
rubberband>>> set index "index" (set index, default is "*")  
rubberband>>> search "search query" (use Lucene search queries)  
rubberband>>> exit (well it exits)  

#####Example  
rubberband>>> set index test (set the index to test)  
rubberband>>> search name: * AND city: London (search for all name values that are in the city of London)  

It's not perfect but it works and that meets my key requirement for coding.


# Python Libraries
pip install elasticsearch

