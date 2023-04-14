(async function() {
    EXTRACT_TEXT = (el) => el.innerText.trim().replace(/\s+/g, " ");
    BASE = () => { return document.querySelector(`[role="feed"]`); }
    TIMEOUT = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    SEND = (data) => fetch("http://localhost:3103/post", {
        method: "POST",
        body: data
    });

    let at = 0;
    while (BASE().children.length > at) {
        try {
            let el = BASE().children.item(at);
            el.scrollIntoView();
            
            let scope = el.querySelector(`[data-ad-comet-preview="message"]`);
            if (scope != null) {
                scope = scope.querySelectorAll(`[style="text-align: start;"]`);
        
                let textContent = "";
                for (let i = 0; i < scope.length; i++) {
                    const txt = scope.item(i);
                    textContent += EXTRACT_TEXT(txt);
                }
        
                SEND(textContent)
            }
            at++;
            await TIMEOUT(750);
        } catch (e) {
            console.error(e);
            console.log("Unexpected error.. sleeping 15s and skipping..")
            await TIMEOUT(15000);
            at++;
        }
    }
})();