function setup() {
  createCanvas(500, 500);
  background(0);
  noStroke();
  fill(0, 255, 0); 

}

var ballX = 250;
var ballY = 100;

var ballXV = -5;
var ballYV = 1;

var rectX = 10;
var rectY = 10;
var rect2X= 470;
var rect2Y = 10;

var numPixels = 10;

var rectWidth = 20;
var rectHeight = 75;

var player1Life = 5;
var player2Life = 5;




function draw() { 
background(100,149,237);
keyPressed();
setShape();
bounceCheck();
increment();
scoreCheck();
checkCollision();
setText();
}

 // checking player 1 and 2 slider bounce

//if ball touches slider along height, bounce back
function sliderBounce() {
  
  if( ballY > rectY && ballY < rectY + 100){ 
  ballXV = ballXV * -1;
  }
  
}

function slider2Bounce(){
  if(ballY > rect2Y && ballY < rect2Y + 100 ) {
  ballXV = ballXV * -1;
  }
}

function bounceCheck() {
  //if balls touches ceiling or floor bounce back
  if(ballY < 0 || ballY > 500) {
    ballYV = ballYV * -1;
  }
  
  //if ball touches either slider along the width, check whether it touches the height too
  if(ballX < 40 && ballXV < 0 ) {
    sliderBounce();
  }
  
  if(ballX > 460 && ballXV > 0){
    slider2Bounce();
  }
     
  if(ballX < 0) {
    ballX = 200;
    player1Life -= 1;
  }
  
  if(ballX >500){
    ballX = 250;
    player2Life -=1;
  }
}

function increment() {  
  //set ball path
  ballX += ballXV;  
  ballY += ballYV;
  
 // if(millis() % 1000 == 0) {
  //  ballXV = ballXV * 2;
 // }
}


function keyPressed() {
  // create up and down keys for both players on the keyboard
  
  //player 1 up
  if ((keyIsPressed == true) && ((key == 'a') || (key == 'A'))) {
  rectY = rectY - numPixels;
  }
  
  //player 1 down
  if ((keyIsPressed == true) && ((key == 'z') || (key == 'Z'))) {
  rectY = rectY  +numPixels;
  }
  
  //player 2 up
  if ((keyIsPressed == true) && ((key == 'k') || (key == 'K'))) {
  rect2Y = rect2Y - numPixels;
  }
  //player 2 down
  if ((keyIsPressed == true) && ((key == 'm') || (key == 'M'))) {
  rect2Y = rect2Y  +numPixels;
  }
  
}    


function ball() {
  //ellipse(ballX - 2, ballY, 30, 30);
  ellipse(ballX, ballY, 20, 20);
}


function setShape() {
  
  //player 1 slider
  fill(255,105,180);
  rect(rectX, rectY, 20, 75);
  
  //ball
  fill(255);
  ball(ballX, ballY);
  
  //player 2 slider
  fill(255,165,0);
  rect(rect2X, rect2Y, 20, 75);
} 

function checkCollision() {
  
    //restrict sliders to stay in visible area for both players
    // up and down player 1
    if (rectY <= 0) {
      rectY = 0
    } else if (rectY + rectHeight >= height) {
      rectY = height - rectHeight;
    }
  
   // up and down player 2
    if (rect2Y <= 0) {
      rect2Y = 0
    } else if (rect2Y + rectHeight >= height) {
      rect2Y = height - rectHeight;
    }
}


function scoreCheck() {
  // check whos score is zero and declare the other person as the winner
  
  if(player1Life == 0 ) {
    noLoop();
    player2Life = "YOU WIN!";
  }
  
  if(player2Life == 0){
    noLoop();
    player1Life = "YOU WIN!";
  }
   
}

function setText() {
  //show scores for each player 
  textAlign(CENTER);
  fill(255);
  textSize(22);
  text(player1Life, 100, 30);
  
  fill(255);
  textSize(22);
  text(player2Life, 400, 30);
}
  