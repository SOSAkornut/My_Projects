x = 750
y = 400
r1 = 400/2
r2 = 200/2
r3 = 250/2
r4 = 400/2
r5 = 200/2
r6 = 250/2
a = 1


var Button = document.querySelector("button")
var Button2 = document.querySelector(".button2")


function rotate(a) {
  Button.addEventListener("click", function() {
   r1 += .001
   r2 += .001
   r3 += .001
   r4 += .001
   r5 += .001
   r6 += .001


})

  Button2.addEventListener("click", function() {
   r1 -= .001
   r2 -= .001
   r3 -= .001
   r4 -= .001
   r5 -= .001
   r6 -= .001


  })
  var px1 = x + r1 * Math.cos(a * 10 / 4);
  var py1 = y - r1 * Math.sin(a * 10 / 4);
  document.querySelector('.Circle1').style.left = px1 + "px";
  document.querySelector('.Circle1').style.top = py1 + "px";


  var px2 = x + r2 * Math.cos(a * 5 / 4);
  var py2 = y - r2 * Math.sin(a * 5 / 4);
  document.querySelector('.Circle2').style.left = px2 + "px";
  document.querySelector('.Circle2').style.top = py2 + "px";

  var px3 = x + r3 * Math.cos(a * 3 / 4);
  var py3 = y - r3 * Math.sin(a * 3 / 4);
  document.querySelector('.Circle3').style.left = px3 + "px";
  document.querySelector('.Circle3').style.top = py3 + "px";

  var px4 = x + r4 * Math.cos(a * 2 );
  var py4 = y - r4 * Math.sin(a * 2 );
  document.querySelector('.Circle4').style.left = px4 + "px";
  document.querySelector('.Circle4').style.top = py4 + "px";

  var px5 = x + r5 * Math.cos(a * 7 );
  var py5 = y - r5 * Math.sin(a * 7 );
  document.querySelector('.Circle5').style.left = px5 + "px";
  document.querySelector('.Circle5').style.top = py5 + "px";

  var px6 = x + r6 * Math.cos(a * 4 );
  var py6 = y - r6 * Math.sin(a * 4 );
  document.querySelector('.Circle6').style.left = px6 + "px";
  document.querySelector('.Circle6').style.top = py6 + "px";

  var px7 = x + r1 * Math.cos(a * 22 / 1);
  var py7 = y - r1 * Math.sin(a * 22 / 1);
  document.querySelector('.Circle1').style.left = px1 + "px";
  document.querySelector('.Circle1').style.top = py1 + "px";

  var px8 = x + (r6 - 200) * Math.cos(a * 1);
  var py8 = y - (r6 - 200) * Math.sin(a * 1);
  document.querySelector('.Circle1').style.left = px8 + "px";
  document.querySelector('.Circle1').style.top = py8 + "px";

  var px9 = x + (r6 - 100) * Math.cos(a * 2);
  var py9 = y - (r6 - 100) * Math.sin(a * 2);
  document.querySelector('.Circle2').style.left = px9 + "px";
  document.querySelector('.Circle2').style.top = py9 + "px";



}


setInterval(function () {

  a = (a - Math.PI / 360) % (Math.PI * 2);
  rotate(a);

}, 5);
