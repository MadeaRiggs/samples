var taxi= {
    make: "Webville Motors",
    model: "Taxi",
    year: 1955,
    color: "yellow",
    passengers: 4,
    convertible: false,
    mileage: 281341,

/*for (var prop in taxi) {
    document.write(prop + ":" + taxi[prop]);
}*/
   started: false,
    fuel: 0,
    start: function() {
        if(this.fuel<= 0) {
            document.write("The car is empty, fill up before starting!");
        } else{
            document.write("Start the car!");
        }
        this.started=true;
    },
    stop: function() {
        this.started=false;
    },
    drive: function() {
        if(this.started) {
            if(this.fuel> 0) {
                alert(this.make + " " + this.model + " goes zoom zoom!");
                this.fuel= this.fuel - 1;
            } else {
                alert("Uh oh, out of fuel. ");
                this.stop();
            }
            
        } else {
            alert("You need to start the engine first.");
        }
    },
    addFuel: function(amount) {
        this.fuel= this.fuel + amount;
    }
};

taxi.start();
taxi.drive();
taxi.addFuel(2);
taxi.start();
taxi.drive();
taxi.drive();
taxi.drive();
taxi.stop();


function prequal(car) {
    if(car.mileage> 10000) {
        return false;
    } else if(car.year>1960) {
        return false;
    }
    return true;
}

var worthALook= prequal(taxi);

if(worthALook) {
    console.log("You gotta check out this " + taxi.make + " " + taxi.model);
} else{
    console.log("You should really pass on the " + taxi.make + " " + taxi.model);
}
