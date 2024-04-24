<<<<<<< HEAD
document.addEventListener('keydown', function(event) {
    if (event.key === 'r' || event.key === 'R') {
        var ships = document.querySelectorAll('.ship-preview');
            
        ships.forEach(function(ship) {
            ship.addEventListener('click', function() {
                ships.forEach(function(s) {
                    s.classList.remove('selected');
                });
                this.classList.add('selected');
                this.classList.toggle('rotated');
            });
        });
    }
 });

=======
function createBoard(grid, squares) {
    for (let i = 0; i < width*width; i++) {
        const square = document.createElement('div')
        square.dataset.id = i
        grid.appendChild(square)
        squares.push(square)
    }
}
>>>>>>> a557cc7f3de19bcd1a3cd0069c5bb6e147bb8d7f
