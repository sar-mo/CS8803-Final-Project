from torch_geometric.datasets import FacebookPagePage, Twitch
import torch_geometric.transforms as T
from torch_geometric.utils import to_dgl
from gnnlens import Writer
import os

data_dir = './data'
facebook_dataset = FacebookPagePage(os.path.join(data_dir, 'FacebookPagePage'), transform=T.NormalizeFeatures())
facebook_graph = facebook_dataset[0]
facebook_labels = facebook_graph.y
facebook_num_classes = facebook_dataset.num_classes
facebook_dgl_graph = to_dgl(facebook_graph)

twitch_dataset = Twitch(os.path.join(data_dir, 'Twitch'), transform=T.NormalizeFeatures(), name='DE')
twitch_graph = twitch_dataset[0]
twitch_labels = twitch_graph.y
twitch_num_classes = twitch_dataset.num_classes
twitch_dgl_graph = to_dgl(twitch_graph)

print(twitch_graph)
print(facebook_graph)

writer = Writer('graphs/unlearning_graphs')
writer.add_graph(name='Facebook', graph=facebook_dgl_graph,
                 nlabels=facebook_labels, num_nlabel_types=facebook_num_classes)
writer.add_graph(name='Twitch', graph=twitch_dgl_graph,
                    nlabels=twitch_labels, num_nlabel_types=twitch_num_classes)
writer.close()