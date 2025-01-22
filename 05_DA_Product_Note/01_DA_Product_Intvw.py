"""

_____________________________________________________________________________

05 (DA)
_____________________________________________________________________________

-----------------------------------------------------------------------------------------------------------------------------

Goldman Sachs

SQL:

 1. Calculate the average salary for each department from the table.
 2. Write a SQL query to display the employee’s name along with their manager’s name using a self-join on the ‘employees’ table, which contains ‘emp_id’, ‘name’, and ‘manager_id’ columns.
 3. Find the most recent hire for each department (solved using LEAD/LAG functions).
 4. Write a query to retrieve the nth highest salary from the Employees table, which has ‘EmployeeID’, ‘Name’, and ‘Salary’ columns.

Power BI:

 1. What is meant by Filter context in DAX?
 2. Explain the process of implementing Row-Level Security (RLS) in Power BI.
 3. Describe the different types of filters available in Power BI.
 4. What’s the difference between the ‘ALL’ and ‘ALLSELECTED’ functions in DAX?
 5. How would you use DAX to calculate total sales for a specific product?

Python:

 1. Create a dictionary, add elements, update a specific entry, and print the dictionary sorted by key in alphabetical order.
 2. Identify unique values from a list of numbers and print how many times each value occurs.
 3. Find and print the duplicate values in a list of numbers, along with their frequency.



Answers:

1. Calculate the average salary for each department from the table.
Ans.

SELECT Department, AVG(Salary) AS AverageSalary FROM Employees GROUP BY Department;



 2. Write a SQL query to display the employee’s name along with their manager’s name using a self-join on the ‘employees’ table, which contains ‘emp_id’, ‘name’, and ‘manager_id’ columns.
Ans.

SELECT e.name AS EmployeeName, m.name AS ManagerName FROM employees e LEFT JOIN employees m ON e.manager_id = m.emp_id;

Using a LEFT JOIN here ensures that we include all employees in the result, even those who may not have a manager (e.g., a CEO or top-level executive without a reporting manager). In this case, the ManagerName would simply appear as NULL for those employees.
If we used an INNER JOIN instead, it would exclude employees without a manager in the output, which might lead to incomplete results if some employees don’t have a manager_id in the table.
So, to ensure you get a full list of all employees and their managers (including those without a manager), LEFT JOIN is generally more appropriate.




 3. Find the most recent hire for each department (solved using LEAD/LAG functions).
Ans.

WITH RecentHires AS (
    SELECT DepartmentID, EmployeeID, HireDate,
           ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY HireDate DESC) AS rnk
    FROM Emp
)
SELECT * 
FROM RecentHires
WHERE rnk = 1;




 4. Write a query to retrieve the nth highest salary from the Employees table, which has ‘EmployeeID’, ‘Name’, and ‘Salary’ columns.
Ans.

WITH RankedSalaries AS (
    SELECT EmployeeID, Name, Salary,
           ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Rank
    FROM Employees
)
SELECT Salary
FROM RankedSalaries
WHERE Rank = @n; 


 -- Replace @n with the desired rank (e.g., 3 for the 3rd highest salary)



 

1. Create a dictionary, add elements, update a specific entry, and print the dictionary sorted by key in alphabetical order.
Ans.

# Create a dictionary
my_dict = {
    "banana": 2,
    "apple": 5,
    "orange": 3
}

# Add elements
my_dict["mango"] = 4
my_dict["grape"] = 6

# Update a specific entry
my_dict["apple"] = 10  # Update the value for key 'apple'

# Print the dictionary sorted by key in descending order 
# sorted_dict_desc = dict(sorted(my_dict.items(), reverse=True))


# Print the dictionary sorted by key in alphabetical order
sorted_dict = dict(sorted(my_dict.items()))

# Display the sorted dictionary
print(sorted_dict)


o/p

{
    'apple': 10,
    'banana': 2,
    'grape': 6,
    'mango': 4,
    'orange': 3
}



 2. Identify unique values from a list of numbers and print how many times each value occurs.
Ans.

from collections import Counter

# Sample list of numbers
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

# Count the occurrences of each unique number
count = Counter(numbers)

# Print the result
for num, occ in count.items():
    print(f"Value {num} occurs {occ} time(s)")

Output:
Value 1 occurs 1 time(s)
Value 2 occurs 2 time(s)
Value 3 occurs 1 time(s)
Value 4 occurs 3 time(s)
Value 5 occurs 1 time(s)
Value 6 occurs 2 time(s)
Value 7 occurs 1 time(s)




# Another method (using dictionary)
# Sample list of numbers
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

# Create an empty dictionary to store the counts
count_dict = {}

# Count occurrences of each value in the list
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Print the result
for num, occ in count_dict.items():
    print(f"Value {num} occurs {occ} time(s)")


Output:
Value 1 occurs 1 time(s)
Value 2 occurs 2 time(s)
Value 3 occurs 1 time(s)
Value 4 occurs 3 time(s)
Value 5 occurs 1 time(s)
Value 6 occurs 2 time(s)
Value 7 occurs 1 time(s)



 3. Find and print the duplicate values in a list of numbers, along with their frequency.
Ans.

# Sample list of numbers
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

# Create an empty dictionary to store the counts
count_dict = {}

# Count occurrences of each value in the list
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Find and print the duplicates
for num, occ in count_dict.items():
    if occ > 1:
        print(f"Value {num} is duplicated {occ} time(s)")


Output:
Value 2 is duplicated 2 time(s)
Value 4 is duplicated 3 time(s)
Value 6 is duplicated 2 time(s)




-----------------------------------------------------------------------------------------------------------------------------









Mercedes Benz.

Power BI (DAX):

1. Write a DAX measure to find the top 5 products based on product color from two tables: 'Product' (columns: 'product_id', 'product_color') and 'Sales' (columns: 'product_id', 'profit').
2. Explain how to implement Row-Level Security (RLS) in Power BI.
3. Describe different types of filters in Power BI.
4. Explain the difference between 'ALL' and 'ALLSELECTED' in DAX.
5. Write a DAX formula to calculate the rolling 12 months of average sales using a 'sales': table with a 'DATE' column, 'product_id' and 'profit' column.

Python:

1. Create a dictionary, add elements to it, modify an element, and then print the dictionary in alphabetical order of keys.
2. Find unique values in a list of assorted numbers and print the count of how many times each value is repeated.
3. Find and print duplicate values in a list of assorted numbers, along with the number of times each value is repeated.
4. Write a function to add two numbers, take input from the user, and handle possible input errors such as non-numeric input and empty input.

SQL:

1. Write a SQL query to see employee name and manager name using a self-join on 'employees' table with columns 'emp_id', 'name', and 'manager_id'.
2. Explain the order of execution in SQL queries.








Answers:

1. Write a DAX measure to find the top 5 products based on product color from two tables: 'Product' (columns: 'product_id', 'product_color') and 'Sales' (columns: 'product_id', 'profit').
Ans.

SUMMARIZE(
            Sales, 
            Product[product_color], 
            Product[product_id], 
            "TotalProfit", SUM(Sales[profit])
        ), 

TOPN(
        5, 
        SUMMARIZE(
            Sales, 
            Product[product_color], 
            Product[product_id], 
            "TotalProfit", SUM(Sales[profit])
        ), 
        [TotalProfit], DESC
    ),


Top5ProductsByColor = 
CONCATENATEX(
    TOPN(
        5, 
        SUMMARIZE(
            Sales, 
            Product[product_color], 
            Product[product_id], 
            "TotalProfit", SUM(Sales[profit])
        ), 
        [TotalProfit], DESC
    ),
    Product[product_id],
    ", "
)


Explanation:
1.	SUMMARIZE: We summarize the Sales table by product_color and product_id, while calculating the total profit for each combination of product_color and product_id.
2.	TOPN: We use TOPN(5, ...) to retrieve the top 5 products based on the calculated total profit for each product.
3.	CONCATENATEX: This function concatenates the product_id values of the top 5 products (based on the sorted total profit) into a single text string, separated by commas.
Result:
•	The measure will return a comma-separated list of the top 5 product IDs (based on profit) within each product color group.
•	If you want to show the product names or additional details (instead of just the product IDs), you can modify the CONCATENATEX function to display product names or other relevant fields.




5. Write a DAX formula to calculate the rolling 12 months of average sales using a 'sales': table with a 'DATE' column, 'product_id' and 'profit' column.
Ans.


Here’s the DAX measure for the 12-Month Running Sum:


Running12MonthsSum = 
CALCULATE(
    SUM(Sales[profit]),
    DATESINPERIOD(
        Sales[DATE],
        LASTDATE(Sales[DATE]),
        -12,
        MONTH
    )
)


Explanation:
•	DATESINPERIOD: Defines the 12-month period based on the latest date (LASTDATE(Sales[DATE])).
•	SUM(Sales[profit]): Sums the profit over the 12-month period.
•	CALCULATE: Changes the context to calculate the sum over the defined 12-month period.
This will give you the running sum of sales for the last 12 months based on the current date context.



To calculate the Rolling 12-Month Average Sales using DAX, we need to use the CALCULATE function along with DATESINPERIOD and AVERAGEX to calculate the average sales over the past 12 months for each row in the 'sales' table. The rolling average should calculate based on the DATE column.
Here’s how you can write the DAX measure for rolling 12-month average sales:
 
Rolling12MonthsAvgSales = 
CALCULATE(
    AVERAGEX(
        DATESINPERIOD(
            Sales[DATE], 
            LASTDATE(Sales[DATE]), 
            -12, 
            MONTH
        ),
        Sales[profit]
    )
)


Explanation:
1.	DATESINPERIOD: This function is used to define the period of the last 12 months. It takes:
o	The Sales[DATE] column as the date column,
o	LASTDATE(Sales[DATE]) as the reference point for the most recent date in the dataset,
o	-12 to specify the previous 12 months (negative sign indicates the past period),
o	MONTH to define the period as months.
2.	AVERAGEX: This function calculates the average of the Sales[profit] for the dates returned by DATESINPERIOD, which gives the profit for each of the last 12 months.
3.	CALCULATE: This is used to modify the context of the calculation and apply the AVERAGEX to the 12-month rolling period.






-----------------------------------------------------------------------------------------------------------------------------

Cyient

1. Write the DAX to calculate the sales for the last year.
Ans.

Sales Last Year = 
CALCULATE(
    SUM('Sales'[SalesAmount]),
    SAMEPERIODLASTYEAR('Date'[Date])
)
Explanation:
•	SUM('Sales'[SalesAmount]): This calculates the total sales amount from the Sales table.
•	SAMEPERIODLASTYEAR('Date'[Date]): This function shifts the date context to the same period in the previous year, based on the Date table.
•	CALCULATE: Used to modify the context in which the data is evaluated, applying the SAMEPERIODLASTYEAR filter.
Note: Ensure you have a Date table marked as a date table in Power BI, as SAMEPERIODLASTYEAR requires a continuous date range to work correctly.


Sales Last Year = 
CALCULATE(
    SUM('Sales'[SalesAmount]),
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -1, YEAR)
)

Explanation:
•	SUM('Sales'[SalesAmount]): This calculates the total sales amount from the Sales table.
•	DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -1, YEAR): This function creates a date range starting from the last date in the current context and going back 1 year.
•	CALCULATE: Modifies the evaluation context to apply the date range created by DATESINPERIOD.
This approach is useful if you want a rolling last-year calculation that doesn’t strictly follow calendar years, as it allows for more flexible date intervals.





2. Write the DAX to calculate the percentage of each product contributing to the total sales.
Ans.
To calculate the percentage of each product's contribution to total sales, you can use the following DAX formula:
DAX

Product Sales % of Total = 
DIVIDE(
    SUM('Sales'[SalesAmount]),
    CALCULATE(SUM('Sales'[SalesAmount]), ALL('Sales'))
)

Explanation:
•	SUM('Sales'[SalesAmount]): This calculates the total sales amount for each product.
•	CALCULATE(SUM('Sales'[SalesAmount]), ALL('Sales')): The ALL function removes any filters on the Sales table, allowing us to get the total sales across all products.
•	DIVIDE: This function divides the sales for each product by the total sales. Using DIVIDE helps handle any potential division by zero issues.
This measure will return the percentage of each product's sales relative to the total sales.




3. Write the DAX to calculate the percentage changes in sales month over month only for the top 10 based on sales in the last month.
Ans.

To calculate Month-over-Month (MoM) changes in sales, you can use the following DAX formula:
DAX

MoM Sales Change = 
    CALCULATE(
        SUM('Sales'[SalesAmount]),
        DATEADD('Date'[Date], -1, MONTH)
    )

Explanation:
•	SUM('Sales'[SalesAmount]): This calculates the total sales amount for the current context.
•	DATEADD('Date'[Date], -1, MONTH): This shifts the date context back by one month using the Date table. The result will be the sales amount from the previous month.
Calculating the MoM Percentage Change
If you want the percentage change instead of the raw value difference, you can use this formula:
DAX

MoM % Change = 
DIVIDE(
    SUM('Sales'[SalesAmount]) - [MoM Sales Change],
    [MoM Sales Change]
)

Explanation:
•	SUM('Sales'[SalesAmount]) - [MoM Sales Change]: This calculates the difference in sales between the current month and the previous month.
•	DIVIDE(... , [MoM Sales Change]): This divides the difference by the previous month's sales to get the percentage change. DIVIDE handles division by zero, returning a blank result if the previous month’s sales were zero.
These formulas provide both the MoM sales change and the percentage change.

Main answer:

To calculate the Month-over-Month (MoM) percentage change for only the top 10 products based on sales, you can create a measure that filters to include only the top 10 products. Here’s how you can do it in DAX:
DAX


Top 10 Products MoM % Change = 

VAR CurrentMonthSales = 
    CALCULATE(
        SUM('Sales'[SalesAmount]),
        TOPN(10, ALL('Product'), SUM('Sales'[SalesAmount]), DESC)
    )

VAR PreviousMonthSales = 
    CALCULATE(
        SUM('Sales'[SalesAmount]),
        TOPN(10, ALL('Product'), SUM('Sales'[SalesAmount]), DESC),
        DATEADD('Date'[Date], -1, MONTH)
    )

RETURN 


    DIVIDE(
        CurrentMonthSales - PreviousMonthSales,
        PreviousMonthSales
    )


Explanation:
1.	CurrentMonthSales: Calculates the total sales for the current month, but only for the top 10 products.
o	TOPN(10, ALL('Product'), SUM('Sales'[SalesAmount]), DESC): Filters for the top 10 products based on total sales across all time.
o	ALL('Product'): Clears any existing filters on the Product table to ensure we’re calculating the top 10 products based on overall sales.
2.	PreviousMonthSales: Calculates the total sales for the previous month, using the same top 10 products.
o	DATEADD('Date'[Date], -1, MONTH): Shifts the date context back by one month.
3.	DIVIDE(CurrentMonthSales - PreviousMonthSales, PreviousMonthSales): Calculates the MoM percentage change for these top 10 products.
This measure will give the Month-over-Month percentage change specifically for the top 10 products based on their total sales.




-----------------------------------------------------------------------------------------------------------------------------






Confidential

 SQL:
1. How do window functions work in SQL, and when would you use them?
2. What is the purpose of indexing in SQL? How do you decide when to create an index?
3. Can you explain the differences between UNION and UNION ALL?
4. How do you write a SQL query to find the second highest salary in a table?
5. What are CTEs (Common Table Expressions) and their benefits?

 Excel:
1. How do you use the INDEX and MATCH functions together? How does it improve over VLOOKUP?
2. Explain how you can use Excel to forecast future data trends.
3. What is the purpose of Data Validation in Excel, and how would you implement it?
4. How do you use the OFFSET function, and in which scenarios is it most useful?
5. How do you use Excel Solver, and what kind of problems can it help solve?



 Power BI:
1. What are the differences between Power BI Desktop and Power BI Service?
2. How do you optimize data refresh in Power BI for large datasets?
3. Can you explain how to create a dashboard in Power BI, and what are the key components?
4. What is the use of Quick Measures in Power BI, and how do they simplify calculations?
5. How do you use Power Query to merge and append data from multiple sources?

 Python:
1. How would you use Python for exploratory data analysis (EDA)? Provide an example.
2. What is the difference between the merge() and join() functions in pandas?
3. How do you use Python to create data visualizations with libraries like Matplotlib or Seaborn?
4. Explain the use of lambda functions in Python with a practical example.
5. How do you apply regular expressions to clean text data in Python?



Answers:

1. How do window functions work in SQL, and when would you use them?
Ans.
Window functions perform calculations across a set of rows related to the current row while maintaining the individual row context. They are used for tasks like calculating running totals, ranking results, or calculating moving averages, without collapsing the result set. You would use them when you need to perform calculations over a group of rows but still return individual row details.

2. What is the purpose of indexing in SQL? How do you decide when to create an index?
Ans.
Indexing speeds up query performance by allowing the database to quickly locate rows without scanning the entire table. Indexes are typically created on columns that are frequently used in WHERE clauses, JOIN conditions, or sorting (ORDER BY). However, be cautious when creating indexes on large tables with frequent inserts or updates, as indexes can slow down write operations due to the overhead of maintaining them.



4. What is the use of Quick Measures in Power BI, and how do they simplify calculations?
Ans.
Quick Measures in Power BI allow users to create common calculations like averages, year-to-date totals, and running totals without needing to write complex DAX code. They simplify calculations by providing pre-built templates that automatically generate DAX expressions, making it easier for non-technical users to perform complex calculations. This feature is especially useful for those who are not familiar with DAX but still want to create dynamic, data-driven reports.


5. How do you use Power Query to merge and append data from multiple sources?
Ans.
In Power Query, you can merge data by using the Merge Queries option, which combines two tables based on a common column. This works similarly to a SQL join (e.g., inner, left outer). To append data, you use the Append Queries option, which stacks data from multiple tables with the same structure. Merging is useful for combining related data, while appending is ideal for adding rows from different sources into a single dataset. Both actions allow you to clean and transform data seamlessly before loading it into Power BI.




1. How do you use the INDEX and MATCH functions together? How does it improve over VLOOKUP?
Ans.
The INDEX and MATCH functions are often used together as a more flexible alternative to VLOOKUP. INDEX returns the value from a specified row and column in a range, while MATCH finds the position of a value in a row or column. When combined, they allow you to look up a value in any column (not just the leftmost one, like in VLOOKUP).
For example, INDEX(A2:A10, MATCH(B1, B2:B10, 0)) will return the value from column A that corresponds to the value in cell B1, found in column B. This approach is more efficient because it allows for dynamic column selection and doesn’t require the lookup column to be on the left.



2. Explain how you can use Excel to forecast future data trends.
Ans.
Excel provides several tools for forecasting data trends, such as the FORECAST function, Trendlines in charts, and Data Analysis Toolpak. The FORECAST function predicts future values based on historical data by fitting a linear regression model. You can also use Trendlines in scatter or line charts to visually project future trends. For more advanced forecasting, you can enable the Data Analysis Toolpak, which offers tools like Exponential Smoothing and Regression Analysis to forecast based on patterns in the data. These methods help project future trends based on past behavior.



3. What is the purpose of Data Validation in Excel, and how would you implement it?
Ans.
Data Validation in Excel is used to control the type of data entered into a cell, ensuring consistency and accuracy. It helps prevent errors by restricting inputs to certain values, ranges, or formats. To implement it, select the cell or range, go to the Data tab, and click Data Validation. From there, you can set rules such as allowing only whole numbers, dates, or dropdown lists. You can also create custom validation formulas for more specific criteria. This ensures data integrity by enforcing rules at the point of entry.


4. How do you use the OFFSET function, and in which scenarios is it most useful?
Ans.
The OFFSET function in Excel returns a reference to a range that is a specified number of rows and columns from a starting point. It’s often used in dynamic range definitions for charts, reports, or named ranges. For example, OFFSET(A1, 2, 3, 5, 1) will reference a range starting from cell D3, extending 5 rows down and 1 column wide.
It's most useful when creating dynamic ranges that automatically adjust as data grows or changes, such as creating dynamic charts or running totals that adapt to new data without manually updating ranges.



5. How do you use Excel Solver, and what kind of problems can it help solve?
Ans.
Excel Solver is an optimization tool that helps solve complex problems by finding the best solution based on given constraints. It works by adjusting variables to achieve a specific objective, such as maximizing profit or minimizing cost. To use Solver, you need to define:
1.	Objective: The cell that contains the formula you want to optimize.
2.	Variables: The cells that Solver will change to optimize the objective.
3.	Constraints: Conditions that restrict the values of the variables (e.g., limits on resource usage or budget).
Solver can be used for linear programming, resource allocation, supply chain optimization, financial planning, and scheduling problems. It helps find the optimal solution within the defined constraints.




1. How would you use Python for exploratory data analysis (EDA)? Provide an example.
Ans.
Python is widely used for exploratory data analysis (EDA) through libraries like Pandas, Matplotlib, Seaborn, and NumPy. The process typically involves inspecting the dataset, cleaning it, and performing statistical analysis to uncover patterns.
Example:
Python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv')

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualize distributions
sns.histplot(df['column_name'])
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
This process involves loading data, summarizing statistics, visualizing distributions, and checking correlations, which helps in understanding the data before applying models.



2. What is the difference between the merge() and join() functions in pandas?
Ans.
In Pandas, both merge() and join() are used to combine DataFrames, but there are key differences in how they work:
•	merge(): More flexible and similar to SQL joins. It allows merging on one or more columns (or indexes) and supports different types of joins (inner, outer, left, right). You can specify the columns to join on using the on, left_on, and right_on parameters.
Example:
Python

pd.merge(df1, df2, on='key_column', how='inner')
•	join(): Primarily used for joining on indexes (although it can also join on columns). It's simpler for index-based merges but less flexible than merge().
Example:
Python

df1.join(df2, on='key_column', how='left')
In summary, merge() is more versatile and can join on both columns and indexes, while join() is simpler and mainly designed for joining on DataFrame indexes.




3. How do you use Python to create data visualizations with libraries like Matplotlib or Seaborn?
Ans.
To create data visualizations in Python, you can use libraries like Matplotlib and Seaborn, which provide powerful tools for plotting data in various formats such as line charts, histograms, bar plots, and heatmaps.
Example using Matplotlib and Seaborn:
Python

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example dataset
df = pd.read_csv('data.csv')

# Line plot with Matplotlib
plt.plot(df['column1'], df['column2'])
plt.title('Line Plot')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.show()

# Histogram with Seaborn
sns.histplot(df['column_name'], bins=30, kde=True)
plt.title('Distribution of Column')
plt.show()

# Heatmap with Seaborn
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
•	Matplotlib: Used for basic and customizable plots like line charts and scatter plots.
•	Seaborn: Built on Matplotlib and provides higher-level interfaces for making attractive statistical plots, such as histograms, box plots, and heatmaps, with simpler syntax.
These libraries help visualize relationships, distributions, and correlations in data.



4. Explain the use of lambda functions in Python with a practical example.
Ans.
Lambda functions in Python are small, anonymous functions defined with the lambda keyword. They can take any number of arguments but only contain a single expression, which is evaluated and returned. They are useful for short, throwaway functions where you don't want to define a full function with def.
Example:
Python

# Using lambda to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Using lambda with the `map` function to square a list of numbers
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Using lambda with `filter` to filter out even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
Use cases:
•	Map: Apply a function to all items in a list or iterable.
•	Filter: Filter elements in an iterable based on a condition.
•	Sort: Sort data based on custom sorting logic.
Lambda functions are great for simple, one-liner operations in functions like map(), filter(), or sorted().



5. How do you apply regular expressions to clean text data in Python?
Ans.
Regular expressions (regex) in Python, using the re module, are powerful tools for cleaning and manipulating text data. They allow you to search for specific patterns and modify or extract parts of the text.
Example of using regex to clean text data:
Python

import re

# Sample text data
text = "The price of the item is $100. The sale ends on 12/15/2024."

# Remove dollar sign and digits
cleaned_text = re.sub(r'\$\d+', '', text)
print(cleaned_text)  # Output: "The price of the item is . The sale ends on 12/15/2024."

# Remove all non-alphanumeric characters (except spaces)
cleaned_text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
print(cleaned_text)  # Output: "The price of the item is 100 The sale ends on 12152024"

# Extract all date patterns
dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
print(dates)  # Output: ['12/15/2024']
Key operations:
•	re.sub(pattern, replacement, string): Replace text matching a pattern.
•	re.findall(pattern, string): Extract all occurrences of a pattern.
•	re.match(pattern, string): Match the pattern at the start of the string.
Regular expressions are useful for tasks like:
•	Removing unwanted characters or symbols.
•	Extracting specific patterns like emails, dates, or phone numbers.
•	Standardizing formats in messy text data.









-----------------------------------------------------------------------------------------------------------------------------

Myntra Data Analyst Interview Experience (1-3 years):


Round 1 Elimination Resume Grilling + SQL:

1️⃣ 2-3 SQL Question, around self join , usage of Ranking functions and one case specific question around Lead/lag window function
2️⃣ Myntra wants to improve its data quality by identifying duplicate or similar product listings in their inventory. Due to slight variations in product titles (such as spelling differences, abbreviations, or extra spaces), some products might appear more than once in the inventory. You are tasked with identifying pairs of products that are likely duplicates based on their titles, using fuzzy matching.

Round 2 Case Study 

1️⃣ A basic guess estimate question, Estimate the number of Uber Cars are there in Bengaluru? 
2️⃣ Myntra, wants to solve the issue pertaining to fraudulent customer behavior, list down all the metrics and provide some actionable on solving this issue

⏩This round also had resume grilling

Round 3 (Hiring Manager):

1️⃣Resume Grilling around the projects being mentioned on resume.

2️⃣Behavioral questions and whether you would be the right fit at Myntra 

Round 4 HR Discussion

1️⃣ Discussion around salary, joining date and what culAmazon Data Analyst Interview Experience(1-3 Years):



SQL:

1- Find the second-highest salary in a department. You may need to use the ROW_NUMBER() or DENSE_RANK() function to solve this.

2- Write a SQL query to return the total number of transactions per user for each day. This could involve using GROUP BY and COUNT() functions. This is common in data aggregation tasks.

3- Create a query that selects projects with the highest budget-per-employee ratio from two related tables (projects and employees). This tests your ability to handle complex joins and aggregations.

Power BI:

1-Explain the difference between Import and Direct Query modes. Which would you choose when working with large datasets? (Direct Query offers real-time data but can be slower, while Import is faster but may become outdated).

2- What are slicers, and how do they differ from visual-level filters? Discuss how each affects the data on the Power BI dashboard.

3-How do you implement Row-Level Security (RLS) in Power BI? Explain how you would restrict data access to specific users or groups.

4-What is a paginated report, and when would you use it? It’s especially useful for creating reports that span multiple pages, such as invoices or billing statements.

Python:

1- Write a Python script to identify unique values in a list and count their occurrences. This tests your understanding of basic Python data structures like sets and dictionaries.

2- How would you use pandas to merge two datasets and calculate the total sales for products with valid promotions? This requires fluency with merge(), groupby(), and basic data analysis functions.

3- Explain the difference between lists, tuples, sets, and dictionaries in Python. Each has different use cases in data manipulation and analysis.ture to expect at Myntra.


-----------------------------------------------------------------------------------------------------------------------------

Uber Business Analyst Interview Experience (1-3 years):


SQL Questions:

1. Write an SQL query to extract the third transaction of every user, displaying user ID, spend, and transaction date.
 
2. Calculate the average ratings for each driver across different cities using data from rides and ratings tables.

3. Create an SQL query to identify customers registered with Gmail addresses from the 'users' database.

4. What does database denormalization mean?

5. Analyze the click-through conversion rates using data from ad_clicks and cab_bookings tables.

6. Define a self-join and provide a scenario for its application.

Scenario-Based Question:

1. What is the probability that at least two of three recommended routes for drivers are the fastest, given a 70% success rate?

Guesstimate Questions:

1. Estimate the number of Uber drivers in Delhi.
2. How many Uber cabs leave Bengaluru Airport in a day?


-----------------------------------------------------------------------------------------------------------------------------

Deloitte Recent Interview Insights for a Data Analyst Position(0-3 Years):



 1. Tell us about yourself and your current job responsibilities.
 2. Can you share some challenges you encountered in your recent project involving Power BI dashboards, and how did you resolve them?
 3. What distinguishes a KPI (Key Performance Indicator) from a dimension?
 4. Write a SQL query to find the third highest salary from an employee table with the following columns: EID, ESalary.
 5. Create a SQL procedure using ESalary as a parameter that selects all EIDs from the Employee table where ESalary is less than 50,000.
 6. For the Employee table (with columns EID and ESalary), retrieve all EIDs with odd salaries and join this with another table, empdetails (with columns EID and EDOB), to obtain EDOB.
 7. How would you use the LEAD or LAG function in SQL to compare week-over-week data?
 8. Can you explain how you would create a DAX measure in Power BI to calculate the year-over-year growth for a specific metric?
 9. Identify a unique chart type in Power BI that differs from standard charts and explain its purpose.
 10. Describe how you would implement a time intelligence feature in Power BI to analyze sales trends over different time periods.

-----------------------------------------------------------------------------------------------------------------------------

Tiger Analytics Data Analyst Interview Experience (0-3 years)



SQL Questions:

 1. Describe a scenario where you used SQL to analyze customer data. What insights did you uncover?
 2. Rate your SQL skills on a scale of 1-10 and provide examples of advanced queries you’ve written.
 3. Write a query to identify the second-highest salary in each department.
 4. Explain the concept of JOINs and provide a query that joins three tables (Orders, Customers, Products) to find the top 5 customers by revenue.
 5. What is a Common Table Expression (CTE) in SQL, and when would you use it? Write a CTE query to calculate cumulative monthly sales.
 6. Write an SQL query to find all employees whose salaries are above the department average.
 7. Describe your approach to optimizing SQL queries. Can you share an example where optimization made a noticeable difference?

Python Questions:

 1. What Python libraries do you frequently use for data manipulation, and why?
 2. How would you write a Python function to calculate moving averages for sales data?
 3. Write a Pandas code snippet to remove outliers from a dataset based on the IQR method.
 4. Describe a project where you used Matplotlib or Seaborn for data visualization. What insights did your visualizations reveal?
 5. How would you merge three DataFrames (Sales, Customers, Regions) and compute the average sales per region?
 6. Write a Python code snippet to group data by product category and calculate total revenue for each category.
 7. How do you handle missing data in Python? Share a few imputation techniques you use.
 8. Explain how you would use time series analysis in Python for forecasting monthly sales.


-----------------------------------------------------------------------------------------------------------------------------


KPMG Data Analyst Interview Experience at (2+ Years)


SQL:

 1. Write a query to calculate the total revenue generated by each region.
 2. Display the names of employees who have a salary above the average salary in their department.
 3. Identify the second highest salary in each department from the ‘employees’ table, which has ‘emp_id’, ‘department_id’, and ‘salary’ columns.
 4. Write a SQL query to find employees who have not had any recent sales in the last 3 months.

Power BI:

 1. Explain how you would create a dynamic date filter in Power BI for last month’s data.
 2. Describe the steps for setting up role-based access in Power BI using Row-Level Security (RLS).
 3. What is the difference between a calculated column and a measure in Power BI?
 4. How would you approach building a KPI dashboard that tracks multiple metrics over time?

Python:

 1. Write a Python function to filter out customers who have made more than 5 purchases in the last 6 months.
 2. Create a program that reads a CSV file, extracts unique values in a column, and saves the results in a new file.
 3. Develop a Python script to visualize monthly sales trends for a dataset using Matplotlib or Seaborn.

Case Study Round (Guesstimate Focus):
In addition to technical questions, there was a guesstimate question to test analytical thinking.

— Estimate the number of coffee cups sold in New York City daily.

-----------------------------------------------------------------------------------------------------------------------------

Flipkart 

SQL Questions:

 1. What are window functions, and how do they differ from aggregate functions? Can you give a use case?
 2. Explain indexing. When would an index potentially reduce performance, and how would you approach indexing strategy for a large dataset?
 3. Write a query to retrieve customers who have made purchases in the last 30 days but did not purchase anything in the previous 30 days.
 4. Given a table of transactions, find the top 3 most purchased products for each category.
 5. How would you identify duplicate records in a large dataset, and how would you remove only the duplicates, retaining the first occurrence?

Guesstimates:

 1. Estimate the number of online food delivery orders in a large metropolitan city over a month.
 2. How many customer service calls would a telecom company receive daily for a customer base of 1 million?

Case Studies:

 1. A sudden decrease in conversion rate is observed in a popular product category. How would you investigate the cause and propose solutions?
 2. Imagine the company is considering adding a new subscription model. How would you evaluate its potential impact on customer lifetime value and revenue?

Managerial Questions:

 1. Describe a time when you faced conflicting priorities on a project. How did you manage your workload to meet deadlines?
 2. How would you handle a disagreement within the team on an analytical approach?

Python Questions:

 1. Write a Python function to find the longest consecutive sequence of unique numbers in a list.
 2. If you’re working with a large dataset with missing values, what Python libraries would you use to handle missing data, and why?




-----------------------------------------------------------------------------------------------------------------------------

Myntra Data Analyst Interview Experience (1-3 years):


Round 1 Elimination Resume Grilling + SQL:

1️⃣ 2-3 SQL Question, around self join , usage of Ranking functions and one case specific question around Lead/lag window function
2️⃣ Myntra wants to improve its data quality by identifying duplicate or similar product listings in their inventory. Due to slight variations in product titles (such as spelling differences, abbreviations, or extra spaces), some products might appear more than once in the inventory. You are tasked with identifying pairs of products that are likely duplicates based on their titles, using fuzzy matching.

Round 2 Case Study 

1️⃣ A basic guess estimate question, Estimate the number of Uber Cars are there in Bengaluru? 
2️⃣ Myntra, wants to solve the issue pertaining to fraudulent customer behavior, list down all the metrics and provide some actionable on solving this issue

⏩This round also had resume grilling

Round 3 (Hiring Manager):

1️⃣Resume Grilling around the projects being mentioned on resume.

2️⃣Behavioral questions and whether you would be the right fit at Myntra 

Round 4 HR Discussion

1️⃣ Discussion around salary, joining date and what culture to expect at Myntra.



















Confidential 

(Tricky and Advanced)

SQL

1. Scenario: Query Optimization

You have a slow-running query that joins three large tables. How would you go about optimizing this query to improve its performance?

Hint: Consider factors like indexing, query structure, and execution plans.

2. Scenario: Data Cleaning in SQL

How would you handle a dataset where there are duplicate records based on multiple columns? Write a SQL query to remove duplicates while keeping the

most recent record. Hint: Use ROW NUMBER () with PARTITION BY and filtering

3. Practical Task Aggregating Data for Reporting

Write a SQL query to calculate the monthly revenue growth for a retail business using sales data.

Excel:

1. Scenario: Dynamic Data Reporting
How would you create a dynamic dashboard in Excel that automatically updates when new data is added?
Hint: Use dynamic named ranges and data tables.

2. Practical Task Financial Forecasting
Using Excel's built in forecasting tools, predict the sales for the next six months using historical sales data. How would you evaluate the accuracy of your forecast?

3. Scenario: Data Transformation

How would you normalize a large dataset in Excel. ensuing that all values are scaled between 0 and 1?
Hint: Use formulas to calculate normalized values

Power BI:

1. Scenario: Large Dataset Performance
How would you manage and optimize Power Bl reports that use large datasets (millions of rows), ensuring that the reports nun efficiently and refresh quickly?
Hint: Consider techniques like data aggregation, Direct Query, and incremental refresh

2. Practical Task Custom Visuals
How would you create a custom Power BI visual to display a complex KPI metric that isn't supported by default visuals?

3. Scenario: Row-Level Security
How would you implement row-level security (PLS) in Power Bl to restrict date access based on user roles?

Python
1. Scenario: Automating Data Cleaning
How would you write a Python script that automatically detects and replaces outliers in a dataset using the IDR method?

2. Practical Task Advanced EDA
Using pandas, matplotlib, and seaborn, perform an  EDA on a dataset with missing values, outliers, and skewed distributions. Summarize your findings with appropriate visualizations

3. Scenario. Efficient Data Merging
You have two large datasets that need to be merged based on multiple columns. How would you optimize the merge() function in pendas to handle this efficiently?

-----------------------------------------------------------------------------------------------------------------------------



"""