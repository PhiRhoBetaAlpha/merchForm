general notes:

- using django, python, html, sql, maybe java

front end:

- primarily html and django
- *will probably have to be a [form](https://docs.djangoproject.com/en/5.0/topics/forms/)*
- listing of all the merch on the front page with a photo of the front and back
  - include tax (10%)
  - include greekbill charge (4%)
  - there's one site that does shipping. i'm not sure if we're going to order from them again, but i will discuss this with shelby
  - i believe i have a list of the prices from this past year, if possible make things editable in case that values change
- have a checkout cart
  - members can add items to the cart
- have a confirm purchases page that lists all of the items in one's cart (like payment, but it's just submission of the form)
- each member has the ability to "login" to their existing page
  - this can be a real login, or just a code they create or that we provide that allows them to get back into their previous list of shopping stuff

back end:

- the models and sql
- caluclates each person's total charge
- calculates the total charge of the chapter
- calculates the total number of each shirt design
- calculates quantity of each size of each shirt design (like 3 mediums, 4 larges, etc)
  - also.. if possible, have a name attached to each size..? idk
- all of these calculations stored on a single sheet

DJANGO SITE

* merchForm - the bigger project name
* shop - intended for the page that has all of the merch items. if possible please make the items dynamic and not dirrectly written into the page.
  * hopefully will be intergrated into a "Cart" page
  *
