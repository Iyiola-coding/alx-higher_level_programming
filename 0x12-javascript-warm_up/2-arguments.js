#!/usr/bin/node
/* script that prints a message depending of the number of arguments passed */
const args = process.argv;

if (args.lenght <= 2) {
  console.log('No argument');
} else if (args.lenght === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
