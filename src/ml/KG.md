Knowlege graphs
===============

### Differentiable Reasoning over a Virtual Knowledge Base

- <https://arxiv.org/abs/2002.10640>
- Referenced topics:
  * Shrivastava, 2014, Maximum inner product search (MIPS), appoximate
    algorithms
  * Seo et al, 2018, Phrase-inexed question answering (PIQA)
  * Seo et al, 2016, Bi-directional attention flow for machine comprehension
  * Cohen et al, 2019, Multi-hop questions against explicit KB
- Referenced datasets:
  * HotpotQA, Yang et al, 2018
  * WikiDATA, for mention encoding
  * SLING
  * MetaQA
- The paper is said to address the limitation of Pharse-indexed QA introduced
  by Shrivastava(?), by encoding the text corpus in a query-independent manner
- Reference TF RaggedTensors. Maybe implemented in TF


### Phrase-Indexed Question Answering: A New Challenge for Scalable Document Comprehen

- <https://arxiv.org/abs/1804.07726> by Seo et al, 2018
- Defines a leaderboard <https://github.com/uwnlp/piqa>
- Idea: make encoding of the question not depend on the encoding of the document
