# ================================================================================
# main.py
# ================================================================================
# Main driver of the program, responsible for setting up the query methods,
# calling the appropriate queries, evaluating performance, and reporting
# the results.
# ================================================================================

# === Imports === #
from time    import perf_counter  # used to evaluate performance
from Utility import *             # utility class & functions
from LSH     import *             # locality-sensitive hash class & functions

# === Setup Utility and LSH, Time LSH Setup Overhead === #
util = Utility( )  # create Utility class instance
t0   = perf_counter( )  # start overhead timer
lsh  = LSH( A='dataset/patches_color.csv' , k=20 , L=10 )  # create LSH class instance
t1   = perf_counter( )  # end overhead timer

# === LSH Query by a Given Index, Time the Query === #
'''PREFERRED TO QUERY BY IMAGE INSTEAD
query_index = 1  # index of CSV to query from
t2          = perf_counter( )  # start query timer
lsh_results = lsh.lsh_search_by_index( query_index , num_neighbors=5 )  # get 5 nearest neighbors
t3          = perf_counter( )  # end query timer
query_df , lsh_neighbor_df , lsh_dist_arr = lsh_results  # parse query results
'''

# === LSH Query by a Given Image Filepath/Filename === #
query_file  = 'query/patch-1.png'  # filename/filepath of query image
query_df    = util.image_to_dataframe( query_file )  # convert the query image to a dataframe
t2          = perf_counter( )  # start query timer
lsh_results = lsh.lsh_search_by_dataframe( query_df , num_neighbors=5 )  # get 5 nearest neighbors
t3          = perf_counter( )  # end query timer
lsh_neighbor_df , lsh_dist_arr = lsh_results  # parse query results

# === Output Results with Formatting === #
print( '\nCandidates Distances:\n' , lsh_dist_arr    )
print( '\nCandidates Dataframe:\n' , lsh_neighbor_df )
print( '\nTime to Hash: '          , ( t1 - t0 )     )
print( 'Time to Query: '           , ( t3 - t2 )     )

# === Save the Nearest Neighbors as Images === #
util.dataframe_to_image( lsh_neighbor_df , 'output/lsh-result' )
