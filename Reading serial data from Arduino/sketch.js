let serial;
let latestData = "waiting for data";
var circle;
var song;
var volume;


//----------------------
var size01;
var size02;
var size03;
var size04;
var size05;
var size06;
var size07;
var size08;
var size09;
var width01;
var height01;
var height04;
var height05;
var height06;
var height07;
var height08;
var width02;
var width03;
var width04;
var width05;
var width06;
var width08;
//----------------------

function preload(){
  
    song = loadSound ("talking.mp3");

}


function setup() {
  


 createCanvas(windowWidth, windowHeight);
  song.play();
  song.setVolume(volume);

 
 serial = new p5.SerialPort();

 serial.list();
 serial.open('/dev/tty.usbmodem14301');

 serial.on('connected', serverConnected);

 serial.on('list', gotList);

 serial.on('data', gotData);

 serial.on('error', gotError);

 serial.on('open', gotOpen);

 serial.on('close', gotClose);
}

function serverConnected() {
 print("Connected to Server");
}

function gotList(thelist) {
 print("List of Serial Ports:");

 for (let i = 0; i < thelist.length; i++) {
  print(i + " " + thelist[i]);
 }
}

function gotOpen() {
 print("Serial Port is Open");
}

function gotClose(){
 print("Serial Port is Closed");
 latestData = "Serial Port is Closed";
}

function gotError(theerror) {
 print(theerror);
}

function gotData() {
 let currentString = serial.readLine();
  trim(currentString);
 if (!currentString) return;
 console.log(currentString);
 latestData = currentString;
}

function draw() {
  
 
  background(0);
  float(latestData);
  data2 = constrain(latestData,1,13);
  circle = map(data2, 1,13,900,0);
  volume = map(data2, 1, 13, 0, 1);
  console.log(volume);

  
  //--------------------------------------
  
  fill(255);
  ellipse(width01, height01, size01, size01);
  size01 = circle;
  if (size01 <= 0) { 
    size01=0;
  }
  
  if (size01 > 0) {
    width01 = width/4*3+size01*1.5;
    height01 = height/4*3+size01*1.5;
  }
  
  fill(0);
  ellipse(width01-size01/8, height01-size01/8, size01/10, size01/10);
  
  fill(0);
  ellipse(width01+size01/8, height01-size01/8, size01/10, size01/10);

  fill(255);
  ellipse(width02, height/2, size02, size02);
  size02 = circle - 100;
  if (size02 <= 0) { 
    size02=0;
  }
  if (size02 > 0) {
    width02 = width/4-size02*1.5;
  }
  
  fill(0);
  ellipse(width02-size02/8, height/2-size02/8, size02/10, size02/10);
  
  fill(0);
  ellipse(width02+size02/8, height/2-size02/8, size02/10, size02/10);

  fill(255);
  ellipse(width03, height/2, size03, size03);
  size03 = circle - 160;
  if (size03 <= 0) { 
    size03=0;
  }
  if (size03 > 0) {
    width03 = width/4*3+size03*1.5;
  }
  
  fill(0);
  ellipse(width03-size03/8, height/2-size03/8, size03/10, size03/10);
  
  fill(0);
  ellipse(width03+size03/8, height/2-size03/8, size03/10, size03/10);

  fill(255);
  ellipse(width/2, height04, size04, size04);
  size04 = circle - 290;
  if (size04 <= 0) { 
    size04=0;
  }
  if (size04 > 0) {
    height04 = height/4-size04*1.5;
  }
  
  fill(0);
  ellipse(width/2-size04/8, height04-size04/8, size04/10, size04/10);
  
  fill(0);
  ellipse(width/2+size04/8, height04-size04/8, size04/10, size04/10);


  fill(255);
  ellipse(width05, height05, size05, size05);
  size05 = circle - 420;
  if (size05 <= 0) { 
    size05=0;
  }
  if (size05 > 0) {
    width05 = width/4-size05*1.5;
    height05 = height/4-size05*1.5;
  }
  
  fill(0);
  ellipse(width05-size05/8, height05-size05/8, size05/10, size05/10);
  
  fill(0);
  ellipse(width05+size05/8, height05-size05/8, size05/10, size05/10);

  fill(255);
  ellipse(width06, height06, size06, size06);
  size06 = circle - 500;
  if (size06 <= 0) { 
    size06=0;
  }
  if (size06 > 0) {
    width06 = width/4*3+size06*1.5;
    height06 = height/4-size06*1.5;
  }
  
  fill(0);
  ellipse(width06-size06/8, height06-size06/8, size06/10, size06/10);
  
  fill(0);
  ellipse(width06+size06/8, height06-size06/8, size06/10, size06/10);


  fill(255);
  ellipse(width/2, height07, size07, size07);
  size07 = circle - 600;
  if (size07 <= 0) { 
    size07=0;
  }
  if (size07 > 0) {
    height07 = height/4*3+size07*1.5;
  }
  
  fill(0);
  ellipse(width/2-size07/8, height07-size07/8, size07/10, size07/10);
  
  fill(0);
  ellipse(width/2+size07/8, height07-size07/8, size07/10, size07/10);

  fill(255);
  ellipse(width08, height08, size08, size08);
  size08 = circle - 680;
  if (size08 <= 0) { 
    size08=0;
  }
  if (size08 > 0) {
    width08 = width/4-size08*1.5;
    height08 = height/4*3+size08*1.5;
  }
  
  fill(0);
  ellipse(width08-size08/8, height08-size08/8, size08/10, size08/10);
  
  fill(0);
  ellipse(width08+size08/8, height08-size08/8, size08/10, size08/10);

  fill(255);
  ellipse(width/2, height/2, size09, size09);
  size09 = circle-800;
  if (size09 <= 0) { 
    size09=0;
  }
  if (size09 > 0) { 
    size09 = size09*10;
  }
  
  fill(0);
  ellipse(width/2-size09/8, height/2-size09/8, size09/10, size09/10);
  
  fill(0);
  ellipse(width/2+size09/8, height/2-size09/8, size09/10, size09/10);
  
//----------------------------
  

  /*
  fill(0);
  ellipse(windowWidth/2, windowHeight/2, circle);
  */
  
  fill(255,0,0);
  text(data2, 10, 10);

 
}

