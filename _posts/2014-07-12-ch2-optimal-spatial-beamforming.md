---
layout: post
title: "ch2 最优空域波束形成"
description: ""
category: STAP for Radar
tags: [STAP,Beamforming]
---
<!-- {% include JB/setup %} -->
最优空域波束形成的内容位于书中的2.2节，首先对随机相位信号的最优波束形成进行推导，接下来引入随机干扰量（包括热噪声、干扰信号和杂波），建立信噪比最优的波束形成问题，最后对加性白噪声和加性色噪声两种特殊情形下的最优波束形成问题进行研究。

##随机相位波束形成##
假设接收的电磁波是单位幅度的窄带平面波，接收的天线阵列是N元均匀线性阵列(ULA)，模型如下图所示:


<img class="center" src="/public/img/STAP_figure2_1.png" alt="STAP_figure2_1"  width="500px"/>  


阵元间距：d  
窄带B限制条件：$$\frac{c}{B}>>Nd$$，以确保传播延时可转换成相移，方便处理。在第4章中进一步研究带宽有限造成的影响。  
波达角度（AOA）:$$\theta_{0}$$  
第$$n$$个阵列元接收信号用基带复包络信号表示为：  
\begin{equation}
    S\_{n}=e^{j2\pi(n-1)\frac{d}{\lambda}\sin{\theta\_{0}}}， n=1,\cdots,N  
\end{equation}
其中,$$\lambda$$: 电磁波波长。

空域波束形成，即使输出响应在某一方向$$\theta_{0}$$最大。数学模型表示为：
\begin{equation}
    y = \sum\_{n=1}^{N}w\_{n}^{*}s\_{n}=\mathbf{w}^{'}\mathbf{s}
\end{equation}  






