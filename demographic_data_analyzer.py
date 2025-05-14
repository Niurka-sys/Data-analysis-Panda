import pandas as pd

def calculate_demographic_data(print_data=True):
    # Nombres de las columnas del archivo CSV
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "hours-per-week", "native-country", "salary"
    ]

    # Cargar el archivo CSV con los nombres de columna correctos
    df = pd.read_csv("adult.data.csv", names=column_names, skipinitialspace=True)

    # 1. Cantidad de personas por raza
    race_count = df['race'].value_counts()

    # 2. Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje de personas con título universitario (Bachelors)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Dividir entre educación avanzada y básica
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Porcentaje de ricos con educación avanzada
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)

    # Porcentaje de ricos con educación básica
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 5. Mínimo número de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 6. Porcentaje de ricos que trabajan pocas horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. País con el mayor porcentaje de personas que ganan más de 50K
    rich_by_country = (
        df[df['salary'] == '>50K']['native-country'].value_counts() /
        df['native-country'].value_counts()
    )

    # Asegurarse de eliminar posibles valores vacíos
    rich_by_country = rich_by_country.dropna()

    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max() * 100, 1)

    # 8. Ocupación más común entre los ricos en India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation'].value_counts().idxmax()
    )

    # Si el parámetro está activado, imprimimos los resultados
    if print_data:
        print("Race Count:\n", race_count)
        print("Average Age of Men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Higher education rich %:", higher_education_rich)
        print("Lower education rich %:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich in country:", highest_earning_country_percentage)
        print("Top occupation in India for >50K:", top_IN_occupation)

    # Devolver todos los resultados en un diccionario
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }