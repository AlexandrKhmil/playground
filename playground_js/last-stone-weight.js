var lastStoneWeight = function(stones) {
  if (stones.length === 1) return stones[0]
  if (stones.length === 0) return 0

  const { max, abs } = Math

  const m1 = max(...stones)
  const m1_index = stones.indexOf(m1)
  stones = stones.filter((item, index) => index !== m1_index)

  const m2 = max(...stones)
  const m2_index = stones.indexOf(m2)
  stones = stones.filter((item, index) => index !== m2_index)

  console.log(stones)
  result = abs(m1 - m2)
  if (result !== 0) stones.push(result)
  return lastStoneWeight(stones)
}

console.log(lastStoneWeight([2, 2]))

//2,7,4,1,8,1