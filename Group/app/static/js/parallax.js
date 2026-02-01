/* Parallax Scrolling JavaScript */

window.addEventListener('scroll', () => {
    // Parallax effect for fixed background images
    const parallaxElements = document.querySelectorAll('.parallax');
    parallaxElements.forEach(element => {
        let scrollPosition = window.scrollY;
        element.style.backgroundPosition = `center ${scrollPosition * 0.5}px`;
    });

    // Update scroll progress bar
    let scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    let progressBar = document.querySelector('.scroll-progress');
    if (progressBar) {
        progressBar.style.width = scrollPercent + '%';
    }

    // Reveal elements on scroll
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const elementVisible = 150;
        if (elementPosition < window.innerHeight - elementVisible) {
            element.classList.add('active');
        }
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Optional: stop observing after animation
            // observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements with observer classes
document.querySelectorAll('.observe-fade, .observe-slide-left, .observe-slide-right, .stagger-item').forEach(el => {
    observer.observe(el);
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add parallax effect to hero sections
function updateParallax() {
    const scrollY = window.scrollY;
    const heroElements = document.querySelectorAll('[data-parallax]');
    
    heroElements.forEach(element => {
        const parallaxValue = element.getAttribute('data-parallax') || 0.5;
        element.style.transform = `translateY(${scrollY * parallaxValue}px)`;
    });
}

window.addEventListener('scroll', updateParallax);

// Menu link active state
const menuLinks = document.querySelectorAll('.menu-link, .nav-link');
menuLinks.forEach(link => {
    link.addEventListener('click', function() {
        // Remove active class from all links
        menuLinks.forEach(l => l.classList.remove('active'));
        // Add active class to clicked link
        this.classList.add('active');
    });
});

// Add fade-in animation to feature cards
const cards = document.querySelectorAll('.feature-card, .security-item, .credential-card');
cards.forEach((card, index) => {
    card.style.animation = `slideUp 0.6s ease-out ${index * 0.1}s backwards`;
});

// Mouse parallax effect on hover
document.addEventListener('mousemove', (e) => {
    const parallaxItems = document.querySelectorAll('[data-mouse-parallax]');
    const x = (window.innerWidth - e.clientX * 5) / 100;
    const y = (window.innerHeight - e.clientY * 5) / 100;
    
    parallaxItems.forEach(item => {
        item.style.transform = `translateX(${x}px) translateY(${y}px)`;
    });
});

console.log('Parallax scrolling initialized');
