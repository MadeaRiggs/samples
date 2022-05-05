var scores= [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44];
function printAndGetHighScore(scores) {
    var highscore= 0;
    var output;
    for(var i= 0; i < scores.length; i++){
        output= "Bubble solution #" + i + "score:" + scores[i];
        console.log(output);
        if(scores[i] > highscore) {
            highscore = scores[i];
}
    }
    return highscore;
}

//while(i < scores.length) {
    //output= "Bubble solution #" + i + "score:" + scores[i];//
    //console.log(output); //
    //i= i + 1; 
 //
 function getBestResults(scores, highscore) {
    var bestSolutions= [];
    for(var i= 0; i < scores.length; i++){
    
        if(scores[i]== highscore) {
            bestSolutions.push(i);
 }
}
return bestSolutions;
 }

 var highscore= printAndGetHighScore(scores);
console.log("Bubble tests: " + scores.length);
console.log("Highest bubble score: " + highscore);

var bestSolutions= getBestResults(scores, highscore);
console.log("Solutions with the highest score: " + bestSolutions);

var costs=[25, 27, 25, 25, 25, 33, 31, 25, 29, 27, 22, 31, 25, 25, 33, 21, 25, 25, 25, 28, 25, 24, 25, 25, 25, 27, 25, 26, 29];
function getMostEffectiveSolution(scores, costs, highscore) {
    var cost= 100;
    var index;
    var bestSolutions= [];
   
    for(var i= 0; i < scores.length; i++){
        if(scores[i]== highscore) {
            if(cost> costs[i]) {
                index= i;
                cost= costs[i];
                
            }
    
        }
    }
    return index;
}
var mostCostEffective= getMostEffectiveSolution(scores, costs, highscore);
console.log("Bubble solution # " + mostCostEffective + " is the most cost effective");

