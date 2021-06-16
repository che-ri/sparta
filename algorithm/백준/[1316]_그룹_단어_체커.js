const input = require('fs').readFileSync('dev/stdin').toString().split('\n');
let cnt = Number(input[0]);
input.shift();

for (let word of input) {
  let arr = [];
  for (let j = 0; j < word.length; j++) {
    if (!arr.includes(word[j])) arr.push(word[j]);
    else if (arr.includes(word[j]) && word[j - 1] === word[j]) continue;
    else {
      cnt--;
      break;
    }
  }
}

console.log(cnt);
