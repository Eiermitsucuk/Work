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

