import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

def main():
    penguins.plot(kind = "scatter",
                x= "flipper_length_mm",
                y = "body_mass_g")

    sns.lmplot(penguins,
            x = 'flipper_length_mm',
            y = 'bill_length_mm',
            hue = 'island',
    )

    plt.title('Biscoe Penguins Have Big Feet and Bills, Dream Penguins.. Just Bills')
    plt.xlabel('Flipper Length (mm)')
    plt.ylabel('Bill Length (mm)')
    plt.show()

if __name__ == "__main__":
    main()
