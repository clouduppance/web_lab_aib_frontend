let blockCounter = 0;
let palleteColor;
let saved = false;
let savedColor;

function updateBackgroundColor() {
  redValue = document.getElementById('inputRed').value;
  greenValue = document.getElementById('inputGreen').value;
  blueValue = document.getElementById('inputBlue').value;

  if (isValidColorValue(redValue) || isValidColorValue(greenValue) || isValidColorValue(blueValue)) {
    if(!isValidColorValue(redValue)) redValue = 0;
    if(!isValidColorValue(blueValue)) blueValue = 0;
    if(!isValidColorValue(greenValue)) greenValue = 0;
    colorArea = document.getElementById('colorArea');
    palleteColor = `rgb(${redValue}, ${greenValue}, ${blueValue})`;
    colorArea.style.backgroundColor = palleteColor;
  }
}

function generateBlock() {
  const blocksContainer = document.getElementById('blocksContainer');
  const block = document.createElement('div');
  block.className = 'colorBlock';
  block.style.backgroundColor = palleteColor;

  if (blockCounter < 10) {
    blocksContainer.appendChild(block);
    blockCounter++;
  } else {
    blocksContainer.removeChild(blocksContainer.firstChild);
    blocksContainer.appendChild(block);
  } 
}

document.addEventListener('click', function (event) {
  if (event.target.classList.contains('colorBlock')) {
    if(!saved) {
      savedColor = event.target.style.backgroundColor;
      saved = true;
    }

    event.target.style.backgroundColor = savedColor;
  }
});

function isValidColorValue(value) {
  return !isNaN(value) && parseInt(value) >= 0 && parseInt(value) <= 255;
}
