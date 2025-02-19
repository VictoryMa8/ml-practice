import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# penguins = sns.load_dataset('penguins')
flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')

def main():
    '''
    sns.lmplot(penguins,
            x = 'flipper_length_mm',
            y = 'bill_length_mm',
            hue = 'island',
    )
    plt.title('Biscoe Penguins Have Big Feet and Bills, Dream Penguins.. Just Bills')
    plt.xlabel('Flipper Length (mm)')
    plt.ylabel('Bill Length (mm)')
    plt.show()
    '''

    # print(penguins.describe())
    print(flights.describe())
    print(tips.describe())
    flights_list = flights.values.tolist()
    for i in flights_list:
        print(i[0])

    # penguins_list = penguins.values.tolist()
    # print(penguins_list)

if __name__ == "__main__":
    main()
