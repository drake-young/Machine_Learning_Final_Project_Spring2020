# ================================================================================
# LSH.create_hash_function_list
# ================================================================================
#
# Input:
#   - num_dimensions: the number of pixels expected in the image vector (default=400)
#   - min_threshold: minimum value a randomly generated threshold can have (default=0)
#   - max_threshold: maximum value a randomly generated threshold can have (default=255)
# Output:
#   - list of length L, where each item in the list is a custom hash function, which takes
#     a vector v as input, and outputs a k-digit number
# Task:
#   - iterate self.L times
#   - each iteration, generate k random dimensions (pixel coordinates) and k random
#     thresholds to correspond to those dimensions
#   - use the randomly generated values to create a hash function using
#     self.create_single_hash_function()
#   - append the custom hash function to the list of functions to be returned
# NOTE: the hash functions are described in better detail in create_single_hash_function.py
#       but at the high-level, it will be a numerical value with k digits
#       where each digit contains a value between 0 and 7 indicating which color
#       channels at that pixel pass that threshold. The output will be
#
# ================================================================================
def create_hash_function_list( self , num_dimensions=400 , min_threshold=0 , max_threshold=255 ):

    # === Necessary Imports === #
    from numpy import random

    # === Setup Variables === #
    functions = [ ]

    # === Iterate self.L Times === #
    for i in range( self.L ):

        # === Produce self.k Random Dimensions and Corresponding Thresholds === #
        dimensions = random.randint( low=0             , high=num_dimensions  , size=self.k )
        thresholds = random.randint( low=min_threshold , high=max_threshold+1 , size=self.k )

        # === Add the Customly Generated Hash Function === #
        functions.append( self.create_single_hash_function( dimensions , thresholds ) )
        continue # end for i

    # === Return Value === #
    return functions
