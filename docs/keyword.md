The approach to crawl by keyword is to send some parameters to tiki search url. Those parameters are: 
- ```keyword```: input by user.
- ```sort_type```: Tiki product pages provides users some options to find products better.

Then to crawl all the product from that search url. I provide two choices:
1. Crawl by API:
After obtaining all the product urls. I find their product IDs and pass them to Tiki Product Detail API. Here I request to get some data such as: name, price, variants, etc. 

2. Crawl by HTML:
After obtaining all the product urls. I go to their product detail page and extract all the data from its HTML. I can crawl almost everything that display on these website.

Since my approach is heavily dependent on the UI/UX of the page. So if I want to crawl more data, I have to handle site paging. After crawling all data from page 1, I can paginate to the next page and crawl until the ```num_products``` argument is satisfied.

Some comparisons between these two crawling techniques are discussed in [comparison](./comparison.md)



