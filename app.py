class machine:
    def __init__(self):
        print('----------------------------------')
        print('| Welcome to ABC vending machine.|')
        print('----------------------------------')

        # drinks & price
        self.drinks = [ 
            ['Coca-cola', 3], 
            ['Milo', 5], 
            ['Water', 1] ,
            ['100 Plus', 2],
            ['Sprite', 4]
        ]

        # go to menu
        self.display_menu()

    def display_menu(self):
        print('Please select a drink.')

        # display items
        for i in range(len(self.drinks)):
            print('{}. {} (RM {})'.format(i+1, self.drinks[i][0], self.drinks[i][1]))
    
        # get user's choice
        self.get_choice()

    def get_choice(self):
        v_input = input('>> (1-5): ')

        try:
            choice = int(v_input)-1
        except ValueError:
            print('!! Please input a valid number (1-5).')
            self.get_choice()
        else:
            if 0 <= choice <= 4:
                # display item's price
                self.display_total(choice)
            else:
                print('!! Please input a number between 1-5.')
                self.get_choice()

    def display_total(self, choice):
        print('----------------------------------')
        print('Item: {}'.format(self.drinks[choice][0]))
        print('Total: RM {}'.format(self.drinks[choice][1]))

        # go to payment
        self.payment(choice)

    def payment(self, choice):
        v_input = input('>> Insert money: RM ')

        try:
            cash = int(v_input)
        except ValueError:
            print('!! Please input a valid number.')
            self.payment(choice)
        else:
            if cash > self.drinks[choice][1]:
                # go to calculate change
                self.calc_change(self.drinks[choice][1], cash)
            elif cash == self.drinks[choice][1]:
                print('----------------------------------')
                print('No change required. Have a nice day :)')
            else:
                print('!! Insufficient amount. Please insert again.')
                self.payment(choice)

    def calc_change(self, total, payment):
        # get change
        change = payment - total

        # calculate notes needed
        notes = [100, 50, 20, 10, 5, 1]
        return_notes = {}

        for n in notes:
            if change >= n:
                num_notes = change // n
                return_notes[n] = num_notes
                change -= num_notes * n

        print('----------------------------------')
        print("Here's your change:")
        
        for note, num_notes in return_notes.items():
            print('- RM {} x{}'.format(note, num_notes))

        print('Have a nice day :)')
        print('----------------------------------')
    
if __name__ == '__main__':
    v_machine = machine()
    
