---
title: "Debugging Interface"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

First after unzipping the initial archive my stupid head thought it was another archive in it and I extracted that too...because the GUI fooled me

don't do that...pay attention to the `.sal` extension

what is that? good question! let's ask google

among many results and refferences to sql application language, I found [THIS!](https://discuss.saleae.com/t/utilities-for-sal-files/725)

Google about how to use that...took me some time

add Midi analyser in `analyzers` panel

then in `data` choose terminal...you may use `restart` on analyzer to query data again

But you would be able to see the flag already in the data

```text
 Activity from: HTB{super_dupper_mega_long_flag_debug_here}\r\n
```
