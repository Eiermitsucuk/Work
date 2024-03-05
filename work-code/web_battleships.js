function start() {
    console.log("\n");
    console.log("!!! Welcome the Battleships Game")
    console.log("\n1. Play Game");
    console.log("2. View Highscores");
    console.log("3. Exit");
    console.log("-".repeat(45));
}

function printBoard(board) {
const rows = board.length;
const columns = board[0].length;
console.log("  " + [...Array(columns)].map((_, i) => String.fromCharCode(65 + i)).join(" "));
for (let i = 0; i < rows; i++) {
console.log(`${i} ${board[i].join(" ")}`);
}

}
function creatingBoard(rows, columns) {
return Array.from({ length: rows }, () => Array(columns).fill(" "));
}
return board;

function lettersToIndex(letter) {
    return letter.charCodeAt(0) - "A".charCodeAt(0);
}

function saveScores(score, player){
    console.log('Highscore: $(player): $(score)');
}

function viewScores(){
    console.log("Scores:");
}

async function playGame(){
    const player = prompt("Enter your username: ");
    let score = 0;
    const rows = 10;
    const columns = 10;
    const board = creatingBoard(rows, columns);

    for (let 1 = 0; 1 < 4: i++){
        const shipRows = randomInt(0, rows - 1);
        const shipColumns = randomInt(0, columns - 1);
    }
}

printBoard(board);
const screen = creatingBoard(rows, columns);

for (let i = 0; i < 5; i++){
    console.log(5 - 1);

    let guess;
    while(true) {
        guess = prompt("Where should we bomb, commander!?")
    }
}