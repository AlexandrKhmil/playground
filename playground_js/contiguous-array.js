/*
 * Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
 *
 * @param {number[]} nums
 * @return {number}
 */

const findMaxLength = (nums) => {
  let max = 0;
  for (let start = 0; start < nums.length; start++) {
    for (let end = start + 1; end < nums.length; end += 2) {
      let arr = nums.slice(start, end + 1);
      let sum = arr.reduce((prev, item) => prev + item);
      if ((sum === arr.length / 2) && sum > max) max = sum;
    } 
  }
  return max * 2;
};

console.log(findMaxLength([0,1]))