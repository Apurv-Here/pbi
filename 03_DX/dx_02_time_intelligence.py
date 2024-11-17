""""

_____________________________________________________________________________

02 DAX
_____________________________________________________________________________

TotalSales = SUM(balances[Amount])

For writing Current MTD, QTD and YTD we will use TOTALMTD, but for other time intelligence DAX like Previous month and MoM or SAMEPERIODLASTYEAR, we will start with CALCULATE function and 
While writing time intelligence DAX, be very careful for suppose month to date will be TOTALMTD and DATESMTD, 
If you change to QTD, the TOTALQTD and DATESQTD. Everything will be changed.
If you change to YTD, the TOTALYTD and DATESYTD. Everything will be changed.


Current MTD = TOTALMTD([TotalSales],DATESMTD(balances[Dates]))

Current QTD = TOTALQTD([TotalSales],DATESQTD(balances[Dates]))

Current YTD = TOTALYTD([TotalSales],DATESYTD(balances[Dates]))



To use same period calculations, first you have to create normal MTD, QTD or YTD.

To calculate MoM we use Current MTD with SAMEPERIODLASTYEAR
SPLY MTD = CALCULATE([Current MTD],SAMEPERIODLASTYEAR(balances[Dates]))


To calculate QoQ we use Current QTD with SAMEPERIODLASTYEAR
SPLY QTD = CALCULATE([Current QTD],SAMEPERIODLASTYEAR(balances[Dates]))


To calculate YoY we use Current YTD with SAMEPERIODLASTYEAR
SPLY YTD = CALCULATE([Current YTD],SAMEPERIODLASTYEAR(balances[Dates]))



Note: It is using PREVIOUSMONTH, PREVIOUSQUARTER, PREVIOUSYEAR and DATESMTD, DATESQTD and DATESYTD both, whereas in the SAMEPERIODLASTYEAR , it onlt used current mtd and sameperiodlasytear(Dates[Date])

Previous MTD = CALCULATE([TotalSales],PREVIOUSMONTH(DATESMTD(balances[Dates])))

Previous QTD = CALCULATE([TotalSales],PREVIOUSQUARTER(DATESQTD(balances[Dates])))

Previous YTD = CALCULATE([TotalSales],PREVIOUSYEAR(DATESYTD(balances[Dates])))








"""