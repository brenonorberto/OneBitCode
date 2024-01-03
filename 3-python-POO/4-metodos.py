class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Nome do Filme: {self.name} - Ano de Lançamento: {self.yearLaunch}"

    def technical_sheey(self):
        print("#### Dados Filme ####")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(
            f"Plano incluído: {'Sim' if self.includedPlan else 'Não'}"
        )
        print(f"Avaliação do Filme: {self.note}")
        print(f"Duração do Filme: {self.durationMinutes}\n")


movie = Movie("Top Gun Maverick", 2022, False, 5.0, 120)
movie2 = Movie("Super Mario", 1985, True, 4.5, 100)
movie.technical_sheey()
movie2.technical_sheey()
