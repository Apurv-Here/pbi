""""

---------------------------------------------------------------------------------------------------------------------


1. EPAM

2. KPMG

3. EY

4. Mindtree



---------------------------------------------------------------------------------------------------------------------



Minds YT:

---------------------------------------------------------------------------------------------------------------------


1. EPAM


R1 (INV - 0007)


- Data sources used.

- What is dual mode.

- Whole general process -> from requirement gathering till end.

- RLS -> Give example.

- OLS and how to implement it.

- SCD and its types.

- How to optimize the report.

- How to optimize DAX with DAX studio.

- Many to many relationships and how to solve them.

- DAX to male the bridge table. (Use summarize and distinct)

- Incremental refresh.

- copilot with power bi.

- power bi template file.

- percent of sales by category -> DAX.

- 3rd max salary.

- what is dataflow.

- what is microsoft fabric and its integration and all.

- onelake in fabric.





R2 (INV - 0008)


- day to day work.

- what is CI CD & related to power bi.

- what is version control.

- OLAP vs OLTP.

- data warehouse vs data lake vs data mart.

- what is database normalization.

- star schema.

- SCD and its types.

- factless vs fact table.

- types of pbi license and explain them.

- RLS and its types, and how it is different from OLS.

- optimize dax.

- role playing dimesnion and its example.

- bidirectional cross filtering  & example when it is useful.

- what is semantic model.

- guidelines for report creation.

- how to deal with irregular data.

- forecast line chart based on last 3 months data.

- DDL vs DML.

- types of window function.

- union vs union all vs except.

- how do you perform sql query optimization.

- what are indexes.

- clusterd vs non clustered index.

- PBI -> calculate the average of total sales amount over a 7 day period.

- 
i/p table
 
 ______________________________
| dep_id | recruitment_count  |
|--------|--------------------|
|   1    |        10          |
|   2    |        20          |
|   3    |        30          |
|______________________________|



o/p table

 ______________________________
| dep_id | recruitment_count  | percent_of_recruitment_count |
|--------|--------------------|-----------------------------|
|   1    |        10          |           16.67%           |
|   2    |        20          |           33.33%           |
|   3    |        30          |           50.00%           |
|______________________________|



DAX:

Percent_of_Recruitment_Count =
VAR Total_Recruitment = CALCULATE(SUM(Table[recruitment_count]), ALL(Table))
VAR Department_Recruitment = SUM(Table[recruitment_count])
RETURN
    DIVIDE(Department_Recruitment, Total_Recruitment)

    

Calculation Breakdown
---------------------
Total Recruitment Count:
10 + 20 + 30 = 60

Department 1:
(10 / 60) * 100 = 16.67%

Department 2:
(20 / 60) * 100 = 33.33%

Department 3:
(30 / 60) * 100 = 50.00%






R3 (INV - 0009)


- reason for sudden change.

- current month sales & previous month sales.

- month sales percent change.

- fabric in power bi.

- what is uses matrix.

- how to get uses matrix for all these reports which is present in that workspace in a single uses matrix report.

- Q&A feature in power bi.

- new updates in power bi.


Answers:

- what is uses matrix.

- how to get uses matrix for all these reports which is present in that workspace in a single uses matrix report.





1. What is Usage Matrix in relation to Power BI?
A Usage Matrix in Power BI refers to a report that tracks and displays the usage statistics of reports, dashboards, and datasets within the Power BI workspace. It shows important details like:

Who is accessing the reports.
Frequency of usage.
Interactions with visualizations.
User-level engagement metrics.
This type of report helps administrators and report owners understand how their Power BI content is being utilized across the organization, helping them optimize reports, troubleshoot issues, and track user activity.




2. How to Get Usage Matrix for All Reports in a Workspace in a Single Usage Matrix Report?


Summary:

By combining the Power BI Activity API or Usage Metrics and creating a Matrix Visual in Power BI, you can aggregate usage data for all reports in a workspace into a single consolidated Usage Matrix report. This helps you efficiently monitor report usage across your organization.



To create a Usage Matrix report that aggregates usage data for all reports in a specific workspace, follow these steps:

Step 1: Enable Audit Logs (Power BI Admin)
Step 2: Use Power BI Activity API
Step 3: Use Power BI Service Usage Metrics




Step 1: Enable Audit Logs (Power BI Admin)
You must have Power BI Admin or Global Admin permissions to access audit logs. These logs contain user activity data.

Go to the Power BI Admin Portal.
Under Audit Logs, enable logging to track usage of reports, dashboards, and datasets.


Step 2: Use Power BI Activity API

Power BI provides an Activity API to retrieve detailed usage data across reports and workspaces. This can be used to track who is accessing reports, their interactions, and other relevant activities.

Steps:

Query the Power BI REST API to retrieve activity data across workspaces.
You’ll need an Azure Active Directory (AAD) application with the necessary permissions to access this API.
Use the Get Activity Reports function to retrieve report usage metrics.


Step 3: Use Power BI Service Usage Metrics

You can use Power BI Service Usage Metrics to track usage for individual reports, dashboards, and workspaces:

In Power BI Service, go to the workspace containing the reports.
Click on the Usage Metrics tab for individual reports (under Settings for each report).
For a consolidated usage report, export the usage data for each report and merge them into one dataset in Power BI.
Step 4: Create a Usage Matrix Report
Once you have the usage data, you can create a Usage Matrix report:

Load the usage data into Power BI (either by pulling from the API or importing exported files).
Design the report:
Use Matrix Visuals to display user activity metrics like views, interactions, and frequency.
Organize the data by user (rows) and report or workspace (columns).
You can enhance this report by adding filters for dates, users, or reports to allow deeper analysis.






---------------------------------------------------------------------------------------------------------------------


2. KPMG


R1 (INV - 0021)

- what is a stored procedures.

- how to handle exceptions in stored procedure, error exception.

- sql data type for multi language.

- max length for nchar and var.

- what is block data type.

- table & temp table difference.

- what is table variable.

- types of different temp tables.

- situational example for global & temp tables.

- functions in sql.

- user defined function in sql and give example.

- triggers and its types and give example.

- different types of joins.

- query to find duplicates, two methods.

- 10th highest salary.

- views in sql.

- views vs materialized view.

- table vs view.

- we have a stored procedure of 1000 of lines, execution time is 10 mins. Factors for performance improvement.

- how many reports have you developed so far.

- limitations of direct query.

- what is dataflow and how to create it.

- what is data mart.

- measures vs calculated columns.

- hierarchical relationships in dax and report. 

- summarize vs sumarizecolumns in dax.

- what is query folding.

- sum vs sumx.

- concatenatex dax function.

- 12 months rolling data dax.

- what are the exact options available when you go to update the bookmarks.

Summary:
When updating a bookmark, you can control the following:

Data (filter selections and slicer states),
Display (visibility of visuals),
Current Page (page where the bookmark was created),
Selected Visuals (specific visuals' states).
These options allow you to have a high level of control over how the bookmark behaves when activated.



How to Update a Bookmark:
Go to the View tab in Power BI Desktop.
In the Bookmarks pane, right-click on an existing bookmark.
Select Update from the context menu.
The Update Bookmark dialog will appear, allowing you to choose which of the above options to include in the update.


- different transformations used in your report.

- combine two string columns.

- how do you clean the data.

- how are you sharing your reports.

- I don't want to use schedule refresh, still how to refresh the report, remove manual as well.

If you want to avoid scheduled and manual refresh:

Use DirectQuery or Live Connection to query the data in real time.
Consider using Push Data through the Power BI API or Azure Stream Analytics for real-time updates.



---------------------------------------------------------------------------------------------------------------------


3. EY


R1 (INV - 0018)

- types of data sources used.

- issues faced while using multiple data sources.

- how to handle performance.

- how to do schedule refresh for excel & sql, exact steps.

- when you publish your report, how many files you get (2 or 3) & what are those name them.
(3 files -> report, model (dataset) & dashboard)

- So, in these 3 which you configure for schedule refresh. (model)

- types of gateways.

- many to many relationship.

- what is USERELATIONSHIP() and give example.

- row context vs filter context.

- RLS and its types.

- top 2nd customer based on sales amount, dax code.

Top 2nd Customer Sales = 
VAR RankedCustomers = 
    ADDCOLUMNS(
        SUMMARIZE(Sales, Sales[CustomerID], "TotalSales", SUM(Sales[Amount])),
        "Rank", RANKX(ALL(Sales[CustomerID]), SUM(Sales[Amount]), , DESC)
    )
VAR SecondTopCustomer =
    FILTER(RankedCustomers, [Rank] = 2)
RETURN
    CALCULATE(
        MAXX(SecondTopCustomer, [TotalSales])
    )




---------------------------------------------------------------------------------------------------------------------


4. LTIMindtree


R1 (INV - 00)


-


---------------------------------------------------------------------------------------------------------------------



---------------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------------




"""