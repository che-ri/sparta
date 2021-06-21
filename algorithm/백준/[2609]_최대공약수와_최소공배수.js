const [firstnum, lastnum] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .split(' ')
  .map(ele => Number(ele));

let gcd = 0;
let comp1 = firstnum;
let comp2 = lastnum;
let storage = 0;
while (true) {
  if (comp1 % comp2 !== 0) {
    storage = comp2;
    comp2 = comp1 % comp2;
    comp1 = storage;
  } else {
    gcd = comp2;
    console.log(gcd);
    break;
  }
}

console.log((firstnum * lastnum) / gcd);
