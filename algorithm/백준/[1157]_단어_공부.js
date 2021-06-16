const input = require('fs').readFileSync('/dev/stdin').toString().trim();

function maxAlphabet(str) {
  const word = str.toUpperCase();
  let Alphabet = {};

  for (let i of word) {
    if (!Alphabet.hasOwnProperty(i)) Alphabet[i] = 1;
    else Alphabet[i] += 1;
  }

  let max = Number.MIN_SAFE_INTEGER;
  let answer = '';
  for (let i in Alphabet) {
    if (max < Alphabet[i]) {
      max = Alphabet[i];
      answer = i;
    } else if (max === Alphabet[i]) {
      answer = '?';
    }
  }

  console.log(answer);
}

maxAlphabet(input);
