var timer = 0;
var timerInterval;
var ms = document.getElementById('ms');
var second = document.getElementById('second');
var minute = document.getElementById('minute');
var res = document.getElementById('to-send')

function vpered() {
  sanovka();
  timerInterval = setInterval(function() {
  timer += 1/60;
  msVal = Math.floor((timer - Math.floor(timer))*100);
  secondVal = Math.floor(timer) - Math.floor(timer/60) * 60;
  minuteVal = Math.floor(timer/60);
  ms.innerHTML = msVal < 10 ? "0" + msVal.toString() : msVal;
  second.innerHTML = secondVal < 10 ? "0" + secondVal.toString() : secondVal;
  minute.innerHTML = minuteVal < 10 ? "0" + minuteVal.toString() : minuteVal;
  }, 1000/60);
}

function sanovka() {
  clearInterval(timerInterval);
}

function end() {
    res.value = minuteVal * 100 + secondVal;
}

vpered();