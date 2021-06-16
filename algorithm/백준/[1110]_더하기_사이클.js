let input = Number(require('fs').readFileSync('/dev/stdin').toString());
let a = Number(input);

let result = Number.MIN_SAFE_INTEGER;
let cnt = 0;
if (a < 10) a *= 10;

while (result !== a) {
  cnt += 1;
  if (cnt === 1) result = a;
  let one = result % 10;
  let ten = Math.floor((result % 100) / 10);
  result = one * 10 + ((one + ten) % 10);
}
console.log(cnt);
