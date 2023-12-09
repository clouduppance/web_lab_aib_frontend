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

function isValidColorValue(value) {
  return !isNaN(value) && parseInt(value) >= 0 && parseInt(value) <= 255;
}
