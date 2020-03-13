# ================================================================================
# LSH.hash_data
# ================================================================================
#
# Input:
#   - data: dataframe to be hashed, it is assumed that each entry in the dataframe
#           satisfies the requirements of the hash functions
# Output:
#   - dataframe where each entry corresponds to the L different k-digit hash values
#     by calling that value on each of the functions in self.functions
# Task:
#   - iterate over each entry of data
#   - call self.hash_vector() for each of those entries
#   - add that result to a list using a generator
#   - cast the generated list to a pandas DataFrame object
#   - return the dataframe
#
# ================================================================================
def hash_data( self , data ):

    # === Required Imports === #
    from pandas import DataFrame

    # === Return Value === #
    return DataFrame( [ self.hash_vector( v[1] ) for v in data.iterrows( ) ] )
