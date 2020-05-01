/*
  Say you have an array prices for which the ith element is the price of a given stock on day i.
  Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
  Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
*/

// IN: [7,1,5,3,6,4]
// OUT: 7
// EXP: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

const maxProfit = prices => {
  const { max } = Math

  let best_without_stock = 0, best_with_stock = -999999;

  for (x of prices) {
    best_with_stock = max(best_with_stock, best_without_stock - x);
    best_without_stock = max(best_without_stock, best_with_stock + x);
  }
  
  return best_without_stock
}

console.log(maxProfit([7,1,5,3,6,4]))

