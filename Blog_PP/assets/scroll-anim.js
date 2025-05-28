function applyScrollAnimations() {
    const elements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, {
        threshold: 0.1
    });

    elements.forEach(el => {
        // Evita duplicar observadores
        if (!el.classList.contains('observed')) {
            observer.observe(el);
            el.classList.add('observed');
        }
    });
}

document.addEventListener('DOMContentLoaded', applyScrollAnimations);

// Observa cambios en el DOM (por ejemplo, cuando cambias de página en Dash)
const observer = new MutationObserver((mutations) => {
    mutations.forEach(() => {
        applyScrollAnimations();
    });
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
