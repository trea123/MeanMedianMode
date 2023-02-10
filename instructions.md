
# Question:

Calculate the mean, median, and mode of a given dataset.

---

## Additional Details:

+ Write a function to solve the mean of a given data set.

+ Write a function to solve the median of a given data set.

+ Write a function to solve the mode of a given data set.

Then, write a function that combines the usage of these functions into a single method capable of returning the mean, median, and mode of a data set based on user input.

You should have a **main** function that shows the usage of your aggregation function's purpose with example data sets.

---

## Structure Expectation

The structure of the application should be as follows:

```
calc_mean funtion
    takes in a dataset
    returns the mean

calc_median funtion
    takes in a dataset
    returns the median

calc_mode function
    takes in a dataset
    returns the mode

solve_dataset function
    takes in a dataset
    returns mean, median, and mode as a tuple

main function
    hard codes all datasets
    prints mean, median, and mode for each data set
```

---

## Logic Constraints

+ Each function, upon completion, should be committed separately.

+ The mean should be rounded to three decimal places.

+ The median should be rounded to two decimal places.

+ The mode should ALWAYS be returned as a list of modes (integers).

---

## Intermezzo Styling Constraints

+ Your functions should be documented using google style docstrings.

+ Your functions (all of them) should utilize proper annotations.

---

## Sample Data Sets

The datasets to use for completion are as follows...

```
[6, 9, 1, 2, 6, 3, 7]
[6, 9, 1, 2, 6, 3, 7, 4]
[6, 9, 1, 2, 6, 3, 7, 4, 1]
[6, 9, 1, 2, 3, 7, 4]
```
