# Stats with SciPy

## Reading the Data

#### 1. Use `DictReader` from `import csv` to read the CSV data file into a list of dictionaries, where each row is a dictionary.

    >>> import csv
    >>> f = open('london_2012_olympic_athlete_data.csv', 'r')
    >>> dict_reader = csv.DictReader(f)
    >>> athletes = []
    >>> for row in dict_reader:
    ...     athletes.append(row)

#### 2. Create a list named `ages` that is a simple list of integers of all the ages in our file.

    >>> ages = []
    >>> for athlete in athletes:
    ...     ages.append(int(athlete['Age']))

#### 3. Create two lists named `ages_female` and `ages_male` that is a simple list of integers of the ages of female and male athletes.

    >>> ages_female = []
    >>> ages_male = []
    >>> 
    >>> for athlete in athletes:
    ...     if athlete['Sex'] == 'F':
    ...         ages_female.append(int(athlete['Age']))
    ...     else:
    ...         ages_male.append(int(athlete['Age']))

#### 4. Create three lists `weights`, `weights_female`, and `weights_male`, much like parts 2 and 3, that are simple lists of integers values of the weights from `athletes`.

    >>> weights = []
    >>> weights_female = []
    >>> weights_male = []
    >>> 
    >>> for athlete in athletes:
    >>>     weights.append(int(athlete['Weight (kg)']))
    >>>     if athlete['Sex'] == 'F':
    >>>         weights_female.append(int(athlete['Weight (kg)']))
    >>>     else:
    >>>         weights_male.append(int(athlete['Weight (kg)']))

#### 5. Create three lists `heights`, `heights_female`, and `heights_male`, much like parts 2 and 3, that are simple lists of integers values of the heights from `athletes`.

    >>> heights = []
    >>> heights_female = []
    >>> heights_male = []
    >>> 
    >>> for athlete in athletes:
    >>>     heights.append(int(athlete['Height (cm)']))
    >>>     if athlete['Sex'] == 'F':
    >>>         heights_female.append(int(athlete['Height (cm)']))
    >>>     else:
    >>>         heights_male.append(int(athlete['Height (cm)']))

#### 6. Create a list called `bmi`, which is a list of the body mass index (BMI) values for each athlete in our list. (**HINT**: BMI = weight {kg} / (height {meters} * height {meters}).)

    >>> bmi = []
    >>> 
    >>> for athlete in athletes:
    >>>     num = int(athlete['Weight (kg)'])
    >>>     denom = int(athlete['Height (cm)']) / 100.0
    >>>     bmi.append(num / (denom * denom))

#### 7. Much like part 5, create two lists `bmi_female` and `bmi_male`, which include just the BMI values for the female and male atheletes respectively.

    >>> weights = []
    >>> weights_female = []
    >>> weights_male = []
    >>> 
    >>> for athlete in athletes:
    >>>     weights.append(int(athlete['Weight (kg)']))
    >>>     if athlete['Sex'] == 'F':
    >>>         weights_female.append(int(athlete['Weight (kg)']))
    >>>     else:
    >>>         weights_male.append(int(athlete['Weight (kg)']))

## Basic Stats

 * Coming Soon

## Stats

 * Coming Soon

## Interpolation

 * Coming Soon


[Back to Problem Set](problem_set_1_scipy.md)
