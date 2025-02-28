window.onload = () => {
    const grid = document.querySelector('.grid')

    const masonry = new Masonry(grid, {
        columnWidth: 200,
        itemSelector: '.grid-item'
    });
    
};