# ================================================================================
# CLASS: LSH
# ================================================================================
#
# Constructor:
#   Input:
#      - A: filename of csv containing the data (to be read as dataframe)
#      - k: number of thresholds (bit/byte) per hash
#      - L: number of hash functions to create
#
# Attributes
#   - A: dataframe representation of the A passed in the constructor
#   - k: as defined by constructor
#   - L: as defined by constructor
#   - functions: list of L custom hash functions with k thresholds
#   - hashed_A: dataframe representation of A with each row's output for each hash function
#
# Getters:
#   - get_A
#   - get_hashed_A
#
# Member Functions:
#   - cosine_similarity
#      * (A, B)
#   - create_single_hash_function
#      * (dimensions, thresholds)
#   - create_hash_function_list
#      * (self, num_dimensions=400, min_threshold=0, max_threshold=255)
#   - hash_vector
#      * (v)
#   - hash_data
#      * (data)
#   - get_candidates_dataframe
#      * (query_dataframe)
#   - lsh_search_by_index
#      * (self, query_index, num_neighbors=10)
#   - lsh_search_by_dataframe
#      * (self, query_dataframe, num_neighbors=10)
#
# ================================================================================
class LSH:
    # === Constructor === #
    def __init__( self , A , k , L ):
        # === Imports === #
        from pandas import read_csv

        # === Store Attributes === #
        self.k         = k
        self.L         = L
        self.A         = read_csv( A , header=None )
        self.functions = self.create_hash_function_list( num_dimensions=len( self.A.columns ) )
        self.hashed_A  = self.hash_data( self.A )
        return # __init__


    # === Getters for Debugging === #
    def get_A( self ):
        return self.A


    def get_hashed_A( self ):
        return self.hashed_A


    # === External Functions === #
    from .tasks.cosine_similarity           import cosine_similarity
    from .tasks.create_single_hash_function import create_single_hash_function
    from .tasks.create_hash_function_list   import create_hash_function_list
    from .tasks.hash_vector                 import hash_vector
    from .tasks.hash_data                   import hash_data
    from .tasks.get_candidates_dataframe    import get_candidates_dataframe
    from .tasks.lsh_search_by_index         import lsh_search_by_index
    from .tasks.lsh_search_by_dataframe     import lsh_search_by_dataframe
