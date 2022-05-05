var input = "jenny@wickedlysmart.com";
for(var i = 0; i<input.length; i++) {
    if(input.charAt(i)=== "@") {
        console.log("There's an @ sign at index " + i);
    }
}

var phrase= "the cat in the hat";
var index= phrase.indexOf("cat");
console.log("there's a cat sitting at index " + index);

index=phrase.indexOf("the", 5);
console.log("there's a the sitting at index " + index);

index=phrase.indexOf("dog");
console.log("there's a dog sitting at index " + index);

var data="name|phone|address";
var val=data.substring(5, 10);
console.log("Substring is " + val);
val= data.substring(5);
console.log("Substring is now " + val);

var datas="name|phone|address";
var vals=datas.split("|");
console.log("Split array is " , vals);

//Code1//
/*function validate (phoneNumber) {
    if(phoneNumber.length > 8 || phoneNumber.length <7) {
        return false;
    }
    for(var i=0; i<phoneNumber.length; i++) {
        if(phoneNumber.length===8 && phoneNumber.charAt(i) !== '-') {
            return false;
        } else if (phoneNumber.length===7 && isNaN(phoneNumber.charAt(i))) {
            return false;
        }
    }
    return true;
}
var spec=validate(1234567);
console.log(spec);

//Code2 has error as phonenumber.substring is not a function//
function validate(phoneNumber) {
    if(phoneNumber.length >8 || phoneNumber.length <7) {
        return false;
    }
    var first=phoneNumber.substring(0,3);
    var second=phoneNumber.substring(phoneNumber.length - 4);
    if(isNaN(first) || isNaN(second)) {
        return false;
    }
    if(phoneNumber.length === 8) {
        return(phoneNumber.charAt(3) === "-");
    }
    return true; 

}
var spec=validate(1234567);
console.log(spec); */

//Code3//
function validate(phoneNumber){
    return phoneNumber.match(/^\d(3)-?\d(4)$/);
}
var spec=validate(1234567);
console.log(spec);