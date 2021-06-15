const input = require('fs')
  .readFileSync('dev/stdin')
  .toString()
  .split(' ')
  .map(ele => Number(ele));

const climb = input[0];
const slip = input[1];
const allDistance = input[2];
console.log(Math.ceil((allDistance - slip) / (climb - slip)));
//마지막날 달팽이가 올라가서 도착지점에 가면 내려갈 필요가 없으니, 애초부터 총 길이에서 내려가는 길이를 빼고, 달팽이가 도착할때까지 걸리는 총 일자를 구한다.
