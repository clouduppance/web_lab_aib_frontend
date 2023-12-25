let blockCounter = 0;
let redValue;
let greenValue;
let blueValue;

function updateBackgroundColor() {
  redValue = document.getElementById('inputRed').value;
  greenValue = document.getElementById('inputGreen').value;
  blueValue = document.getElementById('inputBlue').value;

  if (isValidColorValue(redValue) || isValidColorValue(greenValue) || isValidColorValue(blueValue)) {
    if(!isValidColorValue(redValue)) redValue = 0;
    if(!isValidColorValue(blueValue)) blueValue = 0;
    if(!isValidColorValue(greenValue)) greenValue = 0;
    colorArea = document.getElementById('colorArea');
    colorArea.style.backgroundColor = `rgb(${redValue}, ${greenValue}, ${blueValue})`;
  }
}

function generateBlock() {
  const blocksContainer = document.getElementById('blocksContainer');
  const block = document.createElement('div');
  block.className = 'colorBlock';
  block.style.backgroundColor = `rgb(${redValue}, ${greenValue}, ${blueValue})`;

  if (blockCounter < 10) {
    blocksContainer.appendChild(block);
    blockCounter++;
  } else {
    blocksContainer.removeChild(blocksContainer.firstChild);
    blocksContainer.appendChild(block);
  } 
}

function isValidColorValue(value) {
  return !isNaN(value) && parseInt(value) >= 0 && parseInt(value) <= 255;
}
