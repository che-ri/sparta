let input = require('fs').readFileSync('dev/stdin').toString().split(' ');

let num1 = Number(input[0]);
let num2 = Number(input[1]);

num2 -= 45;

if (num2 < 0) {
  num2 += 60;
  num1--;

  if (num1 === -1) {
    num1 = 23;
  }
}

console.log(num1 + ' ' + num2);
