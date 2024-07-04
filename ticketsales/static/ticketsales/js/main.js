document.addEventListener('DOMContentLoaded', function() {
    function showSection(sectionId) {
        const sections = document.querySelectorAll('.section');
        sections.forEach(section => {
            section.classList.remove('active');
        });
        const activeSection = document.getElementById(sectionId);
        if (activeSection) {
            activeSection.classList.add('active');
        }
    }

    // نمایش بخش قطار به صورت پیش‌فرض
    showSection('train');
    
    const searchButton = document.querySelector('.search-bar button');
    searchButton.addEventListener('click', function() {
        const query = document.querySelector('.search-bar input').value;
        alert(`جستجوی شما: ${query}`);
    });
});
