from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Preprocesses the population string and returns the corresponding population value.

    Parameters:
    pop_str (str): The population string to be preprocessed.

    Returns:
    float: The preprocessed population value.

    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    Loads population data from a CSV file, processes and
    plots(used for creating line plots)
    the population comparison of three countries.
    """
    data = load("population_total.csv")

    countries = ["Finland", "France"]

    data_1 = data[data['country'] == countries[0]].iloc[:, 1:]
    data_2 = data[data['country'] == countries[1]].iloc[:, 1:]

    pop_1 = data_1.values.flatten()
    pop_2 = data_2.values.flatten()
    
    years = data_1.columns.astype(int)

    pop_1 = [preprocess_population(pop) for pop in pop_1]
    pop_2 = [preprocess_population(pop) for pop in pop_2]

    plt.plot(years, pop_1, label=countries[0])
    plt.plot(years, pop_2, label=countries[1])

    plt.title("Population in {} and {}".format(countries[0], countries[1]))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(pop_1), max(pop_2))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()