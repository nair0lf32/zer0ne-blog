---
title: "Gunship"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

Its a "very easy" web challenge so lets speedrun it

We got the source code of the website.

it runs node js and listens on port 1337

I didnt find anything helpful first

Tried to look for classics, XSS, Sqli, command injecton on the website...

But that didnt help

looked at the dependencies in `packages.json` and their known vulnerabilities

- express : RCE? (version)

- pug :  AST injection, prototype pollution

- flat : prototpe pollution

Google `"prototype pollution"`

the submit endpoint in `index.js` route uses `"unflatten"`

Its definitely that!

```js
router.post('/api/submit', (req, res) => {
    const { artist } = unflatten(req.body);

	if (artist.name.includes('Haigh') || artist.name.includes('Westaway') || artist.name.includes('Gingell')) {
		return res.json({
			'response': pug.compile('span Hello #{user}, thank you for letting us know!')({ user: 'guest' })
		});
	} else {
		return res.json({
			'response': 'Please provide us with the full name of an existing member.'
		});
	}
});

```

Time to exploit it! (that is the funny part)

Found many articles explaining it and my first Poc was from [here!](https://blog.p6.is/AST-Injection/)

But blindly modifying it wont help you...you have to know what you are doing

Actually many articles explain `AST injection` and `Prototype pollution`

This one by example focus on the "unflatten" usage vuln from `flat` dependency

This vulneraility also exist in `pug` with usage of `pug.compile()`

And that is what itt's about here! The author modified the challenge to make it less obvious (probably)

And it works! If you used an old writeup blindly you would be confused as the old exploit wonn't work as it is

I made my "exploit.py" using this article [here](https://www.linkedin.com/pulse/ast-injection-prototype-pollution-joshua-berben)!

```bash
└──╼ $python exploit.py
{"response":"<span>Hello guestndefine, thank you for letting us know!</span>"}
flagLWO4w
index.js
node_modules
package.json
routes
static
views
yarn.lock

```

After enumerating the directory with `ls` we modify the script again

Now that we know the flag name we just read it with `cat`

```bash
└──╼ $python exploit.py
{"response":"<span>Hello guestndefine, thank you for letting us know!</span>"}
HTB{f1gh7ing_4ga1nst_p0llut1on!}

```

Ah yes the "very easy" challenges of hackthebox
Very nice machine but I personally rated this as medium
** added the source code as a zip file for github security reasons.
you know the password already: **hackthebox**
