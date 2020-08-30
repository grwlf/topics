Program Induction
-----------------

* https://arxiv.org/pdf/2008.07912.pdf
  - WIP
  - Surwey

* https://arxiv.org/abs/2007.03132
  - 2020, Hewitt, Learning to learn generative programs with Memoised Wake-Sleep
  - Supposedely describes Generative Probabilistic Regex

* https://arxiv.org/abs/2006.08381
  - 2020, DreamCoder: Growing generalizable, interpretable knowledge with
    wake-sleep Bayesian program learning
  - PwC https://paperswithcode.com/paper/dreamcoder-growing-generalizable
  - Supplementary materials:
    https://web.mit.edu/ellisk/www/dreamcodersupplement.pdf Unfortunately, it
    looks like supplementary has a recursive links to the parent paper.
  - References:
    + RobustFill
    + DeepCoder
    + Candidate structures (as in Liang, 2010)
    + FlashFill (13)

* https://arxiv.org/pdf/1902.06349.pdf
  - 2019, Learning to Infer Program Sketches

* https://arxiv.org/pdf/1703.05698v5.pdf
  - 2018, Neural Sketch Learning for Conditional Program Generation
  - PwC https://paperswithcode.com/paper/neural-sketch-learning-for-conditional
  - GitHub https://github.com/trishullab/bayou

* https://papers.nips.cc/paper/6803-neural-program-meta-induction
  - 2017, Neural Program Meta-Induction
  - *RobustFill* originates from this paper

* https://arxiv.org/abs/2007.03132
  - 2017, Balog, DeepCoder: Learning to Write Programs
  - *DeepCoder* described here

* https://people.eecs.berkeley.edu/~jordan/papers/liang-jordan-klein-icml10.pdf
  - 2010, Liang, Learning programs: A hierarchical bayesian approach.

* https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/popl11-synthesis.pdf
  - 2016, Gulwani, Automating string processing in spreadsheets using
    input-output examples.
  - FlashFill originates from here (TODO: check)

DreamCoder
----------

### Tasks

* List Processing
* Text Editing
  - Task references [Syntax-Guided Synthesis (SyGuS) competitions](https://sygus.org/)
* LOGO Graphics
* Tower Building
* Probabilistic Generative Regexes
  - Somehow related to Hewitt, 2020, https://arxiv.org/abs/2007.03132
* Symbolic regression: Programs for Smooth Trajectories
* Learning a language for physical laws
* Learning a language of recursive functions

### Program synthesis

* RobustFill - Draw next program component from autoregressive NN model
* DeepCoder - Discriminatively classifies whether or not DSL primitive will be
  used in program at least once. Model is run once per input/output sample.
* DreamCoder - Model outputs the probability of using DSL primitive, conditioned
  on its local syntactic context. This allows to:
  - Provide information on structure of resulting program
  - Break syntactic symmetries in the solution space (???)

### Learning new code abstractions

Existing methods:

* Memoization
* Reused command sequence
* Antiunification (caching reused tree-templates wich unify with program syntax
  tree, ???)
* DreamCoder:
  ``` Our abstraction sleep algorithm works through automatic refactoring,
  discovering and incorporating into the library syntax trees which are not
  present in the surface form of programs available to the learner.```




