# Solution for the pharmacy-counting project

## Instruction

The source file is named pharmacy_count.py, which is located at "./src/pharmacy_count.py".
The sys package is imported in pharmacy_count.py to get command-line arguments.

### Data Structure
Three classes are defined in the module.

OrderRecord:
    This class is used to store a single record in the inputed order records.
    This class will be used by the DrugCostNode class and the DrugCostList class as the basic input data.
    
DrugCostNode:
    This class serves as the node of the DrugCostList class.
    The nodes, or instance of this class, store the name of the drug, the individuals who prescribed the drug and the total cost.
    Attributes:
        drug_name (str): Name of the drug.
        total_cost (float): Total cost of the drug
        prescribers (set): People who prescribed the drug, uniqued by (first_name, last_name)
        
DrugCostList:
    This class is a list of instances of the DrugCostNode class.
    Attributes:
        list_nodes (list): a list of nodes, which are instances of the DrugCostNode class.

### Algorithm
Searching:
The searching method in DrugCostList is find_drug(self, drug_name). 
Linear search is applied here.

Sorting:
The sorting method in DrugCostList is sort_by_cost(self).
The built-in sorted() is applied here.
        
### Main Function

Creat an instance of DrugCostList class, namely dcl, to store the results of drug total costs. 

Read the input file line by line to update dcl. For each line, or record:
* Store the information to a instance of OrderRecord class, namely record.
* Update dcl with record.  

When all records have been read, sort dcl in descending order based on total costs.
Print the list to output file.


## Tests

### Test 1: 

A defaulted test as required.

### Test 2: 

Test 2 is to check if there are missing values in the input file.
The records with incompleted values with be skipped when calculating total costs.

