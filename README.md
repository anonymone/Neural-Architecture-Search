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
1. EA(GA) + NAS
    -  2017.03.04  [Genetic CNN](http://cn.arxiv.org/abs/1703.01513)  
    This paper is the first paper I read in structure searching area. In this paper, Xie had proposed a simple way to encode the network's structure(with some drawbacks).And using GA as a auto-design tool to find high performance structure of CNNs. [[Code]](https://github.com/aqibsaeed/Genetic-CNN)  

1. arXiv
    - 2018.02.12 [Efficient Neural Architecture Search via Parameter Sharing](https://arxiv.org/abs/1802.03268)  
    This paper proposed a idea of boosting training process by applying transfer learning. This work's base assumption is that Transfer learning can obtain a not-bad model in limited time.
    You can find a unofficial repetition [[Code]](https://github.com/melodyguan/enas)

    - 2018.10.04 [Aging Evolution for Image Classifier Architecture Search](https://arxiv.org/pdf/1802.01548)  
    This paper proposed a new idea removing oldest individual rather than worest performance individual in order to recive wider search ability.  

1. Translation lgtm articles  
None


