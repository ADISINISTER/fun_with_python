const EventEmitter = require('events');

// Create a new instance of EventEmitter
const myEmitter = new EventEmitter();

// Define the function to sort an array of strings alphabetically
const sortStrings = (arr) => {
  const sortedArr = arr.sort();
  console.log(sortedArr);
}

// Define the function to search for a string in an array of strings
const searchStrings = (arr, searchString) => {
  const results = arr.filter(str => str.includes(searchString));
  console.log(results);
}

// Register the functions with the EventEmitter
myEmitter.on('sort', sortStrings);
myEmitter.on('search', searchStrings);

// Trigger the events to sort and search for a string in an array of strings
const stringArray = ['banana', 'apple', 'orange', 'pear', 'grape'];
myEmitter.emit('sort', stringArray); // Output: ['apple', 'banana', 'grape', 'orange', 'pear']
myEmitter.emit('search', stringArray, 'an'); // Output: ['banana', 'orange', 'grape']