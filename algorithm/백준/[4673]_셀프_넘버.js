function numPlusDigits(num) {
  const toStringNum = num.toString();
  let sumDigits = 0;

  for (let i = 0; i < toStringNum.length; i++) {
    sumDigits += Number(toStringNum[i]);
  }

  const result = sumDigits + num;
  return result;
}

let sumResult = [];
for (let i = 1; i <= 10000; i++) {
  sumResult.push(numPlusDigits(i));
}
sumResult = new Set(sumResult.sort((a, b) => a - b));

for (let i = 1; i <= 10000; i++) {
  if (!sumResult.has(i)) console.log(i);
}
