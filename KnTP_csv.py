from py2neo import Graph, Node, Relationship
import pandas as pd
import csv
# 连接neo4j数据库，输入地址、用户名、密码

graph = Graph("http://localhost:7474",username="neo4j",password='password')
graph.delete_all()
with open('D:\\actor.csv','r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(data[0])
    for j in range(1,len(data)):
        for i in range(j+1,len(data)):
            if  data[j][1]==data[i][1]:
                print(data[j][1])
                data[j][1]=0

    for j in range(1,len(data)):
        for i in range(j+1,len(data)):
            if  data[j][2]==data[i][2]:
                print(data[j][2])
                data[j][2] = 0
                print(data[i])
        #relation = Node('actor', name=data[j][2])
        #graph.create(relation)



    for j in range(1,len(data)):
        for i in range(j+1, len(data)):
            if  data[j][3]==data[i][3]:
                print(data[j][3])
                data[j][3]=0


    for j in range(1,len(data)):
        for i in range(j+1, len(data)):
            if data[j][4]==data[i][4]:
                print(data[j][4])
                data[j][4]=0

    for i in range(1, len(data)):
        if data!= 0:
            node = Node('name', id=data[i][0], level=data[i][1])

            relation = Node('actor', name=data[i][2])

            relation1 = Node('relation', name=data[i][3])

            relation2 = Node('director', name=data[i][4])
            graph.create(node)
            graph.create(relation)
            graph.create(relation1)
            graph.create(relation2)

            actor = Relationship(node, '主演', relation)
            relation = Relationship(relation1, '关系',node )
            director = Relationship(node, '导演', relation2)
            graph.create(actor)
            graph.create(relation)
            graph.create(director)









'''with open('D:\\Study\\Python+Neo4j\\neo4j+python\\film_name.csv','r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data[0])
for i  in  range(1,len(data)):
    node = Node('name',id = data[i][0],level= data[i][1],label=data[i][2])
    graph.create(node)

with open('D:\\Study\\Python+Neo4j\\neo4j+python\\actor.csv', 'r', encoding='UTF-8') as f1:
    reader = csv.reader(f1)
    data = list(reader)
    print(data[0])
    for i in range(1, len(data)):
        relation = Node('actor',name = data[i][1])
        graph.create(relation)
        actor = Relationship(node, '主演', relation)
        graph.create(actor)

with open('D:\\Study\\Python+Neo4j\\neo4j+python\\cooperation.csv', 'r', encoding='UTF-8') as f2:
        reader = csv.reader(f2)
        data = list(reader)
        print(data[0])
        for i in range(1, len(data)):
            relation1 = Node('relation',name = data[i][2])
            graph.create(relation1)
            relation = Relationship(node, '关系', relation1)
            graph.create(relation)

with open('D:\\Study\\Python+Neo4j\\neo4j+python\\director.csv', 'r', encoding='UTF-8') as f3:
        reader = csv.reader(f3)
        data = list(reader)
print(data[0])
        for i in range(1, len(data)):
            relation2 = Node('director',name = data[i][1])
            graph.create(relation2)
            director = Relationship(node,'导演',relation2)
            graph.create(director)'''

'''from py2neo import Graph, Node, Relationship
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
        graph.create(director)'''
