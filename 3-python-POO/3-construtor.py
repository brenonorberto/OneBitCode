class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Nome do Filme: {self.name} - Ano de Lançamento: {self.yearLaunch}"


movie = Movie("Top Gun Maverick", 2022, False, 5.0, 120)
movie2 = Movie("Super Mario", 1985, True, 4.5, 100)
print(movie2)
