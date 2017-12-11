#### fakebook web crawler

## How to start the web crawler
**Username**: *banana.s*

**Password**: *banana*

```bash
    # if 'webcrawler' is not marked as executable => `chmod u+x webcrawler`
    ./webcrawler <username> <password>
```

## How the web crawler crawls

#### Libraries used
- *urllib.request* : to make http requests
- *http.cookiejar* : used to make an opener to make the http requests
- *deque* : used to keep track of the fringe when crawling
- *urllib.parse* : used to parse a url to get the scheme, domain, and path

#### Logging in & Staying logged in
First, a GET request is made to the [home page](http://cs5700sp15.ccs.neu.edu/fakebook/). If you are not logged in, it redirects to the login page and returns a response. I grab the login url from this response. The cookie jar stores cookie info from the response; I grab the crsf token and session id from the cookie jar. I use this token to make a POST request to the login url and now we are signed in.

The opener using the cookie jar was used to make the http request and hold the cookie info. For every subsequent GET request, I simply used the opener and remained 'logged in'.

#### Crawling
Once you are logged in, the main page shows a list of possible profiles you can browse. I used these as my starting links. I created a queue with these starting links. For every link in the queue, I did the following:
- Make an http GET request to the link
- If the link is a user profile, increment the user count
- Parse the response and grab all child links contained on the page
- If the child link has not yet been visited, add it to the queue and mark it as visited

The crawler stops once the queue is empty.

#### Handling errors
When making an http request, I only had to worry about handling http responses with status codes within the range 400-500. The *urllib.request* library took care of all others. Other things I needed to handle were socket timeouts. For timeouts and responses with the code 500 (INTERNAL SERVER ERROR), I tried to make the request 2 more times and then gave up. If I encountered any other error, I also gave up. If I was unable to fulfill the request, I added the url to a list of reject urls and moved on.

If requests were asynchronous (as they should be, but aren't in this project), I would've kept my original approach of exponential random back offs, waiting an increased amount of time between each failure before trying to make the request again. I initially took this approach but my crawler as running for 45 minutes before I accidentally canceled it.. Removing exponential back-offs made the crawler faster, at the expense of possibly not visiting a page. When the crawler ends, I spit out the number of users visited as well as any urls collected but ignored by the crawler and any urls that the crawler tried but was unable to visit. 

## Results
- CRAWL TIME: ~35 minutes
- NUMBER OF USERS: 2500
- SECRET FLAGS: 0, no secret flags found

## Thoughts/Extensions
1. Even though 'every user is connected to one friend or more', there could be disconnected sub-graphs in FakeBook. Perhaps that is why Tom was everyone's friend on MySpace, to keep track of them all with one crawl.
1. This crawler would likely be faster if
    1. it was parallelized in some way/requests were asynchronous
    1. I ditched the libraries nad optimized low-level code for the task
    1. I was connected to ethernet

