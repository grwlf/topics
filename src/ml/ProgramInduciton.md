Program Induction
-----------------

* https://arxiv.org/pdf/2008.07912.pdf
  - WIP
  - Surwey

* https://arxiv.org/abs/2003.09040
  - TF-Coder: Program Synthesis for Tensor Manipulations
  - 2020, Kensen Shi
  - Describes *TF-Coder*
  - PwC https://paperswithcode.com/paper/tf-coder-program-synthesis-for-tensor
  - GitHub https://github.com/google-research/tensorflow-coder

* https://arxiv.org/abs/2007.03132
  - Learning to learn generative programs with Memoised Wake-Sleep
  - 2020, Hewitt
  - Supposedely describes Generative Probabilistic Regex

* http://learningsys.org/sosp19/assets/papers/22_CameraReadySubmission_Abstract___SOSP__19_ML_Sys_workshop-4.pdf
  - The Case for a Learned Sorting Algorithm
  - 2020 June, Ani Kristo, SIGMOD'20
  - Describes *MER-Sort* (Model-Enhanced Radix Sort)

* https://arxiv.org/abs/2006.08381
  - DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep
    Bayesian program learning
  - 2020 June 15, Kevin Ellis
  - Describes *DreamCoder*
  - PwC https://paperswithcode.com/paper/dreamcoder-growing-generalizable
  - [Supplementary
    materials](https://web.mit.edu/ellisk/www/dreamcodersupplement.pdf)
    Unfortunately, it looks like supplementary has a recursive links to the
    parent paper.
  - [GitHub link](https://github.com/ellisk42/ec)
  - References:
    + RobustFill
    + DeepCoder
    + Candidate structures (as in Liang, 2010)
    + FlashFill (13)

* https://arxiv.org/abs/2006.06762
  - Ansor: Generating High-Performance Tensor Programs for Deep Learning
  - 2020 June 11, Lianmin Zheng

* https://arxiv.org/abs/1912.12345
  - Synthetic Datasets for Neural Program Synthesis
  - 2019 Dec 27, Richard Shin

* https://arxiv.org/pdf/1902.06349.pdf
  - Learning to Infer Program Sketches
  - 2019

* https://arxiv.org/pdf/1703.05698v5.pdf
  - Neural Sketch Learning for Conditional Program Generation
  - 2018
  - PwC https://paperswithcode.com/paper/neural-sketch-learning-for-conditional
  - GitHub https://github.com/trishullab/bayou

* https://arxiv.org/abs/1805.08166
  - Learning to Optimize Tensor Programs
  - 2018, Tianqi Chen
  - Describes *AutoTVM* of TVM

* https://papers.nips.cc/paper/6803-neural-program-meta-induction
  - Neural Program Meta-Induction
  - 2017
  - Describes *RobustFill*

* https://arxiv.org/abs/1611.01989
  - DeepCoder: Learning to Write Programs
  - 2016, Balog
  - Describes *DeepCoder*
  - PwC: https://paperswithcode.com/paper/deepcoder-learning-to-write-programs

* https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/popl11-synthesis.pdf
  - Automating string processing in spreadsheets using input-output examples.
  - 2016, Gulwani
  - Describes *FlashFill* (TODO: check)

* https://people.eecs.berkeley.edu/~jordan/papers/liang-jordan-klein-icml10.pdf
  - Learning programs: A hierarchical bayesian approach.
  - 2010, Liang

Details on DreamCoder
---------------------

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
  ```
  Our abstraction sleep algorithm works through automatic refactoring,
  discovering and incorporating into the library syntax trees which are not
  present in the surface form of programs available to the learner.
  ```

Resources
---------

* https://www.arxiv-vanity.com/


