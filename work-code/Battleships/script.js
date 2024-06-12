document.querySelectorAll('.ship-preview').forEach(function(ship) {
    ship.addEventListener('click', function(event) {
        document.querySelectorAll('.ship-preview').forEach(function(s) {
            s.classList.remove('selected');
        });
        event.target.classList.add('selected');
        selectedShips = event.target;
    });
});

document.addEventListener('keydown', function(event) {
    if (event.key === 'r' || event.key === 'R') {
        if (selectedShips != null) {
            selectedShips.classList.toggle('rotated');
        } else {
            alert('No ships selected')
        }
    }
});

const dragShips = document.querySelectorAll('.ship-preview');
const gameboard = document.getElementById('gameboard');

dragShips.forEach(function(ship) {
    ship.addEventListener('dragstart', function(event) {
        event.dataTransfer.setData('text/plain', ship.id);
    });
});

gameboard.addEventListener('dragover', function(event) {
    event.preventDefault();
})

gameboard.addEventListener('drop', function(event) {
    event.preventDefault();
    const shipId = event.dataTransfer.getData('text/plain');
    const draggedShip = document.getElementById(shipId);
    if (draggedShip.classList.contains('selected')) {
        gameboard.appendChild(draggedShip);
        draggedShip.classList.remove('selected');
    } else {
        alert('Please select the ship first to drop it onto gamebaord');
    }
});

