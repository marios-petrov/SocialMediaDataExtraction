# Facebook Group Scraper
The facebook group scraper is in two components for ease of use. The webserver is a simple NodeJS Express server that listens to incoming requests on port 3103, aggregating all data sent from the browser to a file.
It requires NodeJS to be installed, as well as the NPMJS libraries express and body-parser. The server can be started by running the command `node server.js` in the server directory.
<br><br>
The browser script (ChromeConsoleScript.js) can be pasted into the chrome dev console and run. If the user is currently looking at the home page for a group, it will begin to automatically scroll down and send the posts as it sees them to the server.