The approach to crawl by category is:
1. First, I request to the Tiki homepage and crawl all the categories name from it.
2. Then checking the category argument if it matches with 24 supported categories.
3. After obtaining the wanted category url. I extract the category ID from it and pass to Tiki Category API with limitation of the number ```num_products```.
4. For every product ID I request to the Tiki Product API and get some data from it.