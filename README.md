# Neural Architecture Search

## Tabel of contents
* [1. NAS introdction](#introduction)
* [2. NAS reviews](#reviews)
* [3. Papers](#papers)

## Introduction

The list includes the papers related to NAS I have read. All of them are grouped into three classes ( Search Space, Seach strategy and evaluation strategy) based on my subjectivity.

## Papers
### Reviews
|Data|Title|Venue|Notes|  
|:---|:---:|:--:|:---:|
|2018|[Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377)|JMLR|-|
|2008|[Neuroevolution: From Architectures to Learning](https://link.springer.com/article/10.1007/s12065-007-0002-4)|Evolutionary Intelligence|-|
|1999|[Evolving Artificial Neural Networks](https://ieeexplore.ieee.org/document/784219/)|IEEE|-|

### Search Space / Encoding strategies
|Data|Title|Venue|Code|Notes|  
|:---|:----:|:--:|:--:|:---:|
|2018|[Neural Architecture Search Over a Graph Search Space](https://arxiv.org/abs/1812.10666)|-|-|This paper defined a search space on direct graph which is used to instruct the construction of networks.|
|2017|[Genetic CNN](https://arxiv.org/abs/1703.01513)|ICCV|[Tensorflow](https://github.com/aqibsaeed/Genetic-CNN)|This paper proposed a binary string encoding strategy.|
|2017/18|[Efficient Architecture Search by Network Transformation](https://arxiv.org/abs/1707.04873)|AAAI|-|This paper Proposed a popular block based network definition method.|
|2009|[A Hypercube-based Encoding for Evolving large-scale Neural Networks](https://ieeexplore.ieee.org/document/6792316/)|IEEE Artificial Life|-|This method use a extended CPPNs to encode the ANN.|
|2006|[Evolutionary Design of Neural Network Architectures Using a Descriptive Encoding Language](https://ieeexplore.ieee.org/abstract/document/4016064)| IEEE TEVC| - | This paper proposed a human-readable and writable encoding method. |
|2002|[Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)| EC| -| [NEAT: An Awesome Approach to NeuroEvolution](https://towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f)|
|1998| [Network Generating Attribute grammar Encoding](https://ieeexplore.ieee.org/abstract/document/682305/) | IJCNN | - | Grammar Encoding |
|1996| [A comparison between cellular encoding and direct encoding for genetic neural networks](https://dl.acm.org/citation.cfm?id=1595547) | - | - | This paper compared the celluar encoding and direct encoding methods |
|1996|[Evolving Graphs and Networks with Edge encoding: preliminary report](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.9718&rep=rep1&type=pdf)| The Genetic Programming Conference | - | Edge Encoding method. |
|1994 | [Neurogenetic learning: an integrated method of designing and training neural networks using genetic algorithms](https://www.sciencedirect.com/science/article/abs/pii/0167278994902852) | Physica D | - | This paper inspired by L-System. |
|1994| [Automatic definition of modular neural networks](https://journals.sagepub.com/doi/abs/10.1177/105971239400300202) | Adaptive behavior | - | - |
|1990|[Designing Neural Networks Using Genetic Algorithms with Graph Generation System](http://www.complex-systems.com/abstracts/v04_i04_a06/) | The Conference on Genetic Algorithms | - | This paper proposed a graph grammatical encoding and analysed the problems of the direct encoding method.|

### Search Strategies
|Data|Title|Venue|Code|Notes|  
|:---|:----:|:--:|:--:|:---:|
|2018|[Reinforced Evolutionary Neural Architecture Search](https://arxiv.org/abs/1808.00193)|CVPR|[mxnet](https://github.com/yukang2017/RENAS)| EA/RL|
|2018|[Neural Architecture Optimization](https://arxiv.org/abs/1808.07233)|NeurIPS|[Pytorch](https://github.com/renqianluo/NAO_pytorch) [Tensorflow](https://github.com/renqianluo/NAO)| Gradient Based|
|2018|[NSGA-NET: A Multi-Objective Genetic Algorithm for Neural Architecture Search](https://arxiv.org/abs/1810.03522)|GECCO|-|This paper can be viewed as an extension of Genetic CNN in search strategy and slightly improving in encoding strategy.|
|2017|[Large-Scale Evolution of Image Classifiers](https://arxiv.org/abs/1711.00436)|ICML|-|Google's work. Trying to prove the possibility of evolving CNN automatically.|
|2017|[SMASH: One-Shot Model Architecture Search through HyperNetworks](https://arxiv.org/abs/1708.05344)|NeurIPS|-|Gradient Based|
|2017|[Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578)|ICLR 2017|-| RL|
|2017|[Designing Neural Network Architectures using Reinforcement Learning](https://arxiv.org/abs/1611.02167)|ICLR|-|RL|

### Evaluation Strategies
|Data|Title|Venue|Code|Notes|  
|:---|:----:|:--:|:--:|:---:|
|2018|[Progressive Neural Architecture Search](http://arxiv.org/abs/1712.00559)|ECCV|[Pytorch](https://github.com/chenxi116/PNASNet.pytorch) [Tensorflow](https://github.com/chenxi116/PNASNet.TF)| This paper use a predictor to evaluate the acc of each network with few real training.|

### Extension
|Data|Title|Venue|Code|Notes|  
|:---|:----:|:--:|:--:|:---:|
|2019|[NAS-Bench-101: Towards Reproducible Neural Architecture Search](https://arxiv.org/abs/1902.09635v1)|ICML| [Code](https://github.com/google-research/nasbench)| A Benchmark of NAS.|
|2016|[Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641)|ICLR 2016|-|This paper proposed a mehtod (similar to parameters sharing) to transfer the knowledge from previous network to a larger one.|

## Useful pages
1. [LITERATURE ON NEURAL ARCHITECTURE SEARCH](https://www.automl.org/automl/literature-on-neural-architecture-search/)
1. [Awesome NAS](https://github.com/D-X-Y/Awesome-NAS/blob/master/README.md)
