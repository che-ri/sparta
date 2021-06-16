const number = Number(require('fs').readFileSync('dev/stdin').toString());
let cnt = 0;

for (let i = 666; ; i++) {
  if (`${i}`.includes('666')) {
    cnt++;
    if (cnt == number) {
      console.log(i);
      break;
    }
  }
}
