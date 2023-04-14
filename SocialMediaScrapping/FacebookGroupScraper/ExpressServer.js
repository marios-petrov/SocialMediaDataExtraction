const express = require("express");
const bp = require("body-parser");
const fs = require("fs");

const server = express();

let tally = 0;

// Allow all CORS
server.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "*");
    next();
});

server.use(bp.raw({
    type: "*/*",
    limit: "100kb"
}))

server.post("/post", (req, res) => {
    const s = req.body.toString("utf8");
    // Add the data as a csv tally,content make sure to escape commas
    if (!s.includes("See more")) {
        fs.appendFileSync("data.csv", `${tally},${s.replace(/,/g, "\\,")}\n`);
        console.log(`\nTally: ${tally}\n\t- ${s}\n`)
        tally ++;
    }
    res.send("OK");
});


server.listen(3103, () => {
    console.log("Server is running on port 3000");
})
