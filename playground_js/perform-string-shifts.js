/*
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

    direction can be 0 (for left shift) or 1 (for right shift). 
    amount is the amount by which string s is to be shifted.
    A left shift by 1 means remove the first character of s and append it to the end.
    Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
*/

// Input: s = "abc", shift = [[0,1],[1,2]
// Output: "cab"
// Exp: 
// [0,1] means shift to left by 1. "abc" -> "bca" 
// [1,2] means shift to right by 2. "bca" -> "cab"

const stringShift = (s, shift) => {
  let a = (s) => s[s.length - 1] + s.slice(0, s.length - 1);
  let b = (s) => s.slice(1, s.length) + s[0];

  for (let x of shift) {
    let f = x[0] === 0 ? b : a; 
    for (let i = 0; i < x[1]; i++) {
      s = f(s);
    }
  }

  return s;
};

console.log(stringShift("abc", [[0,1],[1,2]]));