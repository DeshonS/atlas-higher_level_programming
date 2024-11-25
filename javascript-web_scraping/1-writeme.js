#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

try {
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(content);
} catch (error) {
  console.log(error);
}
