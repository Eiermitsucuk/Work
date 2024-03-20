if (gameMode === 'singlePlayer') {
      startSinglePlayer()
    } else {
      startMultiPlayer()
    }
  
function startSinglePlayer() {
    generate(shipArray[0])
    generate(shipArray[1])
    generate(shipArray[2])
    generate(shipArray[3])
    generate(shipArray[4])

    startButton.addEventListener('click', () => {
        setupButtons.style.display = 'none'
        playGameSingle()
    })
}

function createBoard(grid, squares) {
    for (let i = 0; i < width*width; i++) {
        const square = document.createElement('div')
        square.dataset.id = i
        grid.appendChild(square)
        squares.push(square)
    }
}
