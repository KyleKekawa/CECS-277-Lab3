import random 

def roll_dice(dice):
    for i in range(len(dice)):
        dice[i] = random.randint(1,6)
        dice.sort(reverse=True)

def display_dice(name, dice):
    print(name + " =", ' '.join(map(str, dice)))

def find_winner(player_points):
    print("\nPlayer #1 points = ", player_points[0])
    print("Player #2 points = ", player_points[1])
    if player_points[0] > player_points[1]:
        print("Player #1 won!")
    elif player_points[1] > player_points[0]:
        print("Player #2 won!")

    else:
        print("It's a tie")

def main():
    player_points = [0,0]

    for player in range(2):
        print("\n - Ship, Captain, Crew!")
        print(f"Player #{player + 1}'s Turn:")
    
        dice_to_roll = [0, 0, 0, 0, 0]
        dice_to_keep = []
        
        for roll_num in range(3):
            roll_dice(dice_to_roll)
            display_dice("Roll", dice_to_roll)
            
            if 6 not in dice_to_keep and 6 in dice_to_roll:
                dice_to_keep.append(6)
                dice_to_roll.remove(6)
                print("Yo ho ho! Ye secured a ship!")
            
            if 5 not in dice_to_keep and 5 in dice_to_roll:
                dice_to_keep.append(5)
                dice_to_roll.remove(5)
                print("Shiver me timbers! A Captaiyn!")
            
            if 4 not in dice_to_keep and 4 in dice_to_roll:
                dice_to_keep.append(4)
                dice_to_roll.remove(4)
                print("Ye bribed a crew with Grog!")
            
            if 6 in dice_to_keep and 5 in dice_to_keep and 4 in dice_to_keep:
                cargo_points = sum(dice_to_roll)
                display_dice("Keep", dice_to_keep)
                display_dice("Cargo", dice_to_roll)
                print("Your cargo points are:", cargo_points)
                player_points[player] += cargo_points
                break
            
            display_dice("Keep", dice_to_keep)
            
            if roll_num < 2:
                roll_again = input("Roll again? (y/n) ").strip().lower()
                if roll_again != 'y':
                    break
        
    find_winner(player_points)

if __name__ == "__main__":
    main()