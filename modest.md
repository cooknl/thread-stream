# A Modest Twitter Thread

## Content

http://www.gutenberg.org/files/1080/1080-0.txt

Downloaded using `curl`, but didn't have `curl`, so

```bash
sudo apt get install curl
```

Then
```bash
curl http://www.gutenberg.org/files/1080/1080-0.txt > mod_prop.txt
```

## `mod_prop_min.txt`

Manually remove all the preamble and post-matter, including title and author.

## Conversion to tweet-size lines

Read in full text

```python
with open("mod_prop_min.txt","r") as f:
    full_text = f.read()
```

Split by `\n\n` to get paragraphs preserved.

```python
paragraphs = full_text.split("\n\n")
```

Then replace newlines within paragraphs by spaces.

```python
paragraphs_no_n = [p.replace("\n"," ") for p in paragraphs]
```

Now to divide into 270 character chunks. `textwrap()` and `chain()` to the rescue!

```python
import textwrap
from itertools import chain
wrapped = list(chain.from_iterable([textwrap.wrap(p,270) for p in paragraphs_no_n]))
```

Let's add "1/n" to the end of each line

```python
t = len(wrapped)
wrapped_n = [ l + f'{n+1}/{t}' for n, l in enumerate(wrapped)]
```

Let's write it to a file for safe keeping

```python
with open('mod_prop_tweetable.txt', 'wt') as f:
    f.writelines(l + '\n' for l in wrapped_n)
```

This is how to read it back in without newline characters

```python
with open('mod_prop_tweetable.txt') as f:
    wrapped_n = [line.rstrip() for line in f]
```

## `excode`

Small diversion to modify `excode` package to make test bundling optional.

https://github.com/cooknl/excode

## The Twitter API

TODO:
