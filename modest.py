from itertools import chain
import textwrap

with open("mod_prop_min.txt","r") as f:
    full_text = f.read()

paragraphs = full_text.split("\n\n")

paragraphs_no_n = [p.replace("\n"," ") for p in paragraphs]

wrapped = list(chain.from_iterable([textwrap.wrap(p,270) for p in paragraphs_no_n]))

t = len(wrapped)
wrapped_n = [ l + f' [{n+1}/{t}]' for n, l in enumerate(wrapped)]

with open('mod_prop_tweetable.txt', 'wt') as f:
    f.writelines(l + '\n' for l in wrapped_n)

with open('mod_prop_tweetable.txt') as f:
    wrapped_n = [line.rstrip() for line in f]