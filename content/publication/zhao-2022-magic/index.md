---
title: "MAGIC: Microlensing Analysis Guided by Intelligent Computation"
date: 2022-10-14
authors: ["Haimeng Zhao", "Wei Zhu"]
publication_types: ["2"]
abstract: "The modeling of binary microlensing light curves via the standard sampling-based method can be challenging, because of the time-consuming light curve computation and the pathological likelihood landscape in the high-dimensional parameter space. In this work, we present MAGIC, which is a machine learning framework to efficiently and accurately infer the microlensing parameters of binary events with realistic data quality. In MAGIC, binary microlensing parameters are divided into two groups and inferred separately with different neural networks. The key feature of MAGIC is the introduction of neural controlled differential equation, which provides the capability to handle light curves with irregular sampling and large data gaps. Based on simulated light curves, we show that MAGIC can achieve fractional uncertainties of a few percent on the binary mass ratio and separation. We also test MAGIC on a real microlensing event. MAGIC is able to locate the degenerate solutions even when large data gaps are introduced. As irregular samplings are common in astronomical surveys, our method also has implications to other studies that involve time series."
featured: true
publication: "The Astronomical Journal, 164(5), 192."
url_pdf: "https://iopscience.iop.org/article/10.3847/1538-3881/ac9230/pdf"
url_code: "https://github.com/JasonZHM/magic-microlensing"
links:
- name: Conf
  url: 'https://ml4astro.github.io/icml2022/assets/6.pdf'
- name: Talk
  url: 'https://hmzhao.me/files/conf-AI4Astro.mp4'
---

