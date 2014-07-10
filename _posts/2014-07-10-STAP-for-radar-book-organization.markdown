---
date : 2014-07-10
layout : post
categories : STAP
title : STAP for Radar-Book Organization
---
###缘起###
由于研究的需要，开始阅读J.R.Guerci的**Space-Time Adaptive Processing for Radar**。本书一共有6个章节，为以后阅读的方便性和目标性，在此将第一章Introduction中的Book Organization进行摘录。

###第二章摘要###
一维均匀线性阵列（1-D ULA）自适应阵列处理的基本概念。

最优波束形成：最大化信杂噪比（SINR）。

干扰协方差矩阵：R

R未知时，利用自适应阵列进行估计。

基于自适应博士形成的样本协方差：自适应波束的特征分析，运用主成分方法，以减小由于样本有限产生的不良影响。

解决State weights problem: **CMTs**

###第三章摘要###
空载动目标显示（MTI）雷达的信号和干扰模型。

ULA雷达的地杂波二维特性，Brennan‘s rule。
杂波协方差阵估计问题。

###第四章摘要###
影响STAP性能的重要因素：

- 信道不匹配（带宽有限）
- ICM
- Antenna crabbing?
- ISL effects
- Clutter heterogeneity

###第五章摘要###
STAP算法基本原理

###第六章摘要###
6.2 STAP的统计学基础  
加性高斯白噪声模型下，基于干扰协方差矩阵，最大信杂噪比或最小均方差的空时波束形成是统计意义下的最优解。

6.3 讨论基本的实时实现（Real time complementation）问题，并着重强调了数据域（data-dormain）QR因子分解。  
高效率的并行处理方法是样本矩阵求逆（sample matrix inverse，SMI）。  
扩展：对角装载（diag-loading）， CMT：鲁棒性STAP算法。

最后引入知识辅助空时自适应处理（knowledge-aided STAP），以适应十分复杂的杂波环境。