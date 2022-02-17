---
title: Why you don't need the builder Pattern in Python
description: We will talk about the builder Pattern and how it fits in the Python language. TLDR do not use it.
image: https://bulma.io/images/bulma-logo.png
createdAt: 2022-01-23
tags: Python,Design Patterns,Opinion
---

<text-index>
<template #test>
<text-index-anchor anchor_id="title" title="Testing title"></text-index-anchor>
<text-index-anchor anchor_id="content" title="Testing content"></text-index-anchor>
<text-index-anchor anchor_id="code" title="Testing code"></text-index-anchor>
</template>
</text-index>




<text-title anchor_id="title">
<template #content>
Lets have a look at this actually
</template>
</text-title>

<text-block anchor_id="content" title="We shoudln't use this actually hahaa">
<template #cont>
Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has 
survived not only five centuries, but also the leap
into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the
release of Letraset sheets containing Lorem Ipsum 
passages, and more recently with desktop publishing 
software like Aldus PageMaker including versions of 
Lorem Ipsum.
</template>
</text-block>

<code-snippet anchor_id="code" :clipboard="true" class="pt-5" language="Python" version="3.5" content="
def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total
">
</code-snippet>


<text-block>
<template #cont>
Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s
</template>
</text-block>
