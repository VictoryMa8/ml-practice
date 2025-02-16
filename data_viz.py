import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
flights = sns.load_dataset('flights')

def main():
    sns.lmplot(penguins,
            x = 'flipper_length_mm',
            y = 'bill_length_mm',
            hue = 'island',
    )
    plt.title('Biscoe Penguins Have Big Feet and Bills, Dream Penguins.. Just Bills')
    plt.xlabel('Flipper Length (mm)')
    plt.ylabel('Bill Length (mm)')
    plt.show()

    print(penguins.head())
    print(penguins.info())
    print(penguins.describe())

if __name__ == "__main__":
    main()
