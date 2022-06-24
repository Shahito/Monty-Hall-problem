from game import *
from prettytable import PrettyTable

# attemps and loop numbers
N_ATTEMPTS=5
N_ROLLS=100

# printable win rate table (pretty ascii render)
result_table=PrettyTable()

# table field names
result_table.field_names=["Attempts","Changing door","Keeping door"]

# attempts loop
for n in range(N_ATTEMPTS):
    # games played for each win rate calculation
    # loop variables reinit
    attempts,win_with_change,win_without_change=0,0,0
    for m in range(N_ROLLS):
        g=Game() # game initialization
        g.set_random_price() # set a random door to hide the gain
        g.choose_door() # choose a random door (simulate user choice)
        g.open_empty_door() # randomly open an available door
        g.change_chosen_door() # change the chosen door after opening an empty door

        # calculate win rate (change or keep chosen door)
        attempts+=1
        if g.get_result()==True:
            win_with_change+=1
        else:
            win_without_change+=1

    # add row with results to the table
    result_table.add_row([n+1,f"{int(win_with_change/attempts*100)}%",f"{int(win_without_change/attempts*100)}%"])

# display the ascii table
print(result_table)