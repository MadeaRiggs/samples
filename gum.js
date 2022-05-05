var products= [ "Choo Choo Chocolate", "Icy Mint", "Cake Barter", "Bubblegum" ];
var hasBubbleGum= [false, false, false, true];
var i;

for(i= 0; i < hasBubbleGum.length; i++) {
    if (hasBubbleGum[i]) {
        console.log(products[i] + "contains bubblegum");
    }
    
}