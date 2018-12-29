# Network Architecture Search 


## Table of contents
* [1. NAS introdction](#introduction)
* [2. NAS reviews](#reviews)
* [3. NAS Papers](#papers)
    * [Evolutionary Algorithms](#Evolutionary-Algorithms(EA))
    * [Reinforcement Learning](#Reinforcement-Learning(RL))
    * [Others](#Others)


## Introduction 
NAS can be seen as subfield of [AutoML](https://www.ml4aad.org/automl/) and has signicant overlap with hyper-parameter optimization and meta-learning.
In NAS, We can divide it into EA(GA) + NAS, RL + NAS(and so on...I am going to summarize them).

## Reviews
* 09.08, 2018 [Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377)  
This is the latest review of NAS.

## Papers
This block is collated by Jingwen Pan(潘婧文). Thanks for her contributions! :cake:  

### Evolutionary Algorithms(EA)
    - 2017.03.04 [Evolving Deep Neural Networks](https://arxiv.org/abs/1703.00548)

    - 2017.03.04, ICCV2017 [Genetic CNN](https://arxiv.org/abs/1703.01513)

    - 2017.06.11, ICML2017 [Large-Scale Evolution of Image Classifiers](https://arxiv.org/abs/1703.01041)

    - 2018.02.22, ICLR2018 [Hierarchical Representations for Efficient Architecture Search](https://arxiv.org/abs/1711.00436)

    - 2018.06.04, ICLR2018 [PPP-Net: Platform-aware Progressive Search for Pareto-optimal Neural Architectures](https://openreview.net/forum?id=B1NT3TAIM)

    - 2018.07.24 [Efficient Multi-objective Neural Architecture Search via Lamarckian Evolution](https://arxiv.org/abs/1804.09081)

    - 2018.07.26 [Progressive Neural Architecture Search](http://arxiv.org/abs/1712.00559)

    - 2018.10.26 [Regularized Evolution for Image Classifier Architecture Search](https://arxiv.org/abs/1802.01548)

### Reinforcement Learning(RL)
    - 2017.02.15, ICLR2017, [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578)

    - 2017.03.22, ICLR2017, [Designing Neural Network Architectures using Reinforcement Learning](https://arxiv.org/abs/1611.02167)

    - 2017.11.21, AAAI [Efficient Architecture Search by Network Transformation](https://arxiv.org/abs/1707.04873)

    - 2018.02.12 [Efficient Neural Architecture Search via Parameter Sharing](https://arxiv.org/abs/1802.03268)

    - 2018.04.11 [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012)

    - 2018.05.14, CVPR2018 [Practical Block-wise Neural Network Architecture Generation](https://arxiv.org/abs/1708.05552)

    - 2018.06.27, JMLR [MONAS: Multi-Objective Neural Architecture Search using Reinforcement Learning](https://arxiv.org/abs/1806.10332)


### Others
    - 2018.06.10 [Neural Architecture Search with Bayesian Optimisation and Optimal Transport](https://arxiv.org/abs/1802.07191)

    - 2018.09.11, NIPS2018 [Searching for Efficient Multi-Scale Architectures for Dense Image Prediction](https://arxiv.org/abs/1809.04184)

    - 2018.10.31 [Neural Architecture Optimization](https://arxiv.org/abs/1808.07233)

### arXiv
    - 2018.08.30 [Searching Toward Pareto-Optimal Device-Aware Neural Architectures](https://arxiv.org/pdf/1808.09830.pdf)

    - 2018.09.05 [Neural Architecture Optimization](https://arxiv.org/abs/1808.07233)

    - 2018.09.07 [Reinforced Evolutionary Neural Architecture Search](https://arxiv.org/abs/1808.00193)

    - 2018.10.04 [Aging Evolution for Image Classifier Architecture Search](https://arxiv.org/pdf/1802.01548)  
    This paper proposed a new idea removing oldest individual rather than worest performance individual in order to gain wider search ability.  
    
    - 2018.10.08 [NSGA-NET: A Multi-Objective Genetic Algorithm for Neural Architecture Search](https://arxiv.org/abs/1810.03522)  
    This paper proposed a NAS framework based on MOEA. 

    - 2018.10.10 [Automatic Configuration of Deep Neural Networks with Parallel Efficient Global Optimization](https://arxiv.org/abs/1810.05526)
    
    - 2018.10.12 [Graph Hypernetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)
    
    - 2018.10.16 [Evolutionary Stochastic Gradient Descent for Optimization of Deep Neural Networks](https://arxiv.org/abs/1810.06773)

   

<!-- 1. Translation lgtm articles  
None -->

<!-- ## Citations
If this is a lgtm repo which you want to use, please consider citing my repo as follows:


```
@Misc{Network Architecture Search Notebook
    title = {Network Architecture Search Notebook},
    author = {Shichen, peng},  
}
``` -->
