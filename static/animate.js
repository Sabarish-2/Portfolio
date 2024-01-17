document.addEventListener("DOMContentLoaded", function() {
    const blinkJourney = document.getElementById("blink");
    try {
        if (blinkJourney){
        setInterval(function() {
            blinkJourney.style.color = (blinkJourney.style.color === "blue") ? "orange" : "blue";
        }, 750);}
    } catch (error) {}

    try {
        var typed = new Typed('#element', {
            strings: ['App Developer;', 'Website Developer;', 'Game Developer;'],
            typeSpeed: 30,
            loop:true
        });
    } catch (error) { }
});

setTimeout(function() {
    document.querySelectorAll('.delayed-img').forEach(img => {
        img.src = img.dataset.src;
    });
}, 105);
