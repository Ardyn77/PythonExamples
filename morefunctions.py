def ask_ok(prompt, retries=2, reminder = 'please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries-1
        if retries < 0:
            raise ValueError('invalid response')
        print(reminder)
ask_ok('do you want to quit?')