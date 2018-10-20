# Network Architecture Search 

## Newcomer tutorials 
* Evolution Algorithm
    - [莫烦Python 进化算法 简介](https://morvanzhou.github.io/tutorials/machine-learning/evolutionary-algorithm/1-01-intro/) 
    - [A fast and elitist multiobjective genetic algorithm: NSGA-II](https://ieeexplore.ieee.org/document/996017)  
    NSGAII is the most popular Evolution algorithm. And it's also the best EA paper for newcomer.(Because I did this LOL.)  
    And you can find NAGAII and Other EA's code [HERE](./Code/).
* AutoML & NAS
    - [Everything you need to know about AutoML and Neural Architecture Search](https://towardsdatascience.com/everything-you-need-to-know-about-automl-and-neural-architecture-search-8db1863682bf)  
    If you are in China, you have to browse this webpage by using some magic-you-known tools(VPN). But worth for it.


## Table of contents
* [1. NAS introdction](#1introduction)
* [2. NAS reviews](#2reviews)
* [3. NAS Papers](#3papers)
* 4.Code
* 5.Dataset

## 1.Introduction 
NAS can be seen as subfield of [AutoML](https://www.ml4aad.org/automl/) and has signicant overlap with hyper-parameter optimization and meta-learning.
In NAS, We can divide it into EA(GA) + NAS, RL + NAS(and so on...I am going to summarize them).

## 2.Reviews
* 09.08, 2018 [Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377)  
This is the latest review of NAS.

## 3.Papers
This block is collated by Jinwen Pan(潘婧文). Thanks for her contributions!

1. Read notes
    - 2018.02.12, ICML2018, [Efficient Neural Architecture Search via Parameter Sharing](https://arxiv.org/abs/1802.03268)  
    This paper proposed a idea of boosting training process by applying transfer learning. This work's base assumption is that Transfer learning can obtain a not-bad model in limited time.
    You can find a unofficial repetition [[Code]](https://github.com/melodyguan/enas)

    - 2017.03.04, ICCV, [Genetic CNN](http://openaccess.thecvf.com/content_ICCV_2017/papers/Xie_Genetic_CNN_ICCV_2017_paper.pdf)  
    This paper is the first paper I read in structure searching area. In this paper, Xie had proposed a simple way to encode the network's structure(with some drawbacks).And using GA as a auto-design tool to find high performance structure of CNNs. [[Code]](https://github.com/aqibsaeed/Genetic-CNN)  

    - 2018.08.01 [Efficient Progressive Neural Architecture Search](https://arxiv.org/pdf/1808.00391.pdf)
    
1. arXiv
    - 2018.08.30 [Searching Toward Pareto-Optimal Device-Aware Neural Architectures](https://arxiv.org/pdf/1808.09830.pdf)

    - 2018.09.05 [Neural Architecture Optimization](https://arxiv.org/pdf/1808.07233.pdf)

    - 2018.09.07 [Reinforced Evolutionary Neural Architecture Search](https://arxiv.org/pdf/1808.00193.pdf)

    - 2018.10.04 [Aging Evolution for Image Classifier Architecture Search](https://arxiv.org/pdf/1802.01548)  
    This paper proposed a new idea removing oldest individual rather than worest performance individual in order to gain wider search ability.  
    
    - 2018.10.10 [Automatic Configuration of Deep Neural Networks with Parallel Efficient Global Optimization](https://arxiv.org/pdf/1810.05526.pdf)
    
    - 2018.10.12 [Graph Hypernetworks for Neural Architecture Search](https://arxiv.org/pdf/1810.05749.pdf)
    
    - 2018.10.16 [Evolutionary Stochastic Gradient Descent for Optimization of Deep Neural Networks](https://arxiv.org/pdf/1810.06773.pdf)

    - 2018.10.08 [NSGA-NET: A Multi-Objective Genetic Algorithm for Neural Architecture Search](https://arxiv.org/abs/1810.03522)  
    This paper proposed a NAS framework based on MOEA. 

1. Translation lgtm articles  
None

## Citations
If this is a lgtm repo which you want to use, please consider citing my repo as follows:


```
@Misc{Network Architecture Search Notebook
    title = {Network Architecture Search Notebook},
    author = {Shichen, peng},  
}
```
