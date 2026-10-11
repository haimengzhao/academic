---
title: "Exponential quantum advantage in processing massive classical data"
date: 2026-04-08
publishDate:
authors: ["Haimeng Zhao", "Alexander Zlokapa", "Hartmut Neven", "Ryan Babbush", "John Preskill", "Jarrod R. McClean", "Hsin-Yuan Huang"]
publication_types: ["3"]
categories: ["quantum"]
abstract: "Broadly applicable quantum advantage, particularly in classical data processing and machine learning, has been a fundamental open problem. In this work, we prove that a small quantum computer of polylogarithmic size can perform large-scale classification and dimension reduction on massive classical data by processing samples on the fly, whereas any classical machine achieving the same prediction performance requires exponentially larger size. Furthermore, classical machines that are exponentially larger yet below the required size need superpolynomially more samples and time. We validate these quantum advantages in real-world applications, including single-cell RNA sequencing and movie review sentiment analysis, demonstrating four to six orders of magnitude reduction in size with fewer than 60 logical qubits. These quantum advantages are enabled by quantum oracle sketching, an algorithm for accessing the classical world in quantum superposition using only random classical data samples. Combined with classical shadows, our algorithm circumvents the data loading and readout bottleneck to construct succinct classical models from massive classical data, a task provably impossible for any classical machine that is not exponentially larger than the quantum machine. These quantum advantages persist even when classical machines are granted unlimited time or if BPP=BQP, and rely only on the correctness of quantum mechanics. Together, our results establish machine learning on classical data as a broad and natural domain of quantum advantage and a fundamental test of quantum mechanics at the complexity frontier."
featured: true
publication: "arXiv:2604.07639"
url_pdf: "https://arxiv.org/pdf/2604.07639"
url_code: "https://github.com/haimengzhao/quantum-oracle-sketching"
links:
- name: Blog
  url: 'https://quantumfrontiers.com/2026/04/09/unleashing-the-advantage-of-quantum-ai/'
- name: Talk
  url: 'https://hmzhao.me/files/memory-advantage.pdf'
---
