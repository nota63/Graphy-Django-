document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.image-container img');
    images.forEach(img => {
        img.style.animationDuration = `${Math.random() * 5 + 3}s`;
    });
});
