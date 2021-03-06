import random
import pandas as pd
import matplotlib.pyplot as plt

# function that randomizes a coin toss by however many times user enters. (no error checking built in)
def coin_toss():
    heads = 0
    tails = 0
    coin_side = ["heads", "tails"]

    toss_count = int(input("How many coin flips would you like? : "))

    while toss_count > 0:
        toss_count -= 1
        if random.choice(coin_side) == "heads":
            heads += 1
        else:
            tails += 1

    print(f"Heads landed up {heads} times.")
    print(f"Tails landed up {tails} times.")

    if heads > tails:
        print(f"Heads showed up {heads - tails} times more than tails.")
    else:
        print(f"Tails showed up {tails - heads} times more than heads.")

    return heads, tails

# logic to keep the coin flips going. No error checking built in beyond a Yy or Nn input.
flip_again = True
toss_data_heads = []
toss_data_tails = []

while flip_again == True:
    roll = coin_toss()
    head_count = roll[0]  # This line and the one below extract from the tuple returned from the function
    tail_count = roll[1]

    more = input("Flip again? (Y or N): ")

    if more == "Y" or more == "y":
        toss_data_heads.append(head_count)
        toss_data_tails.append(tail_count)
        print(f"{toss_data_heads} for heads and {toss_data_tails} for tails.")
        flip_again = True

    elif more == "N" or more == "n":
        toss_data_heads.append(head_count)
        toss_data_tails.append(tail_count)
        print(f"{toss_data_heads} for heads and {toss_data_tails} for tails.")
        flip_again = False

    else:
        print("You must enter either Y or N!")
        flip_again = True

# create pandas dataset from the two lists
CoinDataSet = list(zip(toss_data_heads,toss_data_tails))
print(CoinDataSet)

# export to csv file
df = pd.DataFrame(data= CoinDataSet, columns=['Heads', 'Tails'])
df.to_csv('coinResults.csv', index=False, header=True)

# open data to a chart, change bar to line for different look
Location = r'C:\Users\TxCav\desktop\pythonCode\practice\coinResults.csv'
df = pd.read_csv(Location)

ax = df.plot(kind= 'line', title = "Heads or Tails", figsize= (15, 10), legend= True, fontsize= 14)
plt.show()






