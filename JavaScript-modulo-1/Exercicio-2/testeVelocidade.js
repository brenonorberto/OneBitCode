const nomeCarro1 = prompt('Insira o nome do 1º carro:')
const velocidadeCarro1 = prompt('Insira a velocidade do 1º carro:')
const nomeCarro2 = prompt('Insira o nome do 2º carro:')
const velocidadeCarro2 = prompt('Insira a velocidade do 2º carro:')

if (velocidadeCarro1 > velocidadeCarro2) {
  alert(veiculo1 + ' é mais rápido do que ' + veiculo2)
} else if (velocidadeCarro2 > velocidadeCarro1) {
  alert(velocidadeCarro2 + ' é mais rápido do que ' + velocidadeCarro1)
} else {
  alert(
    velocidadeCarro1 + ' e ' + velocidadeCarro2 + ' possuem velocidades iguais.'
  )
}
