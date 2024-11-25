#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);