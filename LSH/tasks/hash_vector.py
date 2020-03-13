# ================================================================================
# LSH.hash_vector
# ================================================================================
#
# Input:
#   - v: vector of pixel tuples to be hashed (assumed row of pandas dataframe, but
#        not required)
# Output:
#   - list generated by calling every function in self.functions() on v. Should
#     contain self.L hash values, each being self.k-digits long
# Task:
#   - iterate over all functions in self.functions()
#   - call that function with v as input
#   - append that output to the list
#   - NOTE: the list is created using a python generator
#
# ================================================================================
def hash_vector( self , v ):

    # === Return the Generated List === #
    return [ f( v ) for f in self.functions ]
