



"""


Difference between date/time and time intelligence dax functions. 🤝🤝

Date/Time DAX functions and Time Intelligence DAX functions are both used to manipulate and analyze date and time data in Power BI, but they serve different purposes:

Date/Time DAX functions: ✌️✌️

- Used to perform basic date and time operations like extracting year, month, day, hour, minute, second, etc.
- Examples:
 1. YEAR() ✅
 2. MONTH() ✅
 3. DAY() ✅

Time Intelligence DAX functions: ✌️✌️

- Used to perform time-related calculations like year-to-date, quarter-to-date, moving averages, etc.
- Examples:
 1. TOTALYTD() ✅
 2. TOTALQTD() ✅
 3. MOVINGAVERAGE() ✅

Some other examples of Time Intelligence DAX functions include:

DATEADD(), DATESBETWEEN(), DATESINPERIOD(), TOTALMTD() (Month-To-Date)

Date/Time DAX functions are more focused on basic date and time operations, whereas Time Intelligence DAX functions are more focused on advanced time-related calculations.



Tell me writing order & exceution order of sql: 🙌🙌

Writing Order: 👇🖌

Select ✅
From ✅
Join ✅
Where ✅
Group by ✅
Having ✅
Order by ✅
Limit ✅

Exceution Order 👇🖌

From ✅
Join ✅
Where ✅
Group by ✅
Having ✅
Select ✅
Distinct ✅
Order by ✅
Limit ✅




For BI reports to generate properly with AI features in Service & Copilot with Fabric, What are Pre Requisites? 🤔🤔🤔

1) Relationships must be Perfect ✅️
2) Measures should be written with perfect formula ✅️
3) Naming convention of Measures & column must be Perfect ✅️
4) Hierarchies must be Perfectly defined ✅️
5) Data Types must be Perfect ✅️
6) Direction of Relationships must be Perfect ✅️
7) Maintain standardize values in column eg: Status column should have properly "Open", "Closed" & "Pending" ✅️
8) Data Dictionary Table must be perfect and will helped alott ✅️
9) Standard KPIs will helped alott ✅️
10) Refresh Schedules must be perfectly defined ✅️


Important Point related to Performance Testing of BI Reports: ✌️✌️

1) Whenever we are checking loading time of BI reports just don't check on one Brower. Check on all Chrome, Mozilla, Edge e.t.c Browers ✅️
2) Don't just check with one user at time, check with 4-5 concurrent users at a time ✅️
3) Just don't check at Morning or Evening, but check whole day at every 2 hours of Intervals ✅️
4) Document that into excel with time of readings, time took to load, Name of person and upload at one drive ✅️
5) Report Loading time must be less than 3-4 sec for 1 user and around 10 sec for 5 concurrent users ✅️


Which data source connection can give good performance of Power BI Report when it comes to very large datasets ???

1) View from SQL /ADB
2) Dataflow in Power BI Service 
3) Lake House via Microsoft Fabric

Answer: Lake House via Microsoft Fabric potentially offers the best performance, especially for large-scale data and complex analytics scenarios. ✅️
Connecting to Lake House via Microsoft Fabric can provide excellent performance, as the data is stored in a columnar storage format that is optimized for analytics. ✅️
Additionally, Lake House supports advanced data processing and caching capabilities, making it an attractive option for large-scale analytics workloads.✅️
Optimized for performance in handling both structured and unstructured data. ✅️


What is difference between Report layout and Report themes in BI Reports?

Report Layout: ✌️✌️

- Refers to the arrangement of visual elements, such as charts, tables, and text, on a report page. ✅️
- Defines the structure and organization of the report content. ✅️
- Determines the placement and size of report elements, like headers, footers, and margins.✅️
- Can be customized to create a specific look and feel.✅️

Report Themes:✌️✌️

- Refers to a pre-defined set of visual styles, such as colors, fonts, and shapes, that can be applied to a report.✅️
- Controls the visual appearance of report elements, like charts, tables, and text.✅️
- Can include settings for colors, fonts, backgrounds, and other visual attributes.✅️
- Can be used to maintain consistency across multiple reports or to match company branding.✅️


How would you optimize a Power BI report that contains several visuals (charts, graphs, etc.) for performance while ensuring the report remains user-friendly and informative? ⬆️⬆️

1) Reducing the number of visuals: Consolidating multiple visuals into fewer ones or combining data into matrix or summary views. ✅

2) Using bookmarks/page navigation: To reduce the number of visible visuals on one page but allow users to switch between views. ✅

3) Efficient DAX: Writing optimized DAX queries that minimize computation time. ✅

4) Using aggregations: When working with large datasets, pre-aggregating data can significantly improve performance. ✅

5) Data model optimization: Using star schemas and avoiding bi-directional relationships where unnecessary. ✅

6) Limiting data points: Filtering visuals to show fewer data points or using custom tooltips instead of displaying all data at once. ✅

7) Minimizing cross-filtering: Limiting interactions between visuals to prevent heavy processing loads. ✅



How to reduced time while Dev to Prod PBIX Migration? 🏆

1) Add calculated columns at Power Query End ✅
2) Add Conditional Columns at Power Query End ✅
3) Data Types, Data Formatting changes at Power Query ✅
4) Concenatation at Power Query ✅
5) Grouping at Power Query rather than summarize at Power BI Desktop ✅
6) Manual Table at Power Query ✅
7) Create Index Column at Power Query ✅
8) Do Mapping Transformations at Power Query ✅


Data Visualization Best Practices in Power BI ✌️✌️✌️

1) Less No. of pages in Report ✅
2) Limit No. Of Visuals on single page ✅
3) Use of Bookmarks / Page Navigation / Drill Through /Toogle Button where ever needed ✅ 
4) Use of Custom Visuals if really required or ignored it ✅
5) Monitor with Performance Analyzer which visual taking more time to load ✅
6) Use of Conditional Formatting is good ✅
7) Right choice of Visuals ✅
8) Must be Story Telling ✅
9) Most Underrated is Labelling ✅
10) Use option Page fit to width & Canvas Settings





Questions asked by Power BI Developers to Client at the Start of the Projects: ✌️

1) Are we going to get Sample reports/Mock Reports from you? ✅️
2) What access we will get at Power BI Service side?✅️
3) Are we getting all credentials and access before sprint 0 I.e before Projects starts✅️
4) Are we going to get Proper Workshop / KT✅️
5) Data Volume Table, Rows ?✅️
6) What will be data source ? Data Engineering at your end or ours? ✅️
7) What is Connectivity Mode ?✅️
8) Are we open to use Microsoft Certified Custom Visuals?✅️
9) Production of PBI reports will be taken care by Developers or your team✅️
10) Does Project include reports from scratch development, or enhancement or Migration work✅️
11) What will be data refresh frequency once moved to Production? ✅️
12) Target Audience, No of users using reports at Production side? ✅️
13) Calculations will be from backend or most of Part at PBI end? ✅️
14) Are we going to get any manual files afterwards, apart from exisiting data model✅️
15) We will get access to whole data base including at Landing & Source ? ✅️
16) Are we going to go with Microsoft Fabric ?



Accenture

1. Write a SQL query to fetch the top 10% of employees based on salary. ✅
2. How would you optimize a slow-performing SQL query? ✅
3. What's the difference between INNER JOIN and LEFT JOIN? ✅
4. Write a SQL query to find the second-highest salary in a table. ✅
5. How would you handle NULL values in a SQL query? ✅
6. What's the difference between UNION and UNION ALL? When would you use each? ✅
7. Write a SQL query to find the number of employees in each department. ✅
8. How would you implement data normalization in a database? ✅
9. Write a SQL query to find the highest-selling product in each category. ✅
10. How to Build a View & Stored Procedure ✅


Accenture

L1:

1. Can you explain the difference between Power BI and Power BI Premium? ✅
2. How do you optimize Power BI report performance? ✅
3. What is the difference between a calculated column and a measure in Power BI? ✅
4. How do you handle data modeling in Power BI? ✅
5. Can you explain the concept of data governance in Power BI? ✅
6. How do you implement row-level security (RLS) in Power BI? ✅
7. What are the different types of Power BI visuals and when would you use each? ✅
8. Can you walk me through your process for creating a Power BI dashboard? ✅
9. How do you troubleshoot common Power BI issues? ✅
10. Can you explain the concept of data storytelling in Power BI and how you would approach it? ✅



 L2:

Your PBIX File is not getting published, What are reasons?

1) You have Pro Account and your PBIx has crossed 1 GB ✅
2) 1 file with same name open two times in Power BI Desktop ✅
3) Internet Issues ✅
4) Don't have permission of Workspace ✅
5) Outdated Version of PBI Desktop ✅
6) Refresh going at Backend and data is too Huge in case of Direct Query ✅
7) If your account is deactivated or restricted ✅
8) Heavy Cookies & Caches in PBI Desktop ✅


How to optimize Power BI Report Performance wise: 

1) Check Performance Analyzer in built feature of Power BI ✅
2) Check Report Embedded link opening time on Chrome, Edge & Mozilla loading speed time and use screen record to show to clients ✅ 
3) Use tools like Page Speed Insights & J Meter ✅
4) Run all heavy query at Azure Data Lake and at that point check in how much time our report takes to load ✅
5) Check with 10-12 concurrent users at a time ✅
6) Check at 9 am, 12 pm, 3 pm & 6 pm properly because sometimes at single time there can be many users ✅
7) If Direct Query or Live Connection then Check How much time your PBIX file is taking to open in Power BI Desktop ✅
8) Use Brunner BI tool ✅
9) After scheduled refresh when new data is added also check in 5 min now how much time it is taking to load ✅
10) Always check switching between bookmarks what time it is taking ✅


















































































"""












































































