import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count().sort_values(ascending=False)

    # What is the average age of men?
    avgMaleAge = df.groupby('sex')['age'].mean().loc['Male']
    average_age_men = round(float(avgMaleAge), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelorCount = df.groupby('education')['education'].count().loc['Bachelors']
    totalCount = df['education'].count()
    percentageBachelors = round((bachelorCount/totalCount) * 100, 1)
    percentage_bachelors = percentageBachelors

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    higherEdCount = df['education'].loc[df['education'].isin(['Bachelors','Masters','Doctorate'])].count()
    lowerEdCount = df['education'].loc[~df['education'].isin(['Bachelors','Masters','Doctorate'])].count()
    higherEd50KCount = df['education'][df['education'].isin(['Bachelors','Masters','Doctorate']) & (df['salary'] == '>50K')].count()
    lowerEd50KCount = df['education'][~df['education'].isin(['Bachelors','Masters','Doctorate']) & (df['salary'] == '>50K')].count()

    higherEdPercent = round((higherEd50KCount/higherEdCount) * 100, 1)
    lowerEdPercent = round((lowerEd50KCount/lowerEdCount) * 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = higherEdPercent
    lower_education_rich = lowerEdPercent

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minHourCount = df['hours-per-week'][df['hours-per-week'] == df['hours-per-week'].min()].count()
    richMinHourCount = df['hours-per-week'][(df['salary'] == '>50K') & (df['hours-per-week'] == df['hours-per-week'].min())].count()
    richPercentage = round((richMinHourCount/minHourCount) * 100, 1)

    num_min_workers = None

    rich_percentage = richPercentage

    # What country has the highest percentage of people that earn >50K?
    salaryCountdf = df[['salary','native-country']][(df['salary'] == '>50K')].groupby('native-country').count().sort_values(by='native-country')
    countryCountdf = df[['salary','native-country']].groupby('native-country').count().sort_values(by='native-country')
    countryCountdf['percentage'] = salaryCountdf['salary']/countryCountdf['salary']
    highestCountry = countryCountdf[countryCountdf['percentage'] == countryCountdf['percentage'].max()]
    highestCountryPercentage = round((float(highestCountry['percentage'])) * 100, 1)

    highest_earning_country = highestCountry.index.tolist()[0]
    highest_earning_country_percentage = highestCountryPercentage

    # Identify the most popular occupation for those who earn >50K in India.
    df = df[['occupation','native-country']][(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation').count()
    df = df[df['native-country'] == df['native-country'].max()]

    top_IN_occupation = df.index.tolist()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
