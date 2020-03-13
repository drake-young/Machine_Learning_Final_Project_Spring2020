# ================================================================================
# LSH.get_candidates_dataframe
# ================================================================================
#
# Input:
#   - query_dataframe: dataframe consisting of a single row of RGB tuples
#      * NOTE: it is assumed that the number of columns in the query is the same as
#              the number in self.A
# Output:
#   - dataframe containing all of the "candidates" from self.A
#     where a "candidate" is defined as any entry which has hashed to the same
#     hash value given the same hash function. Based on the principle of Locality-Sensitive
#     Hashing, entries that hash to the same "bucket" are more likely to be "similar"/the same
#     than other images
# Task:
#   - hash the query dataframe using the same hash functions that created self.hashed_A
#     by calling self.hash_data() on the given query dataframe
#   - extract the hashed values of the query from the results of the previous step
#   - filter self.hashed_A to extract the indices of all rows which match the hash
#     in at least one column
#   - extract the original image vecotrs from A using those indices, and return
#     those vectors as a dataframe
#
# ================================================================================
def get_candidates_dataframe( self , query_dataframe ):

    # === Hash the Query and Extract the Hash Values === #
    hashed_point = self.hash_data( query_dataframe )
    query_hash   = hashed_point.iloc[0]

    # === Extract Index Values of all Entries Which Share the Same Hash === #
    candidates   = [ i for i in self.hashed_A[self.hashed_A==query_hash].dropna( how='all' ).index ]

    # === Return the Original Vectors Corresponding to those Indices === #
    return self.A.iloc[candidates]
