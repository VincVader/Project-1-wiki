# Wikipedia-like online encyclopedia

### Written with:

* HTML
* CSS
* Python 3.9
* Django 3.0.2
* SQLite 3

Pages itself are written on the [Markdown2](https://github.com/trentm/python-markdown2), upgraded version of the [Markdown](https://en.wikipedia.org/wiki/Markdown)

### Readme Navigation

1. [Wiki pages](#title-page)  
    1. [Index page](#index-page)
    2. [Titles](#title-page)
    3. [Page not found](#no-such-page)
2. [Search query](#search)  
    1.  [Exact match](#exact-match)
    2.  [Not exact match](#not-exact-match)
3. [Naem](#source)  
4. [Naem](#source)  
5. [Naem](#source)  



## 1. Wiki pages:

### 1.1 Index Page:

On index page are wiki entries are clickable and will brought you to their entry page.

![Clicking on pages](/media/clicking-on-pages.gif) 

### 1.2 Title Page
Each page has it's own url at /wiki/__*TITLE*__ where __*TITLE*__ is the title of an encyclopedia entry.

![Title page](/media/title-pages.gif)

### 1.3 No such page
If page doesn't exist the user will be presented with an error page:

![Search](/media/pages404.gif)
## 2. Search:

### 2.1 Exact match:
If the query matches the name of an encyclopedia entry, the user will be redirected to that entry page:

![Title page](/media/search-exact-match.gif)
### 2.2 Not exact match:

If the query does not match the name of an encyclopedia entry, instead the user will be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.

On result page user can click on any of the entries pages names, doing so the user will be taken to that entry page:

![Title page](/media/search-not-exact-match.gif)

## 3. Bla


