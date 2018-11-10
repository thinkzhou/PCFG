# Implementation of algorithms in PCFG

## What is it

Implementation of the Expectation Maximation algorithm to calculate probabilities of rules in Context-Free Grammar (CFG) in order to create Probabilistic Context-Free Grammar (PCFG). It also generates new sentences in that grammar using a PCFG (.gen file).

## What do you need to run it

* .cfg file

A file with a context-free grammar in Chomsky normal form, but with "#" instead of an arrow (no spaces around).

Rule example:

```
S#NPa ViADV
```

* .train file

A text file with .train extension with sentences you want to train your grammar on. Sentences should be in separate lines.


## How to run it

In the command line, type:

```bash
python train.py [YOUR_GRAMMAR_FILE].cfg [YOUR_TRAIN_FILE].train
```

You can use some examples in the test folder, or try your own.


## References
+    [Inside–outside algorithm](https://en.wikipedia.org/wiki/Inside–outside_algorithm)

+    [The Inside-Outside Algorithm](http://www.cs.columbia.edu/~mcollins/io.pdf)

+    [Note on the Inside-Outside Algorithm](https://www.cs.jhu.edu/~jason/465/iobasics.pdf)
