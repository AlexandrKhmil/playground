() => {
  const getAllVariations = (size, result) => {
    if(size === 0) return [result]
    return [
      ...getAllVariations(size - 1, [...result, false]),
      ...getAllVariations(size - 1, [...result, true]),
    ]
  }

  const maxProfit = prices => { 
    const actionOptions = getAllVariations(prices.length, [])
    let max = 0
    for(let option of actionOptions) { 
      let sum = 0
      let flag = false
      for(let i = 0; i < option.length; i++){
        if(option[i]){
          sum += flag ? prices[i] : -prices[i]
          flag = !flag
        }
      }
      if(sum > max) max = sum
    }
    return max
  }

  console.log(maxProfit([7, 1, 5, 3, 6, 4]))
}

(() => {
  const calculateSum = (variants, sum, key) => {
    if(variants.length === 0) return [sum]
    return (variants[0][1] >= key) 
      ? [
          ...calculateSum(variants.slice(1, variants.length), sum, key),
          ...calculateSum(variants.slice(1, variants.length), sum + variants[0][0], variants[0][2]),
        ]
      : [
        ...calculateSum(variants.slice(1, variants.length), sum, key),
        ]
  }

  const maxProfit = prices => { 
    let variants = []
    for(let priceIndx = 0; priceIndx < prices.length; priceIndx++){
      for(let otherPriceIndx = priceIndx + 1; otherPriceIndx < prices.length; otherPriceIndx++){
        let sum = -prices[priceIndx] + prices[otherPriceIndx]
        if(sum > 0) {
          variants.push([sum, priceIndx, otherPriceIndx])
        }
      } 
    } 
    return Math.max(...calculateSum(variants, 0, 0))
  }

  console.log(maxProfit([7, 1, 5, 3, 6, 4]))
})()