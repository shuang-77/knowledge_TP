import pandas as pd
from py2neo import Node,Relationship,Graph,NodeMatcher,RelationshipMatcher
# 创建节点
def CreateNode(m_graph,m_label,m_attrs):
    m_n="_.name="+"\'"+m_attrs['name']+"\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    print(re_value)
    if re_value is None:
        m_mode = Node(m_label,**m_attrs)
        n = graph.create(m_mode)
        return n
    return None
# 查询节点
def MatchNode(m_graph,m_label,m_attrs):
    m_n="_.name="+"\'"+m_attrs['name']+"\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    return re_value
# 创建关系
def CreateRelationship(m_graph,m_label1,m_attrs1,m_label2,m_attrs2,m_r_name):
    reValue1 = MatchNode(m_graph,m_label1,m_attrs1)
    reValue2 = MatchNode(m_graph,m_label2,m_attrs2)
    if reValue1 is None or reValue2 is None:
        return False
    m_r = Relationship(reValue1,m_r_name,reValue2)
    n = graph.create(m_r)
    return n
graph = Graph('http://localhost:7474',username='neo4j',password='Graph')
graph.delete_all()
Names = ["老师","超市","程序员","小卖部","阳仔公司","人","日常用品"]
action = ["传授","销售","敲","售卖","提供","购买","包括"]
things = ["知识","日常用品","代码","日常用品","餐饮服务","日常用品","鞋子"]
data = pd.DataFrame({"名称":Names,"字段":things,"方式":action})
#data

label1 = "Name"
label2 = "things"
for i,j in data.iterrows():
    # 名称
    attr1 = {"name":j.名称}
    CreateNode(graph,label1,attr1)
    # 产品
    attr2 = {"name":j.字段}
    CreateNode(graph,label2,attr2)

    m_r_name = j.方式
    reValue = CreateRelationship(graph,label1,attr1,label2,attr2,m_r_name)
    print(reValue)

