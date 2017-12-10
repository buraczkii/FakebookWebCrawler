#### fakebook web crawler

## How to start the web crawler
**Username**: *banana.s*

**Password**: *banana*

```bash
    ./webcrawler <username> <password>
```


## How the web crawler crawls
- how to make HTTP GET requests
- how to make HTTP POST requests
- how to handle request codes
  - 200 (OK)
  - 301 (Redirect) - make HTTP GET to suggested website
  - 403/404 (Not found) - abandon. log the site?
  - 500 (Internal Server Error) - try again. exponential back off?

- how to log in
- how to keep track of cookie and use it to stay logged in
- how to keep track of frontier (queue)
- how to keep track of where you've been (visited hashmap/list)
- how to ensure only crawl domain "cs5700sp15.ccs.neu.edu"


## Results
- number of users
- secret flags if any
