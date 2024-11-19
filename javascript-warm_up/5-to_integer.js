#!/usr/bin/node
const args = process.argv.slice(2);
const first = parseInt(args[0], 10);
if (isNaN(first)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + first);
}
