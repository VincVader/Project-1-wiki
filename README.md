# Wikipedia-like online encyclopedia

### Written with:

* HTML
* CSS
* Python 3.9
* Django 3.0.2
* SQLite 3

Pages itself are written on the [Markdown2](https://github.com/trentm/python-markdown2), upgraded version of the [Markdown](https://en.wikipedia.org/wiki/Markdown)

### Readme Navigation

1. [Title pages](#title-page)  
2. [Error handling](#no-such-page)  
3. [Search query](#source)  
4. [Naem](#source)  
5. [Naem](#source)  
6. [Naem](#source)  


### Entry pages:
Each page has it's own url at /wiki/__*TITLE*__ where __*TITLE*__ is the title of an encyclopedia entry.

![Title page](/media/title-pages.gif)

### No such page
If page doesn't exist the user will be presented with an error page:
![Error page](/media/pages404.png)
### Search:

#### 1. Exact match:
#### 2. Not exact match:

![Title page](/media/search-exact-match.gif)

![Title page](/media/search-not-exact-match.gif)


