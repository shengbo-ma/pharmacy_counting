


# -*- coding: utf-8 -*-
"""
    File: pharmacy_counting.py
    Pyhton Version: 3.7.2
    Candidate: Shengbo Ma
    Discription: 
        This module generate a list of all drugs from the a list of order records. 
        This module is use only default data structures in python to meet the requirements of coding challenge.
    
"""
import sys
class OrderRecord():
    '''
    This class is used to store a single record in the inputed order records.
    This class will be used by the DrugCostNode class and the DrugCostList class as the basic input data.
    '''
    def __init__(self, record=None):
        """
        Create a node instance given a record.
        Check if the record in completed. If not, raise ValueError.
        """
        if type(record) == str:
            items = record.strip().split(',')
            if (type(items) == list and len(items) == 5):
                
                if '' in items:# find missing values in record
                    raise ValueError
                    
                self.id = items[0]
                self.last_name = items[1]
                self.first_name = items[2]                
                self.drug_name = items[3]

                try:  
                    if '.' in items[4]:
                        self.cost = float(items[4])
                    else:
                        self.cost = int(items[4])
                except ValueError as e:
                    raise
                    
                if self.cost <= 0: 
                    raise ValueError
                    
            else: 
                raise ValueError

        else:
            raise ValueError
        
class DrugCostNode():
    """This class serves as the node of the DrugCostList class.
    
    The nodes, or instance of this class, store the name of the drug, the individuals 
    who prescribed the drug and the total cost.
    
    Attributes:
        drug_name (str): Name of the drug.
        total_cost (float): Total cost of the drug
        prescribers (set): People who prescribed the drug, uniqued by (first_name, last_name)
    
    
    """
    
    def __init__(self, record):
        """
        Args:
            record (OrderRecord): The record for updating.
        """
        self.drug_name = record.drug_name
        self.total_cost = record.cost
        self.prescribers = set([(record.first_name, record.last_name)]) # maintain the unique names of prescribers

    def update(self, record):
        """When fed a new record of the drug, the node is updated by adding the prescriber's name and additional cost.
        Args:
            record (OrderRecord): The record for updating.
        """
        # Update the node only when the drug name of the new record is the same.
        if record.drug_name == self.drug_name: 
            self.total_cost += record.cost # update the total_cost
            self.prescribers.add((record.first_name, record.last_name)) # update the prescribers
            
    def __str__(self):
        
        return self.drug_name + ',' + str(len(self.prescribers)) + ',' + str(round(self.total_cost,2))
        
class DrugCostList():
    """this class is a list of instances of the DrugCostNode class.

    Attributes:
        list_nodes (list): a list of nodes, which are instances of the DrugCostNode class

    """
    
    def __init__(self):
        
        self.list_nodes = list()

    def size(self):
        return len(self.list_nodes)
        
    def add_node(self, node):
        """
        Adding a node to list_nodes
        """

        self.list_nodes.append(node)

    def find_drug(self, drug_name):
        for idx, node in enumerate(self.list_nodes):
            if node.drug_name == drug_name:
                return idx
        return None
        
    def update_from_record(self, record):
        """Update list_nodes when fed a record.
        
        If the drug is already in list_nodes, update drug information (prescribers, total_cost).
        If the drug is not in list_nodes, add it according to the record.
        """
        
        if record.drug_name != '':
            
            idx = self.find_drug(record.drug_name)
            
            if idx is None: # Drug not found
                new_node = DrugCostNode(record)
                self.add_node(new_node)
            else:
                node = self.list_nodes[idx]
                node.update(record)
                
    def sort_by_cost(self):
        # sort the drugs to be in descending order based on total_cost
        self.list_nodes = sorted(self.list_nodes, key=lambda node: node.total_cost, reverse=True)
        
    def __str__(self):
        """
        Print the drug information in a format of "drug_name,num_prescriber,total_cost"            
        """
        
        results = "drug_name,num_prescriber,total_cost"
        for node in self.list_nodes:
            results += ('\n' + node.drug_name + ',' + str(len(node.prescribers)) + ',' + str(round(node.total_cost,2)))
        return results
    
    def write_to_file(self, path):
        
        with open(path, 'w') as f_out:
            f_out.write(self.__str__())
            


if __name__ == "__main__":

    """
    Creat an instance of DrugCostList class, namely dcl, to store the results of drug total costs.
    
    Read the input file line by line to update dcl. For each line, or record:
    * Store the information to a instance of OrderRecord class, namely record.
    * Update dcl with record.
    
    When all records have been read, sort dcl in descending order based on total costs.
    Print the list to output file.
    """
    input_file = sys.argv[1]
    output_file = sys.argv[2]

            
    dcl = DrugCostList();
    with open(input_file, 'r') as f_in:

        for line in f_in.readlines()[1:]: # skip the header
            try:
                record=OrderRecord(line)
                dcl.update_from_record(record)
            except ValueError as e:
                print("Unexpected Record:"+line.strip())
            
    
    dcl.sort_by_cost()
    dcl.write_to_file(output_file)    

