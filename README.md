## TechCrunch Crawler

### System Overview &  Code Structure
This is an MVP implementation of a crawler backend with the following modules:

**Crawler**

Serves to encapsulate the logics related to an abstract crawler class as well as specific crawler implementations
e.g., TechCrunch Crawler. For further abstraction, I attempted to extract class-specific configurations to a **Config** Module for better readability and faster deployment down the road.

The particular logic for our TechCrunch Crawler is simply reading the html content for from a (RSS) feed API for techcrunch.com.
There are a few improvements/TODOs including pagination to get most recent 100 articles (v.s. the current 20 articles by default) as well as extracting more metadata such as update time, description and etc.

**Storage**

Here we encapsulate the logic related to storage CRUD logics. 

We optimize for fast read with a caching layer of our entire DB
with two different indices: 
1. Index by an internal id(Primary Key), e.g. TC_12345, this is designed as a concat of the namespace of the datasource plus the post id from techcrunch.com; this index serves to maintain uniqueness of an article with the assumption that techcrunch external url can change but not the post id.
In general, for any datasource that we want to integrate, we will need to identify a unique external ID system for the particular datasource.
2. Index by author name; this is a secondary index with the purpose of speeding up get_article_by_author API. In general, we can develop more indices like this for similar speed-up purposes, e.g. get all articles with a tag/key word.

Here we have an assumption that DB is relatively stale (update in a batch fashion by an hourly/daily job), therefore, our cache is relatively stale. 
With the time limit and this assumption in mind, our Create/Update logic is non-optimal: we store our article records in a csv file; whenever there is a new/updated record, we will do an idempotent update to rewrite the entire dataset for simplicity and accuracy. 

An improvement for this case is to only update changed record and incremental records.

With our caching layer in place, the implementation of the APIs become straightforward: simply translate the cached data to human-readable format (we had some compression/encoding logic in place to reduce memory usage)

**Serving**

Lastly, we implemented our customer-facing RESTful APIs using Flask (my first time building a Flask App!) 
