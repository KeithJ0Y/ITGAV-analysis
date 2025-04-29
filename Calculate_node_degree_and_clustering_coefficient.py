import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# 读取数据
df = pd.read_csv("string_interactions.tsv", sep="\t")

# 创建一个空图
G = nx.Graph()

# 遍历数据并将每一行作为边加入图中
for index, row in df.iterrows():
    # 假设数据中的'node1'和'node2'列是蛋白质的ID，'combined_score'是连接权重
    G.add_edge(row['node1_string_id'], row['node2_string_id'], weight=row['combined_score'])

# 计算节点度
degree_dict = dict(G.degree())
print("节点度:", degree_dict)

# 计算聚类系数
clustering_dict = nx.clustering(G)
print("聚类系数:", clustering_dict)

# 查看聚类系数较高的前十个节点
top_10_degree = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:10]
for node, degree in top_10_degree:
    print(f"节点: {node}, 度数: {degree}")
    plt.show()

# 绘制度数分布图
degree_values = list(degree_dict.values())
plt.hist(degree_values, bins=range(min(degree_values), max(degree_values) + 1, 1), edgecolor='black')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

# 绘制聚类系数分布图
clustering_values = list(clustering_dict.values())
plt.hist(clustering_values, bins=20, edgecolor='black')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()