// Wait until the browser has finished building the document before selecting elements.
document.addEventListener('DOMContentLoaded', () => {
    // Find the mobile menu button.
    const menuToggle = document.querySelector('.menu-toggle');
    // Find the navigation menu that the button controls.
    const navigation = document.querySelector('.main-nav');
    // Continue only when both mobile navigation elements exist on the page.
    if (menuToggle && navigation) {
        // Toggle the mobile navigation whenever the button is clicked.
        menuToggle.addEventListener('click', () => {
            // Read the current expanded state from the button.
            const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
            // Tell assistive technology about the new menu state.
            menuToggle.setAttribute('aria-expanded', String(!expanded));
            // Add or remove the open class that controls the mobile menu appearance.
            navigation.classList.toggle('open');
        });
    }
    // Find every element marked for reveal-on-scroll animation.
    const revealItems = document.querySelectorAll('.reveal');
    // Use the browser's IntersectionObserver when it is available.
    if ('IntersectionObserver' in window) {
        // Create an observer that watches when elements enter the viewport.
        const observer = new IntersectionObserver((entries, currentObserver) => {
            // Process every element whose visibility changed.
            entries.forEach((entry) => {
                // Animate the element only after it becomes visible.
                if (entry.isIntersecting) {
                    // Add the visible class that activates the CSS transition.
                    entry.target.classList.add('is-visible');
                    // Stop watching the element after it has appeared once.
                    currentObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        // Start observing each reveal element.
        revealItems.forEach((item) => observer.observe(item));
    } else {
        // Make all reveal elements visible immediately in older browsers.
        revealItems.forEach((item) => item.classList.add('is-visible'));
    }
});
