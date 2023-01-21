let bg;
var lines;
var counts;
var total;

function preload() {
  lines = loadStrings('libraries/hobbit.txt');
}

function setup() {
  createCanvas(700, 540);
  background(255);  
  var params = {
    ignoreStopWords: true,
    ignoreCase: true,
    ignorePunctuation: true
  };
  counts = RiTa.concordance(lines.join(" "),
    params); 
  total = totalValues(counts);

  textAlign(CENTER, CENTER);
  textSize(24);
  noStroke();
  fill(random(255));
  noLoop();
}
function draw() {
  
  for (var k in counts) {
    if (counts.hasOwnProperty(k)) {
      if (counts[k]/total > 0.001) {
        fill(0, random(255), random(255));
        textSize((counts[k]/total) * 10000);
        text(k, random(width), random(height));
      }
    }
  }
}
function totalValues(obj) {
  var total = 0;
  for (var k in obj) {
    if (obj.hasOwnProperty(k)) {
      total += obj[k];
    }
  }
  return total;
}