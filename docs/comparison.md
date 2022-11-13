## Scraping from HTML
### Advantage
- It always available.
### Disadvantage
- The data format is unstructured.
- The website may be mixed with irrelevant components.
- The UI/UX is more likely to change after a short period of time.
- If the website uses Client Side Rendering. We must use javascript engine to render the layout.


## Scraping from API
### Advantage
- The API is structured in JSON format.
- The data is easier to read and cleaner.
- They are less likely to change, unless it's a big update from the website.
### Disadvantage
- Depends on the website. Not all website can have APIs or publicly available.


## Personal experience
- Doing this project, I think scraping from API is faster and easier if the website has APIs than scraping from HTML. 
- Scraping from HTML: Most of the time I have to search the XPATH of the wanted tags. And every pages are not the same so it takes long time to crawl from many pages. Moreover, it is easier to encounter bugs and errors. And if we want to crawl a lot of data it can be extremely difficult.
- Scraping from API is hard only at how to find APIs if they are not public. Using DevTools we can search it but it requires some time.
- Overall, I learnt how to crawl data by using Scrapy framework. Crawling from HTML and API, know their strengths and weaknesses; therefore, applying them better in the future.