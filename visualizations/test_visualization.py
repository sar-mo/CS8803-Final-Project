from dgl.data import CoraGraphDataset, CiteseerGraphDataset
from gnnlens import Writer

cora_dataset = CoraGraphDataset()
cora_graph = cora_dataset[0]
citeseer_dataset = CiteseerGraphDataset()
citeseer_graph = citeseer_dataset[0]

# Specify the path to create a new directory for dumping data files.
writer = Writer('graphs/test_graph')
writer.add_graph(name='Cora', graph=cora_graph)
writer.add_graph(name='Citeseer', graph=citeseer_graph)
# Finish dumping
writer.close()