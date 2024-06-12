from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This function is the entry point of the program. It loads the income data and life expectancy data from CSV files,
    retrieves the GNP (Gross National Product) and life expectancy values for a specific year, and plots a scatter plot
    of GNP vs life expectancy.

    Parameters:
    None

    Returns:
    None
    """
    year_column = "1900"
    income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")
    gnp = income_data[year_column]
    life_expectancy = life_expectancy_data[year_column]

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp, life_expectancy)
    plt.title(f"Life expectancy vs Gross domestic product (Year {year_column})")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()