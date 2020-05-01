// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
// in - [-2,1,-3,4,-1,2,1,-5,4]
// out - 6
// exp - [4,-1,2,1] has the largest sum = 6.

// Enter Point
const maxSubArray = nums => {
  let max = nums[0]
  for (let j = 0; j < nums.length; j++) {
    sum = 0
    for (let i = j; i < nums.length; i++) {
      sum += nums[i]
      if (sum > max) max = sum
    }
  }
  return max
}

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
