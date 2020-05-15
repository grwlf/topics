BERT training
-------------

### Train Large, Then Compress: Rethinking Model Size for Efficient Training and Inference of Transformers

* Arxiv paper https://arxiv.org/abs/1812.06162
* Work with RoBERTa model
* Tasks:
  - EN-FR translation. Details:
    + 36M sentences for training
    + newstest2014 for validation
    + BLEU is case sensitive
  - BERT Pretraining on Wiki+BookCorpus (later replaced with smth. else).
    Details:
    + They follow RoBERTa pre-training procedures (Liu et al. 2019b)
    + Final dataset is 3.4B words, 0.5% is hold for validation
* Notes:
  - They measure wall-clock time of training models of different size
  - Conclusion: one should train larger models even on limited resourses
  - They conclude about training efficiency from the Perplexity-based validation
    of MLM pre-training. But, they conclude about compression results from the
    Accuracy-based validation of MNLI fine-tuning
  - Results:
    + Bigger models train better: Results per num.layers: `3 < 6 < (12,18,24)`.
      For example: at 250Ks : Perpl is 7.5 for 3-layer, but 6.4 for 6 layer
      models.
    + Optimal model size is linked with dataset size
    + In contrast to `Mirzadeh, 2020`, they found that larger models is _easier_
      to compress (using pruning). M. showed that it is harder, but they used
      distillation
    + Authors find connections with Lottery ticket hypothesis.
* Keywords:
  - Gradient accumulation (to fit large models in memory),
  - Lottery Ticker hypothesis (Larger models are better because there is a
    higher chance of finding lucky initializing in one of it's subnetworks).


### Scheduled DropHead: A Regularization Method for Transformer Models

* Arxiv paper https://arxiv.org/abs/2004.13342

### Training with Quantization Noise for Extreme Model Compression

* Arxiv https://arxiv.org/abs/2004.07320
* Blog https://ai.facebook.com/blog/training-with-quantization-noise-for-extreme-model-compression/
* GitHub https://github.com/pytorch/fairseq/tree/master/examples/quant_noise


### ELectra

* Blog https://ai.googleblog.com/2020/03/more-efficient-nlp-model-pre-training.html
* GitHub https://github.com/google-research/electra
