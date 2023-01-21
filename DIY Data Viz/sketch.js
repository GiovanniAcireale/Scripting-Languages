let message;
var lines;
var counts;
var total;

function preload() 
{
  lines = loadStrings('libraries/AoW.txt');
}

function setup() 
{
  createCanvas(400, 400);
  background(0, 0, 0);  
  
  var params = {ignoreStopWords: true, ignoreCase: true, ignorePunctuation: true};
  
  counts = RiTa.concordance(lines.join(" "), params); 
  total = totalValues(counts);

  textAlign(CENTER, CENTER);
  textSize(28);
  noStroke();
  fill(random(255));
  noLoop();
}

function draw() 
{
  
  for (var a in counts) 
  {
    if (counts.hasOwnProperty(a)) 
    {
      if (counts[a]/total > 0.001) 
      {
        fill(random(255), random(255), random(255));
        textSize((counts[a]/total) * 10000);
        text(a, random(width), random(height));
      }
    }
  }
}

function totalValues(obj) 
{
  var total = 0;
  
  for (var a in obj) 
  {
    if (obj.hasOwnProperty(a)) 
    {
      total += obj[a];
    }
  }
  
  return total;
}