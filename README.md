## Daily Memories 

## Structure

1. Email is received on my domain  
2. Cloudflare workers extract that email convert it to json and send a post request to my flask server running on render  
3. The flask server process the json and adds it to a database via sqlalchemy.  
4. When a browser open the website via get request the flask server asks for their email and if a match is found it displays journals list which the user can click to view the journal of specific day.

## Why This?

Most journaling apps require opening another app. Email once, everything else is automatic.
