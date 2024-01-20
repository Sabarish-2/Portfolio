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

// Create a new Intersection Observer instance
let observer = new IntersectionObserver((entries, observer) => {
    // Loop over the entries
    entries.forEach(entry => {
        // If the element is in the viewport
        if (entry.isIntersecting) {
            // Get the image element from the entry
            let img = entry.target;
            
            // Set the src attribute
            img.src = img.dataset.src;

            // Stop observing the image
            observer.unobserve(img);
        }
    });
});

// Get all the images
let imgs = document.querySelectorAll('.delayed-img');

// Start observing each image
imgs.forEach(img => {
    observer.observe(img);
});
