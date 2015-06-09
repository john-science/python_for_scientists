# Stats with SciPy

For this problem set, we will be using real data. We will analyze the height and weight of the athletes at the 2012 London Olympics. You can find the CSV for this dataset [here](https://raw.githubusercontent.com/theJollySin/python_for_scientists/master/classes/11_scipy/london_2012_olympic_athlete_data.csv).

## Reading the Data

1. Use `DictReader` from `import csv` to read the CSV data file into a list of dictionaries named `athletes`, where each row is a dictionary.
2. Create a list named `ages` that is a simple list of integers of all the ages in our file.
3. Create two lists named `ages_female` and `ages_male` that is a simple list of integers of the ages of female and male athletes.
4. Create three lists `weights`, `weights_female`, and `weights_male`, much like parts 2 and 3, that are simple lists of integers values of the weights from `athletes`.
5. Create three lists `heights`, `heights_female`, and `heights_male`, much like parts 2 and 3, that are simple lists of integers values of the heights from `athletes`.
6. Create a list called `bmi`, which is a list of the body mass index (BMI) values for each athlete in our list. (**HINT**: BMI = weight {kg} / (height {meters} * height {meters}).)
7. Much like part 5, create two lists `bmi_female` and `bmi_male`, which include just the BMI values for the female and male atheletes respectively.

**NOTE**: This problem set deals with the [BMI](https://en.wikipedia.org/wiki/Body_mass_index) because it is easy to calculate for this particular data set. However, the BMI has many [limitations](https://en.wikipedia.org/wiki/Body_mass_index#Limitations), and it does not fully represent the health of the human body.

## Basic Stats

1. Find the mean and standard deviation of: `ages`, `ages_female`, and `ages_male`. What do you now know about the age of Olympic athletes? Is this what you expected?
2. Find the mean and standard deviation of: `heights`, `heights_female`, and `heights_male`. We probably expect the average man to be somewhat taller than the averge woman. Is that true for Olympic athletes?
3. Find the mean and standard deviation of: `weights`, `weights_female`, and `weights_male`. We probably expect the average man to be somewhat heavier than the averge woman. Is that true for Olympic athletes?
4. Find he mean and standard deviation of: `bmi`, `bmi_female`, and `bmi_male`. What is a typical BMI for an Olympic athlete?

## Stats

 * Coming Soon

#### Percentiles

    {'Name': 'Angelina Jolie', 'Age': '40', 'Sex': 'F', 'Weight (kg)': '56.5', 'Sport': 'Acting', 'Height (cm)': '173'}
    {'Name': 'Brad Pitt', 'Age': '52', 'Sex': 'M', 'Weight (kg)': '78', 'Sport': 'Acting', 'Height (cm)': '180'}


## Interpolation

 * Coming Soon


## Solutions

* [Stats - Solutions](problem_set_1_solutions.md)


[Back to Lecture](lecture_11.md)
