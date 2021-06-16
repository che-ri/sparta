let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const AllCases = Number(input[0]);

for (let i = 1; i <= AllCases; i++) {
  let arr = input[i].split(' ');
  let len = Number(arr[0]);

  let sum = 0;
  for (let j = 1; j <= len; j++) {
    sum += Number(arr[j]);
  }

  const ave = sum / len;
  let passlen = 0;
  for (let j = 1; j <= len; j++) {
    if (arr[j] > ave) passlen++;
  }
  result = (passlen / len) * 100;
  console.log(result.toFixed(3) + '%');
}
