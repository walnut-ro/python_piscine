from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This function loads a dataset of life expectancy in years, extracts the data for Finland,
    and plots the life expectancy over the years using matplotlib.

    Parameters:
    None

    Returns:
    None
    """
    dataset = load("life_expectancy_years.csv")
    finland_data = dataset[dataset['country'] == 'Finland']
    years = finland_data.columns[1:]
    life_expectancy = finland_data.values[0][1:]

    plt.plot(years, life_expectancy, label='Finland')
    plt.title('Life Expectancy in Fiinland Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()