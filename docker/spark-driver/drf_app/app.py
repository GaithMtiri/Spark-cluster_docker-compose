from pyspark import SparkConf, SparkContext
import random



# conf = SparkConf().setAppName('MayssaDemo').setMaster('spark://18.184.46.62:7077').setSparkHome('/opt/spark/')
# sc = SparkContext(conf=conf)
#
#
# def inside(p):
#     x, y = random.random(), random.random()
#     return x*x + y*y < 1
#
# count = sc.parallelize(xrange(0, 100)) \
#     .filter(inside).count()
# print ("Pi is roughly %f") % (4.0 * count / 100)




#
#
# conf = SparkConf().setAppName('MayssaDemo').setMaster('spark://10.5.0.2:7077').setSparkHome('/opt/spark/')
# sc = SparkContext(conf=conf)
#
#
# def inside(p):
#     x, y = random.random(), random.random()
#     return x*x + y*y < 1
#
# count = sc.parallelize(xrange(0, 100)) \
#     .filter(inside).count()
# print ("Pi is roughly %f") % (4.0 * count / 100)

from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'10.5.0.5','port':9200}])

# e1={
#     "first_name":"nitin",
#     "last_name":"panwar",
#     "age": 27,
#     "about": "Love to play cricket",
#     "interests": ['sports','music'],
# }
#
# res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)

e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}

res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)