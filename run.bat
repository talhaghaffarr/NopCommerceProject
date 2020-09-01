pytest -v -s -m "sanity" TestCases/ --html=./Reports/report_sanity.html

:: pytest -v -s -m "sanity or regression" TestCases/ --html=./Reports/report_sanity__or_regression.html
:: pytest -v -s -m "sanity and regression" TestCases/ --html=./Reports/report_sanity_and_regression.html
:: pytest -v -s -m "regression" TestCases/ --html=./Reports/report_regression.html
