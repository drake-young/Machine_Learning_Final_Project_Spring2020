# ================================================================================
# LSH.lsh_search_by_index
# ================================================================================
#
# Input:
#   - query_index: integer representing the index of self.A (row of CSV)  to be used as
#                      the query, it is assumed the query dataframe contains the same
#                      number of columns as the dataset (self.A).
#   - num_neighbors: integer representing how many "nearest neighbors" to return
# Output:
#   - Tuple of the form (query_dataframe, n_candidates, distances)
#      * query_dataframe: dataframe containing the vector held in self.A at the
#                         given index
#      * n_candidates: dataframe containing the n-nearest candidate vectors to the query
#                      (using cosine similarity), in descending order of "nearness"
#                      so the top of the dataframe are the most similar to the query
#      * distances: two-column dataframe "Data_Index" and "Cosine_to_Query", sorted by cosine
#         > Data Index is the index in self.A (row in the CSV) that corresponds to the
#           nearest neighbor candidates
#         > Cosine to Query is the cosine similarity score between that vector and the query
# Task:
#   - Extract the row being queried from self.A
#   - Get the Candidates to Examine using self.get_candidates_dataframe()
#   - iterate over these candidates vectors and compute the cosine similarity to
#     the query
#   - order the candidates by cosine in descending order
#   - filter to keep only the num_neighbors most similar are considered
#   - Extract those neighbors in the right order and store the extraction
#     as a dataframe
#   - Create a Dataframe of the Similarity Scores
#   - return the two dataframes from the previous steps
#
# ================================================================================
def lsh_search_by_index( self , query_index , num_neighbors=10 ):

    # === Required Imports === #
    from pandas import DataFrame

    # === Extract Query as DataFrame === #
    query_dataframe = self.A.iloc[[query_index]]

    # === Extract Candidates === #
    candidates = self.get_candidates_dataframe( query_dataframe )

    # === Compute Similarity for Each Candidate === #
    distances = list( )
    for ( idx , pts ) in candidates.iterrows( ):
        dst = self.cosine_similarity( pts , query_dataframe.iloc[0] )
        distances.append( ( idx , dst ) )

    # === Organize Distances Log by Similarity in Descending Order and Take num_neighbors Best === #
    distances = sorted( distances , key=lambda x: x[1] , reverse=True )
    distances = distances[ : min( len( distances ) , num_neighbors ) ]

    # === Extract Candidates Vectors in Order of Similarity === #
    candidates_indices = [ cd[0] for cd in distances ]
    n_candidates       = DataFrame( )
    for i in candidates_indices:
        n_candidates = n_candidates.append( candidates[ candidates.index == i ] )

    # === Convert Distances Log to DataFrame === #
    distances = DataFrame( distances , columns=[ 'Data_Index' , 'Cosine_to_Query' ] )

    # === Return the DataFrames === #
    return query_dataframe , n_candidates , distances
