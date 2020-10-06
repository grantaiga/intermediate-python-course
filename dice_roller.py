def main():
    import random
    dice_size = input('Size?')
    dice_sum = 0
    roll_times = 0
    while True:
        roll = random.randint(1, int(dice_size))
        dice_sum += roll
        roll_times += 1
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail!')
        elif roll == int(dice_size):
            print(f'You rolled a {roll}! Critical Success!')
            break
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')
    print(f'You rolled {roll_times} times.')


if __name__ == "__main__":
    main()
