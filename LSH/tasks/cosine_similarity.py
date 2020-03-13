# ================================================================================
# LSH.cosine_similarity
# ================================================================================
#
# Input:
#   - A: first vector to be compared
#   - B: second vector to be compared
#   * NOTE: it is assumed that |A|==|B|
#   * NOTE: it is assumed that both A and B are vectors of tuples modeling pixels
#   * NOTE: it is assumed that neither A nor B are the zero-vector
# Output:
#   - the result of the cosine similarity score evaluated between the two
#     vectors with a maximum value of 1 (subject to machine precision variation)
#   - one .png file will be created for each row of the dataframe of the form
# Task:
#   - iterate over each tuple in each vector (RGB color channels of the pixel)
#   - increment the numerator and two components of the denomenator appropriately
#   - return the final computation
# Formula:
#   cos(AB) = sum_i_to_n(Ai*Bi) / ( sqrt(sum_i_to_n(Ai^2)) * sqrt(sum_i_to_n(B^2)) )
#
# ================================================================================
def cosine_similarity( self , A , B ):

    # === Necessary Imports === #
    from numpy import sqrt, array
    from ast import literal_eval

    # === Necessary Variables === #
    numerator    = 0
    denominator1 = 0
    denominator2 = 0

    # === Iterate Over Pixels in the Vectors === #
    for i in range( len( A ) ):

        # === Convert Pixel A[i] to Numpy Array: Cast to Tuple First if String === #
        if isinstance( A[i] , str ):
            Ai = array( literal_eval( A[i] ) )
        else:
            Ai = array( A[i] )

        # === Convert Pixel B[i] to Numpy Array: Cast to Tuple First if String === #
        if isinstance( B[i] , str ):
            Bi = array( literal_eval( B[i] ) )
        else:
            Bi = array( B[i] )

        # === Increment Summations === #
        numerator    += sum( Ai * Bi )
        denominator1 += sum( Ai * Ai )
        denominator2 += sum( Bi * Bi )
        continue  # end for i

    # === Return Final Computation === #
    return numerator / ( sqrt( denominator1 ) * sqrt( denominator2 ) )
