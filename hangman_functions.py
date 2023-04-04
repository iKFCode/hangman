def intro_hangman():
    intro = '\n'
    intro += '?' * 80
    intro += '\n\t\t Wellcome to the game Hangman!\n'
    intro += 'Here in this game you only have one task: guees the chosen word in'
    intro += '\nas many attemps as you are given otherwise you are going to be'
    intro += '\nhung up and killed!'
    intro += '\nYou seem to be ready. Let\'s go!!!\n'
    intro += '?' * 80
    intro += '\n'

    print (intro)


def list_provider():
    """
    For incrasing readability of written code of this program, and for having
    a more organised structure this function is created to return a simple list of 
    100 words.
    """
    # This is a list of 100 most commonly used English nouns.
    common_nouns = ['time',
                'year',
                'people',
                'way',
                'day',
                'man',
                'thing',
                'woman',
                'life',
                'child',
                'world',
                'school',
                'state',
                'family',
                'student',
                'group',
                'country',
                'problem',
                'hand',
                'part',
                'place',
                'case',
                'week',
                'company',
                'system',
                'program',
                'question',
                'work',
                'government',
                'number',
                'night',
                'point',
                'home',
                'water',
                'room',
                'mother',
                'area',
                'money',
                'story',
                'fact',
                'month',
                'lot',
                'right',
                'study',
                'book',
                'eye',
                'job',
                'word',
                'business',
                'issue',
                'side',
                'kind',
                'head',
                'house',
                'service',
                'friend',
                'father',
                'power',
                'hour',
                'game',
                'line',
                'end',
                'member',
                'law',
                'car',
                'city',
                'community',
                'name',
                'president',
                'team',
                'minute',
                'idea',
                'kid',
                'body',
                'information',
                'back',
                'parent',
                'face',
                'others',
                'level',
                'office',
                'door',
                'health',
                'person',
                'art',
                'war',
                'history',
                'party',
                'result',
                'change',
                'morning',
                'reason',
                'research',
                'girl',
                'guy',
                'moment',
                'air',
                'teacher',
                'force',
                'education',
                'foot',
                'boy']
    return common_nouns


def play_hangman(word, hint, attempts=6):
    """
    This function take in three parameters. Parameter 'word' is a word that
    need to be guessed, parameter 'hint' is the hint that will be shown to the 
    user, and parameter attemp determines the number of chances 
    a user have to guess the word correctly.

    The function will check the word's length, convert the length of that word 
    into dashes, asks the user to input a letter, and checks if the letter 
    exists in the word. If it does it replaces the letter with the dash in 
    the correct position that the letter was found.

    And, the function keep on running untill the user guesses word correctly, or 
    the number of attemps go to 0, or the user presses the keyword '0'.

    """
    # Giving the user a hint.
    print(hint, end=' ')

    # Convert word to list of dashes
    current_word = list('-' * len(word))
    
    # Keep track of letters guessed so far
    guessed_letters = []
    
    # Loop until user guesses the word or runs out of attempts
    while attempts > 0:
        print(' '.join(current_word))
        print(f'You have {attempts} attempts left.')
        
        # Ask user for a letter
        guess = input('\nGuess a letter (or 0 to quit): ').lower()
        
        # Check if user wants to quit
        if guess == '0':
            print('Quitting...')
            return
        
        # Check if user already guessed this letter
        if guess in guessed_letters:
            print(f'You already guessed "{guess}". Try another letter.')
            continue
        
        # Add guessed letter to list of guessed letters
        guessed_letters.append(guess)
        
        # Check if guessed letter is in the word
        if guess in word:
            print(f'Nice one! "{guess}" is in the word.')
            
            # Replace dashes with guessed letter in the correct positions
            for i in range(len(word)):
                if word[i] == guess:
                    current_word[i] = guess
                    
            # Check if user guessed the whole word
            if ''.join(current_word) == word:
                print(f'\nCongratulations, you guessed the word "{word}"!')
                return
        
        else:
            print(f'Sorry, "{guess}" is not in the word.')            
            # Decrease number of attempts
            attempts -= 1
    
    # Ran out of attempts
    print(f'Game over! The word was "{word}".')