# Zer0ne Blog

![logo](static/pictures/dark_logo.png "credits: this logo is inspired from Genegoldstein's work for izzy deluxe in the living tombstone's hunter song")

Hello friend 🤖,

I am *nairolf32*, A cybersecurity enthusiast slowly getting stronger. I Play CTFs and challenges on various websites and decided to keep a track of what I already know/did/learnt by writing it down. Here is a good place for that. This repository used to simply host my ctf writeups but I turnt it into my cybersec blog and here I share the best things I learnt throughout my learning journey. The writeups are from many platforms. My favorites ones are Tryhackme and Hackthebox. The writeups are mostly from those platforms.

You can click [here](http://zer0ne-hub.github.io/zer0ne-blog/about/) to learn more about this blog!

## Usage

This repository is not really open for external contributions but feel free to open an issue for anything you want to share. For further usage simply clone the repo with `git clone` and run `hugo` (it manages everything for you)

Most importantly, as I use a submodule theme you need to get it locally too using `git submodule init`then `git submodule update`. This is deployed with `github pages + actions`. To test it run below commands:

- `hugo server` for local development (you might need to override the baseURL in the config file
using the `--baseURL=http://localhost:1313` flag)
- `hugo -D` for building the website

Check [hugo website](https://gohugo.io/) for more information about this great static site generator
