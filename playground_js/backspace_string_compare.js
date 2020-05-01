const backspaceCompare = (S, T) => {
  return stringProcessing(S) === stringProcessing(T)
}

const stringProcessing = str => {
  for(let i = 0; i < str.length; i++){
    if(str[i] === '#'){
      if(i === 0){
        str = str.slice(1, str.length)
        i--
      } else {
        str = str.slice(0, i - 1) + str.slice(i + 1, str.length)
        i -= 2
      }
    }
  }
  return str
}

console.log(backspaceCompare("ab#c", "ad#c"))