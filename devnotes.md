## sources/websites.csv
* Convert csv to JSON in case more metadata is required
    * crawl priority (int)
    * enable permision? (bool)
    * authentication
    * robots policy
    * retry limit
    * extra notes

## crawler/manager.py
* Can you get everything with Requests?
    * IF true: use Requests only
    * Else: use Selenium