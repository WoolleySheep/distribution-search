# Search functions
## Python implementations of common list-search algorithms
### TODO
* Convert into a package

### Algorithms implemented
* **Unsorted lists:**
  * Linear search
* **Sorted lists:**
  * Binary search
  * Jump search
  * Exponential search
  * Fibonacci search
* **Uniformly-distributed sorted lists:**
  * Interpolation search
  
### Repository structure
* **list_search_functions**: Search algorithm implementation files
  * *list_search_functions.py*: A collection of list-searching functions, utilising various algorithms
* **tests**: Test files
  * *test_list_search_functions.py*: Unittests for list-searching functions
  * *test_check_Array_format.py*: Unittests for array verification functions
* **tools**: Files to assist with algorithm analysis and use
  * *check_array_format.py*: Functions for testing whether an object can be searched
  * *compare_runtimes.py*: Script comparing algorithm runtime over various length lists

### Setup & Requirements
* Have Python 3.8.2+ installed, as well as pip
* Clone the repository using `git clone https://github.com/WoolleySheep/search-functions.git`
* To use just the search functions, no additional modules need to be installed
* To use the tools, install the relevant packages using `pip install -r requirements.txt`
* To run tests and utilise code styling, install the relevant packages using `pip install -r requirements-dev.txt`
