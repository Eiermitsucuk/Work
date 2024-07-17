document.querySelectorAll('.ship-preview').forEach(function(ship) {
    ship.addEventListener('click', function(event) {
        document.querySelectorAll('.ship-preview').forEach(function(s) {
            s.classList.remove('selected');
        });
        event.target.classList.add('selected');
        selectedShip = event.target;
    });
});

document.addEventListener('keydown', function(event) {
    if (event.key === 'r' || event.key === 'R') {
        if (selectedShip != null) {
            selectedShip.classList.toggle('rotated');
        } else {
            alert('No ships selected');
        }
    }
});

const ships = document.querySelectorAll('.ship-preview');
const gameboard = document.querySelector('.gameboard');
const squares = document.querySelectorAll('.square');

let selectedShip = null;

ships.forEach(function (ship) {
    ship.addEventListener('dragstart', dragStart);
    ship.addEventListener('dragend', dragEnd);
    ship.addEventListener('click', selectShip);
});

squares.forEach(function (square) {
    square.addEventListener('dragover', dragOver);
    square.addEventListener('drop', drop);
});

function dragStart(e) {
    if (!selectedShip) {
        alert('Please select a ship.');
        return;
    }
    setTimeout(() => {
        selectedShip.style.display = 'none';
    }, 0);
}

function dragEnd() {
    if (selectedShip) {
        selectedShip.style.display = 'block';
    }
}

function selectShip(e) {
    if (selectedShip) {
        selectedShip.classList.remove('selected');
    }
    selectedShip = e.target;
    selectedShip.classList.add('selected');
}

function dragOver(e) {
    e.preventDefault();
}

function drop(e) {
    e.preventDefault();
    if (!selectedShip) {
        alert('Please select a ship.');
        return;
    }

    const squareSize = squares[0].offsetWidth;
    const offsetX = e.clientX - gameboard.offsetLeft;
    const offsetY = e.clientY - gameboard.offsetTop;

    const col = Math.floor(offsetX / squareSize);
    const row = Math.floor(offsetY / squareSize);

    if (col >= 0 && row >= 0 && col < 5 && row < 5) {
        const targetSquare = squares[row * 5 + col];

        selectedShip.style.gridColumnStart = col + 1;
        selectedShip.style.gridRowStart = row + 1;

        gameboard.appendChild(selectedShip);
    } else {
        resetShipPosition();
        alert('Please drop your ships on the gameboard.');
    }
}

function resetShipPosition() {
    const shipContainer = document.getElementById('ships');
    shipContainer.appendChild(selectedShip);
}
