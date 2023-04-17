from pick import pick


class Counter():
    player_score = 0
    computer_score = 0

    def checkWinner(self):
        if(self.player_score > self.computer_score):
            print('-------------------------------------------')
            print(
                f'Twój wynik: {self.player_score}, wynik komputera: {self.computer_score}')
            print("Wygrałeś grę!")
            print('-------------------------------------------')
        elif(self.player_score < self.computer_score):
            print('-------------------------------------------')
            print(
                f'Twój wynik: {self.player_score}, wynik komputera: {self.computer_score}')
            print("Komputer wygrał")
            print('-------------------------------------------')
        else:
            print('-------------------------------------------')
            print(
                f'Twój wynik: {self.player_score}, wynik komputera: {self.computer_score}')
            print("Remis!")
            print('-------------------------------------------')

    def checkRoundWinner(self, playerChoice, computerChoice):
        if playerChoice == 'Kamień' and computerChoice == "Nożyce":
            self.player_score += 1
            playerChoice, index = pick(['Świetnie'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Wygrałeś rundę!",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Kamień' and computerChoice == "Papier":
            self.computer_score += 1
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Przegrałeś rundę...",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Kamień' and computerChoice == "Kamień":
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Remis!",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Nożyce' and computerChoice == "Papier":
            self.player_score += 1
            playerChoice, index = pick(['Świetnie'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Wygrałeś rundę!",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Nożyce' and computerChoice == "Kamień":
            self.computer_score += 1
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Przegrałeś rundę...",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Nożyce' and computerChoice == "Nożyce":
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Remis!",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Papier' and computerChoice == "Kamień":
            self.player_score += 1
            playerChoice, index = pick(['Świetnie'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Wygrałeś rundę!",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Papier' and computerChoice == "Nożyce":
            self.computer_score += 1
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Przegrałeś rundę...",
                                       indicator='=>', default_index=0)
        elif playerChoice == 'Papier' and computerChoice == "Papier":
            playerChoice, index = pick(['Ok'], f"Wybrałeś {playerChoice}, komputer wybrał {computerChoice}. Remis!",
                                       indicator='=>', default_index=0)
        else:
            playerChoice, index = pick(['Ok'], f"Uwaga coś mogło pójść nie tak!",
                                       indicator='=>', default_index=0)
