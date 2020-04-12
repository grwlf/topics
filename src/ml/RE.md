Relation Extraction
===================

### Matching the Blanks: Distributional Similarity for Relation Learning

* <https://arxiv.org/pdf/1906.03158v1.pdf>, Soares et al, 2019
* Describes how to apply Transformer (BERT) to RE
* Use "Matching the blank" techniqe
* Requires access to datasets which maps text to some kind of unique entity
  identifiers.
* Datasets mentioned:
  - TACRED (?)
  - FewRel (a task released recently)
  - KBP-37
  - SemEval 2010, task 8
* The approximate goal is to learn relation embedding `h=f_theta(r)`, where
  `r:=(x,s1,s2)` is a relation, `s1,s2:=(a,b)` is an entity representation,
  `a,b` - indices in sentence.
* Authors split the tasks they use in two groups:
  1. Superwised tasks is: given a relation `r`, predict its type `t` using a
     fixed dictionary of types (t=0 means no relation). (Datasets: all except
     FewRel)
  2. Few-shot matching: match query relation type with not-known in advance
     types of several example relations.

