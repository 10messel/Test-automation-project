# Test automation project

## Prerequisites

Install pip packages:

1. selenium
2. pytest
   ````
   pip install
   ````

## Getting started

Run the test:
````
pytest -v (to display a detailed report with tests list and their statuses) 
       -s (to output 'print')
       -m (to run the test with the appropriate mark, for example '-m smoke', see the "pytest.ini" file)
       --tb=line (to shorten the log with test results)
       test_main_page.py or test_product_page.py
````

## Project guide

Open the project in a development environment, for example, "PyCharm", and run the tests using the command described above.