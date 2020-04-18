//function defLoiHybrid(var vitesseH, var penteH, batterieH)

var vitesseHReelle= 135;
var penteHReelle =0.1;
var batterieHReelle = 45.5;
var vitesseHArr;
var penteHArr;
var batterieHArr;


if(vitesseHReelle <= 15) { VitesseHArr = 10}
else if(16 <= vitesseHReelle && vitesseHReelle <= 25) { vitesseHArr = 20}
else if(26 <= vitesseHReelle && vitesseHReelle <= 35) { vitesseHArr = 30}
else if(36 <= vitesseHReelle && vitesseHReelle <= 59) { vitesseHArr = 50}
else if(60 <= vitesseHReelle && vitesseHReelle <= 75) { vitesseHArr = 70}
else if(76 <= vitesseHReelle && vitesseHReelle <= 85) { vitesseHArr = 80}
else if(86 <= vitesseHReelle && vitesseHReelle <= 99) { vitesseHArr = 90}
else if(100 <= vitesseHReelle && vitesseHReelle <= 119) { vitesseHArr = 110}
else if(120 <= vitesseHReelle ) { vitesseHArr = 130}


if (0 <= penteHReelle && penteHReelle < 0.05){ penteHArr = 0}
else if (0.05 <= penteHReelle && penteHReelle < 0.1){ penteHArr = 5}
else if ( penteHReelle => 0.1){ penteHArr = 10}


if (0 <= batterieHReelle && batterieHReelle < 45){batterieHArr = 30}
else if (45 <= batterieHReelle && batterieHReelle < 75){batterieHArr = 60}
else if (75 <= batterieHReelle && batterieHReelle <= 100){batterieHArr = 100}
console.log(vitesseHReelle +"  "+ penteHReelle + "  " + batterieHReelle);
console.log(vitesseHArr +"  "+ penteHArr + "  " + batterieHArr);

var table = [
	[10,0,30,2],[10,0,60,6],[10,0,100,8],[10,5,30,2],[10,5,60,2],[10,5,100,2],[10,10,30,2],[10,10,60,2],[10,10,100,2],
	[20,0,30,2],[20,0,60,6],[20,0,100,8],[20,5,30,2],[20,5,60,2],[20,5,100,2],[20,10,30,2],[20,10,60,5],[10,10,100,2],
	[30,0,30,2],[30,0,60,2],[30,0,100,8],[30,5,30,2],[30,5,60,5],[30,5,100,2],[30,10,30,2],[30,10,60,5],[30,10,100,5],
	[50,0,30,2],[50,0,60,2],[50,0,100,8],[50,5,30,2],[50,5,60,5],[50,5,100,2],[50,10,30,2],[50,10,60,5],[50,10,100,5],
	[70,0,30,2],[70,0,60,2],[70,0,100,2],[70,5,30,2],[70,5,60,5],[70,5,100,5],[70,10,30,6],[70,10,60,2],[70,10,100,5],
	[80,0,30,2],[80,0,60,5],[80,0,100,2],[80,5,30,2],[80,5,60,5],[80,5,100,5],[80,10,30,6],[80,10,60,6],[80,10,100,6],
	[90,0,30,2],[90,0,60,5],[90,0,100,2],[90,5,30,2],[90,5,60,5],[90,5,100,5],[90,10,30,6],[90,10,60,6],[90,10,100,6],
	[110,0,30,2],[110,0,60,5],[110,0,100,5],[110,5,30,6],[110,5,60,6],[110,5,100,6],[110,10,30,6],[110,10,60,6],[110,10,100,6],
	[130,0,30,2],[130,0,60,5],[130,0,100,5],[130,5,30,6],[130,5,60,6],[130,5,100,6],[130,10,30,6],[130,10,60,6],[130,10,100,6],
	]



for(var i = 0;i<table.length-1;i++){
	//console.log("ok1");
	if( table[i][0] === vitesseHArr  && table[i][1] == penteHArr && table[i][2] == batterieHArr){
		console.log('sequence trouvée'+ " // iter = "+ i);
		console.log(table[i]);
		var loi = table[i][3];
		
		console.log('indice de la loi :' +loi);
		return 
	}
}
