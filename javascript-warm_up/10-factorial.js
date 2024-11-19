#!/usr/bin/node
function fractional (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(fractional(num));
}
