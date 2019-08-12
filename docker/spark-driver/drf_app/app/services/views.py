from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.services.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from pyspark import SparkConf, SparkContext
import random
from operator import add
from elasticsearch import Elasticsearch



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PieViewSet(viewsets.ViewSet):
    def list(self, request, format=None):
        conf = SparkConf().setAppName('Pie Approximation').setMaster('spark://10.5.0.2:7077').setSparkHome('/opt/spark/')
        sc = SparkContext(conf=conf)


        def inside(p):
            x, y = random.random(), random.random()
            return x*x + y*y < 1

        count = sc.parallelize(xrange(0, 100)) \
            .filter(inside).count()

        sc.stop()

        return Response(("Pi is roughly %f") % (4.0 * count / 100))

class CalWordViewSet(viewsets.ViewSet):

    def list(self, request, format=None):

        # print request.GET['calc']

        conf = SparkConf().setAppName('Occurence of words').setMaster('spark://10.5.0.2:7077').setSparkHome('/opt/spark/')
        sc = SparkContext(conf=conf)
        es=Elasticsearch([{'host':'10.5.0.5','port':9200}])

        s = request.GET['calc']
        seq = s.split()   # ['Hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'word', 'count']
        counts= sc.parallelize(seq) \
          .map(lambda word: (word, 1)) \
          .reduceByKey(add) \
          .collect()

        sc.stop()

        entry  = {'text': request.GET['calc'], "occurence": dict(counts) }
        res = es.index(index="word_occurence", doc_type="word_occurence", body= entry)

        print(dict(counts))

        return Response(counts)

