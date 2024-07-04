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

document.addEventListener('DOMContentLoaded', () => { //'DOMContentLoaded' event for if the whole doc is loaded
    const ships = document.querySelectorAll('.ship-preview');
    const gameboard = document.getElementById('gameboard');
    
    ships.forEach(ship => {
        ship.addEventListener('dragstart', dragStart);
        ship.addEventListener('dragend', dragEnd);
    });

    gameboard.addEventListener('dragover', dragOver);
    gameboard.addEventListener('drop', drop);

    let selectedShip = null;

    function dragStart(e) { 
        selectedShip = e.target;
        setTimeout(() => { //This is js function that executes a code after a specified delay //'=>' is an alternative function syntax
            selectedShip.style.display = 'none'; //Sets the display none also makes the dragged element invisible
        }, 0); //Delay is 0 miliseconds. Code executes immediately
    }

    function dragEnd() {
        selectedShip.style.display = 'block'; //Sets the display property of element to blocok and its again visible
        selectedShip = null;
    }

    function dragOver(e) {
        e.preventDefault();
    }
    
    function drop(p) {
        p.preventDefault();
        if(selectedShip) {
            const gameboardRect = gameboard.getBoundingClientRect(); //gets the positions of the gameboard
            const offsetX = p.clientX - gameboardRect.left; //calculates the horizantal pos relatiive to the gameboard as a const
            const offsetY = p.clientY - gameboardRect.top; //calculates the vertical pos relatiive to the gameboard as a const

            if (offsetX >= 0 && offsetY >= 0 && offsetX <= gameboardRect.width && offsetY <= gameboardRect.height) {
                //If the horizantal pos(offsetX) is > or = to 0 and the vertical pos(offsetY) is > or = to 0 and the horizontal pos is < or = to the width
                //of the gameboard and the vertical pos is less than or equal to the height of the gameboard, then....
                selectedShip.style.position = 'absolute';
                selectedShip.style.left = `${offsetX - selectedShip.offsetWidth / 2}px`; //positon the ship at the coordinates where the pointer is relative to the gameboard
                selectedShip.style.top = `${offsetY - selectedShip.offsetHeight / 2}px`;
                gameboard.appendChild(selectedShip); //once dropped on the gameboard, appending the ships as a child so they are placed on the gameboard
            } else {
                alert('Please drop the ships on the gameboard.')
            }
        }
    }
});

//FM, amp, hz, waves 