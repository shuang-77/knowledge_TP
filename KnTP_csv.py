from py2neo import Graph, Node, Relationship
import pandas as pd
import csv

# 连接neo4j数据库，输入地址、用户名、密码

graph = Graph("http://localhost:7474", username="neo4j", password='password')
graph.delete_all()
with open('D:\\actor.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(data[0])
    for i in range(1, len(data)):
        # print(data[i][1])
        node = Node('name', id=data[i][0], level=data[i][1])
        relation = Node('actor', name=data[i][2])
        relation1 = Node('relation', name=data[i][3])
        relation2 = Node('director', name=data[i][4])

        graph.create(node)
        graph.create(relation)
        graph.create(relation1)
        graph.create(relation2)
        actor = Relationship(node, '主演', relation)
        relation = Relationship(node, '关系', relation1)
        director = Relationship(node, '导演', relation2)
        graph.create(actor)
        graph.create(relation)
        graph.create(director)
