import pandas as pd


# read data

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    #race
    race_count = pd.value_counts(df['race'])

    #average_age_men
    average_age_men = round(df['age'].loc[df.sex == "Male"].mean(), 1)
    #bachelors
    helper_bachelors = df['education'].value_counts(normalize=1) * 100
    percentage_bachelors = round(helper_bachelors['Bachelors'], 1)
    #education

    high_salary_selection = df['salary'].loc[(df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')]
    low_salary_selection = df['salary'].loc[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')]

    high_salary_results = high_salary_selection.value_counts(normalize=1) * 100
    low_salary_results = low_salary_selection.value_counts(normalize=1) * 100

    higher_education = round(high_salary_results['>50K'], 1)
    lower_education = round(low_salary_results['>50K'], 1)

    #min
    minn = df['hours-per-week'].min()


    min_high_salary = df['age'].loc[(df['hours-per-week'] <= 1) & (df['salary'] == '>50K')]
    total_min_workers = df['age'].loc[(df['hours-per-week'] <= 1)].count()
    result = min_high_salary.count() / total_min_workers

    #salary country
    ca = df['native-country'].loc[df.salary == '>50K']
    ca = ca.value_counts()
    #print(ca)
    ca_all=df['native-country']
    ca_all = ca_all.value_counts()
    #print(test.value_counts())
    #ca_percentage = ca.value_counts(normalize=1)[0] * 100
    result = ca.divide(ca_all, fill_value=0).sort_values(ascending = False)
    #print(result.index[0])

    #india

    result_set = df['occupation'].loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    print(result_set.value_counts().index[0])

calculate_demographic_data()