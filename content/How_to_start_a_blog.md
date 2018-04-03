Title: How to start a blog with Jupyter notebook
Slug: how-to-blog
Date: 2018-04-01 19:00
Category: Jupyter notebook
Tags: blog, jupyter, url 
author: S.-H. Dan Shim

My blog was setup and started with the instruction in: <https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/>


Normal workflow for a blog posting.

- Switch to the main blog folder.

- Run `pelican content` to generate the HTML.

- Switch to the `output` directory.

- Run `python -m pelican.server`.

- Visit `localhost:8000` in a browser to preview.

- Move back to the main blog folder.

- Run `pelican content -s pelicanconf.py`.

- Run `ghp-import output -b master` to import everything in the output folder to the master branch.

- Run `git add .`.

- Run `git commit -m`.

- Run `git push origin master` to push the content to `Github`.
