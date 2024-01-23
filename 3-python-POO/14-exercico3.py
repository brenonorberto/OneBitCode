from exercicio3 import Trip

trip0 = Trip("Lençois Maranhense")
trip1 = Trip("Florianopolis")
trip2 = Trip("Caldas Novas")
trip3 = Trip("Gramado")
trip4 = Trip("São Paulo")

print("E aí viajante. Temos algumas ofertas para você!")
traveler = input("Digite seu nome para começarmos: ")
print(f"{traveler} temos 5 destinos que combinam com você:"
      '''
[0] Lenås Maranhense
[1] Florianópolis
[2] Caldas Novas
[3] Gramado
[4] São Paulo
''')

choice = int(input("Selecione o destino da viajem desejada: "))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:  # caso usuário não digite a opção correta
    if choice >= 5:
        print("Esta opção não está incluída em nossos destinos.")
        break
    if choice <= 4:  # verifica a seleção
        # resultado
        print(
            f"{traveler} sua viagem para {list_trip[choice].destiny} está marcada.")
        print("Volte sempre!")
        break
