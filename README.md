# Implementation of algorithms in PCFG

## What is it

Implementation of Expectation Maximation algorithm to calculate probabilities of rules in Context-Free Grammar (CFG) in order to create Probabilistic Context-Free Grammar (PCFG). It also generates new sentences in that grammar using a PCFG (.gen file).

## What do you need to run it

* .cfg file

File with a context-free grammar in Chomsky normal form, but with "#" instead of arrow (no spaces around).

Rule example:

```
S#NPa ViADV
```

* .train file

Text file with .train extention with sentences you want to train your grammar on. Sentences should be in separate lines.


## How to run it

* Running examples:
	Uncomment a line in train.py file with one of the examples

* Running on your own grammars:
	Change train.py to:

```python
if __name__ == '__main__':
    train('[YOUR_CFG_FILE].cfg','[YOUR_TRAIN_FILE].train')
```


## References
+	[Inside–outside algorithm](https://en.wikipedia.org/wiki/Inside–outside_algorithm)
+	[The Inside-Outside Algorithm](http://www.cs.columbia.edu/~mcollins/io.pdf)
+ 	[Note on the Inside-Outside Algorithm](https://www.cs.jhu.edu/~jason/465/iobasics.pdf)
