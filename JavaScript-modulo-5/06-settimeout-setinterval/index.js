console.log('Programa iniciado!')

// const timeoutId = setTimeout(() => {
//   console.log('3 segundos se passaram desde o início do programa.')
// }, 1000 * 3)

// clearTimeout(timeoutId)

let seconds = 0
const intervalId = setInterval(() => {
  seconds++
  console.log(`${seconds} segundos se passaram desde o início do programa.`)
  if (seconds > 10) {
    clearInterval(intervalId)
  }
}, 1000)
