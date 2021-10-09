# TEST PLAN:

## Table no: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** | **Result** |**Type Of Test**  |
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|------------------|
| HLT01 | Check the functionality of data_validator module | different excel files | respective identifications | identified & reported properly | PASS | Functionality |
| HLT02 | Check the functionality of data_visualization module | different excel files | respective identifications | identified & reported properly | PASS | Functionality |
| HLT03 | Check the functionality of data analysis module | Lists of data | Output of analysis functions | Proper output | PASS | Functionality |
| HLT04 | Check the functionality of logging in to the module  | username and password | successful login | login and start data validation | PASS | Functionality |



## Table no: Low level test plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** | **Result** |**Type Of Test**  |
|-------------|------|--------------------------------------------------------------|------------|-------------|----------------|------------------|------------------|
| LLT01 | HLT01 | missing_row_reporter() --> Able to check if all rows are present | Test_Input_File1.xlsx | DATA_NOT_MISSING | DATA_NOT_MISSING | PASS | Requirement |
| LLT02 | HLT01 | missing_row_reporter() --> Able to report missing rows | Test_Input_File2.xlsx | DATA_MISSING | DATA_MISSING | PASS | Requirement |
| LLT03 | HLT01 | missing_data_reporter() --> Able to check if all data is present | Test_Input_File1.xlsx | DATA_NOT_MISSING | DATA_NOT_MISSING | PASS | Requirement |
| LLT04 | HLT01 | missing_data_reporter() --> Able to report missing SR No | Test_Input_File3.xlsx | DATA_MISSING | DATA_MISSING | PASS | Requirement |
| LLT05 | HLT01 | missing_data_reporter() --> Able to report missing PS No | Test_Input_File3.xlsx | DATA_MISSING | DATA_MISSING | PASS | Requirement |
| LLT06 | HLT01 | missing_data_reporter() --> Able to report missing Names | Test_Input_File3.xlsx | DATA_MISSING | DATA_MISSING | PASS | Requirement |
| LLT07 | HLT01 | missing_data_reporter() --> Able to report missing Marks | Test_Input_File3.xlsx | DATA_MISSING | DATA_MISSING | PASS | Requirement |
| LLT08 | HLT01 | marks_validator() --> Able to check if all marks are valid | Test_Input_File1.xlsx | DATA_VALID | DATA_VALID | PASS | Requirement |
| LLT09 | HLT01 | marks_validator() --> Able to check if marks are non-numeric | Test_Input_File4.xlsx | DATA_INVALID | DATA_INVALID | PASS | Requirement |
| LLT10 | HLT01 | marks_validator() --> Able to check if marks are negative number | Test_Input_File4.xlsx | DATA_INVALID | DATA_INVALID | PASS | Requirement |
| LLT11 | HLT01 | marks_validator() --> Able to check if marks are more then defined maximum | Test_Input_File4.xlsx | DATA_INVALID | DATA_INVALID | PASS | Requirement |
| LLT12 | HLT02 | Checks if the BarChart.xlsl file is saved in the folder | marks for 3 subjects and corresponding ps Number | PASS | PASS | PASS | Requirement |
| LLT13 | HLT02 | Checks if the PieChart.xlsl file is saved in the folder | marks for 3 subjects and corresponding ps Number | PASS | PASS | PASS | Requirement |
| LLT14 | HLT02 | Checks if the Bell_curve.xlsl file is saved in the folder | marks for 3 subjects and corresponding ps Number | PASS | PASS | PASS | Requirement |
| LLT15 | HLT02 | Checks if the Overall_Report.xlsl file is saved in the folder | marks for 3 subjects and corresponding ps Number | PASS | PASS | PASS | Requirement |
| LLT16 | HLT03 | Checking functionality of average function |list of marks | Average of marks | PASS | PASS | PASS | Requirement |
| LLT17 | HLT03 | Checking functionality of percentage function |list of marks | Percentage of marks | PASS | PASS | PASS | Requirement |
| LLT18 | HLT03 | Checking functionality of grades function |list of marks | Grades of learners | PASS | PASS | PASS | Requirement |
| LLT19 | HLT03 | Checking functionality of fail_canidates function |list of marks | list of failed learners | PASS | PASS | PASS | Requirement |
| LLT20 | HLT03 | Checking functionality of top_performer function |list of marks | list of top learners | PASS | PASS | PASS | Requirement |
| LLT21 | HLT04 | Check if username is correct | username | ask for password | PASS | PASS | PASS | Requirement |
| LLT22 | HLT04 | Check if password is correct | password | start data validation | PASS | PASS | PASS | Requirement |
