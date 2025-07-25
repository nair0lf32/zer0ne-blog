# Zer0ne Blog

![logo](static/pictures/dark_logo.png "credits: this logo is inspired from Genegoldstein's work for izzy deluxe in the living tombstone's hunter song")

Hello friend 🤖,

I am *nairolf32*, A cybersecurity enthusiast slowly getting stronger. I Play CTFs and challenges on various websites and decided to keep a track of what I already know/did/learnt by writing it down. Here is a good place for that. This repository used to simply host my ctf writeups but I turnt it into my cybersec blog and here I share the best things I learnt throughout my learning journey. The writeups are from many platforms. My favorites ones are Tryhackme and Hackthebox. The writeups are mostly from those platforms.

You can click [here](http://zer0ne-hub.github.io/zer0ne-blog/about/) to learn more about this blog!

## Usage

This repository is not really open for external contributions but feel free to open an issue for anything you want to share. For further usage simply clone the repo with `git clone` and run `hugo` (it manages everything for you)
Most importantly, as I use a submodule theme you need to get it locally too using `git submodule init` then `git submodule update`. To test it run below commands:

- `hugo server`
- For local development you might need to override the baseURL in the config file
using the `--baseURL=http://localhost:1313` flag with the command above.
- The structure is quite simple, the `content` folder contains all the posts using hugo pages bundles, the `static` folder contains the rest of global static files (images, css, js, etc.), and the `themes` folder contains the theme submodule used for the website. You should not modify the theme files directly, but you can override them in the `layouts` folder (If really needed).
- `hugo -D` for building the website
- Deploying on GitHub Pages using GitHub Actions using the `./github/workflows/pages.yml` file
- Some minor theme layout modifications are done in the `layouts` folder (image render-hooks and shortcodes)
- Added a fuzzy search feature using [Pagefind](https://pagefind.app/). You can install it locally with npm or yarn or download the binary from the [releases page](https://github.com/CloudCannon/pagefind/releases). The latest is
used in the GitHub Actions workflow file. The search feature is implemented using the `pagefind` shortcode in the `layouts/shortcodes/pagefind.html` file and used in the `content/search/index.md` file. The indexing command is `pagefind --site public` to index the website content and generate the search files in the `public` folder. Remember to run this command after building the website with `hugo -D` to update the search index locally.

Check [hugo website](https://gohugo.io/) for more information about this great static site generator
