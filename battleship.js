/*var randomLoc= Math.floor(Math.random() * 5) ;
var location1 =randomLoc;
var location2 =location1 + 1;
var location3 =location2 + 1;*/
var model={
    boardsize:7,
    numShips:3,
    shipLength:3,
    shipSunk:0,
    ships:[{locations: ["06", "16", "26"], hits: ["hit", "", ""] },
           {locations: ["24", "34", "44"], hits: ["", "", ""] },
           {locations: ["10", "11", "12"], hits: ["", "", ""]}
        ],
    fire:function (guess) {
        for(var i=0; i<this.numShips; i++) {
            var ship=this.ships[i];
        }
    }
};
var view={
    displayMessage:function(msg) {
        var messageArea= document.getElementById("messageArea");
        messageArea.innerHTML=msg;
    },
    displayHit:function(location) {
        var cell= document.getElementById(location);
        cell.setAttribute("class", "hit");
    },
    displayMiss:function(location) {
        var cell=document.getElementById(location);
        cell.setAttribute("class", "miss");

    }
};
view.displayMiss("00");
view.displayHit("34");
view.displayMiss("55");
view.displayHit("12");
view.displayMiss("25");
view.displayHit("26");
view.displayMessage("Tap tap, is this thing on?");

/*var guess;
var hits =0;
var guesses =0;

var isSunk =false;

while(isSunk==false) {
    guess=prompt("Ready, aim, fire! (enter a number from 0-6):");
    
    if(guess<0 || guess>6){
        alert("Please enter a valid cell number!");
    } else{
        guesses=guesses + 1;
    }
    if(guess==location1|| guess==location2|| guess==location3){
       alert("HIT!");
       hits= hits + 1;
    
       if (hits==3){
           isSunk=true;
           alert("You sank my battleship!");
       } 
       else {
        alert("MISS!");
    } 
    }
}
var stats ="You took" + guesses + "guesses to sink the battleship," + "which means your shooting accuracy was " + (3/guesses);
alert(stats);*/

