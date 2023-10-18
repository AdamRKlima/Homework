# Excel Class Examples and Activities

We will use the following spreadsheet in the activities folder to learn more about Excel ... `Excel_Practice_Student.xlsx`

> **NOTE**: This spreadsheet has 5 tabs at the bottom of the screen, and the data is wide so scroll to the right to see all the content on each sheet.

<br>

## 0. Upload Excel file to OneDrive (optional)
If using Microsoft Office Online, you'll need to complete the following in order to view the spreadsheets:
1. Login to your account
2. Access Excel online
3. Click `Upload` and select the `Excel_Practice_Student.xlsx` file

NOTE: this steps must be repeated for the different spreadsheets we'll be working with.

<br>

## 1. Excel Table Example – Payroll

Open a new spreadsheet (or add a new tab) and name/save it as ‘Payroll’

- Add title of “employee payroll” in A1
- Add 'Last Name' in cell A3
- Add ‘First Name’ in B3
- Add ‘Hourly Wage’ in c3
- Add ‘Hours Worked’ in d3
- Add ‘Pay’ in e3
- Add today’s date in d1
- Add the following names in cells A4 – A14:
  - Walker, Bell, Rogers, Hill, Abbott, Young, Hail, Miller, Little, Munnson, Taylor
- Add the following names in cells b4 – b14:
  - Lindsay, Gary, Phillip, Bill, Bryan, Tammy, Aaron, Christina, Matthew, Cary, Milton
- Add the following numbers in cells c4-c14:
  - 10, 15, 3.5, 20.1, 5.75, 12, 6.55, 30, 75, 40, 25
- Add the following numbers in cells d4 – d14:
  - 40, 35, 30, 50, 55, 45, 25, 29, 32, 44, 22
- Put ‘MAX’ in A16
- Put ‘MIN’ in A17
- Put ‘AVG’ in A18
- Put ‘TOTAL’ in A19

<br>

### **Next Steps -- Format the table**

1. Adjust the cells to read all text
2. Format hourly wage in dollars and decimals
3. Calculate the Pay column ensuring overtime hours are not included. *Formula Hint =IF(D4<=40, C4*D4, 40*C4)*
4. Put your name in C1
5. INSERT Column to right of Pay (f3) and label it “Overtime Hours”
6. Calculate overtime hours
7. IF STATEMENT for f4 `=if(d4>40,d4-40,0)`
8. Add ‘Overtime Bonus’ in G3
9. Calculate overtime `= 1.5*f4*c4`
10. Add ‘Total’ to H3
11. Calculate Total
12. Calculate MAX
13. Calculate MIN
14. Calculate AVG
15. Calculate TOTAL

<br>

---

<br>

## 2. **Excel Chart Example – Loans**

Do the following on the "Loans" tab in our `Excel_Practice_Student.xlsx spreadsheet`

- Fill in the values for Loans A-D
  - Add Principal Amount
  - Add interest rate
  - Add “12 months”
  - Interest Paid = principle * rate
  - Total Loan Cost = principle + interest paid
  - Monthly payment = Total Loan Cost / Months
  - CTRL D to fill down
- CREATE A BAR CHART FOR THE LOANS

### Once your data is filled out

1. Highlight the information you want to chart

    - For example, highlight A1:B5

2. Click [**Insert**] in the ribbon
3. Bring up chart options
4. Pick the ones you want

<br>

---

<br>

## 3. **Excel: Inserting Pivot Tables**

Open Up `PivotTable_exercise.xlsx Spreadsheet` in the activities folder.

We will work on the Expenses tab. There is also a tab with the instructions for this exercise.

<br>

1. Once you bring up your spreadsheet, open the Expenses sheet tab and note that one of the column headings is blank

    - we will not be able to create a pivot table which includes all the data on the Expenses sheet if one of the field names that need to be used in our pivot table is blank. Select cell F2 and enter the following heading for the column: 'Tax Code'

2. Insert the data on the Expenses sheet into an `Excel table`.

    - If the source data of a pivot table is included in an Excel table, you will not have to edit the source data cell range of the pivot table when you add additional transactions at the bottom of the Expenses sheet.

3. Change the table name to: 'ExpTable'

4. Create a pivot table on a new worksheet which is based on all the cells that have been inserted into the new Excel table. Use the pivot table to display the total tax inclusive amount for each supplier that is included in our source data.

    - Click on [**PivotTable**]
    - Dataset should already be selected
    - Select [**New Worksheet**]
    - Choose the values that you want
    - Analyze your data

5. Rename the new sheet as: Suppliers

6. Change the number formatting in the amount section of the pivot table so that all the amounts include thousands separators and two decimal numbers. Use the pivot table feature for this purpose so that the new number formatting is retained after the pivot table is refreshed.

7. Change the column width of column B to 16.

8. Wrap the column heading in column B so that it is displayed in two lines and center the text.

9. Change the pivot table settings so that the adjusted column width is retained after refreshing the pivot table.

10. Open the Expenses sheet and change the amount in row 14 from 13,000 to 33,000.

11. Open the Suppliers sheet and note the grand total at the bottom of the pivot table. Refresh the pivot table and note the change in the grand total.

12. Change the order of the supplier names in column A so that the suppliers are sorted in a descending order (from Z to A).

13. Drill down to the source data that makes up the supplier total for the "IAS Accountants supplier".
    * Hint: select the "Sum of Tax Inclusive Amount" value for "IAS Accountants"

14. Rename the new sheet as: "IAS"

<br>

---

<br>

## 4. **Excel: Inserting Pivot Charts**

Open Up `SalesData_exercise.xlsx Spreadsheet` in the activities folder.

We will work on the Sales data tab. There is a tab with instructions for this exercise as well as a tab with Homework instructions.

<br>

1. Select all sales data and create a pivot table
2. Select [**Insert**]
3. Select [**PivotTable**]
4. Table/Range should be picked already
5. Save as a new Worksheet
6. Change the sheet name to "Trujiullo"
7. In the Pivot Fileds panel, select: [**CompanyName**, **ProductName**, **UnitPrice**, **Quantity** and **SubTotal**]
8. On the spreadsheet select the [**Row Labels**] drop down, remove the "select all" tick, select [**Ana Trujiullo**], press [**Ok**]
   * NOTE: [**Row Labels**] is not an option on Excel Online. Instead, click on the dropdown on [**Company Name**] and then “Filter” from the dropdown. De-select "Select All", and only select [**Ana Trujiullo**], press [**Ok**].
9. Make sure table is selected
   * NOTE: “Pivot Charts” is not an option in Excel Online. For steps 9-14, as long as you’re in the pivot table, you just select [**Insert**] and then “Charts”. ([Excel Online Documentation](https://techcommunity.microsoft.com/t5/excel-blog/insert-pivotchart-is-available-in-excel-for-the-web/ba-p/613671))
10. Select [**Insert**]
11. Select [**Pivot Charts**]
12. Select the chart and press OK
13. Position and size your chart.
14. Update the table and save the workbook

<br>

---

<br>
