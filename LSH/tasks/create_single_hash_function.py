# ================================================================================
# LSH.create_single_hash_function
# ================================================================================
#
# Input:
#   - dimensions: list of random integers, representing the index of specific pixels
#   - thresholds: list of random integers, representing the threshold value for the pixel
# Output:
#   - reference to a function f(v)
#      * input: v = vector of pixel tuples
#      * output: numerical "hash" of the vector
#      * task: evaluate the RGB of the "dimensions" to determine whether they're >= the
#              corresponding threshold.
#      * For each of the k random pixels:
#         hash digit = 0 if R, G, B < threshold                        (000)
#         hash digit = 1 if R, G    < threshold & B       >= threshold (001)
#         hash digit = 2 if R, B    < threshold & G       >= threshold (010)
#         hash digit = 3 if R       < threshold & G, B    >= threshold (011)
#         hash digit = 4 if G, B    < threshold & R       >= threshold (100)
#         hash digit = 5 if G       < threshold & R, B    >= threshold (101)
#         hash digit = 6 if B       < threshold & R, G    >= threshold (110)
#         hash digit = 7 if                       R, G, B >= threshold (111)
# Task create_single_hash_function:
#   - define function f(v) within local scope (f defined above)
#   - return f
#   - NOTE: f is defined using the thresholds and dimensions parameters in
#           the scope of create_single_hash_function. Treat f like a
#           more verbose lambda expression.
# Task f
#   - iteratively examine the pixels in v as determined by dimensions
#   - iteratively tally the R, G, and B channels of that pixel tuple (B then
#     G then R) adding a subsequent power of 2 when that color channel threshold
#     is passed
#      * Example: RGB = (100, 200, 250), threshold = 150
#           B >= threshold --> add 2^0=1 to hash_digit (=1)
#           G >= threshold --> add 2^1=2 to hash digit (=3)
#           R <  threshold --> no add to hash digit (=3)
#           Final hash digit == 3
#   - multiply the current hash number by 10 (add new least significant digit)
#   - add the current iteration's hash digit to the hash number
#   - iterate to the next pixel specified by dimensions
#
# ================================================================================
def create_single_hash_function( self , dimensions , thresholds ):

    # === Locally Defined Hash Function to be Returned === #
    def f( v ):

        # === Variables === #
        res = 0

        # === Iterate the Random Dimensions of the
        for i in range( len( dimensions ) ):

            # === Variable Setup: clear hash, bit, and ensure rgb is a tuple === #
            rgb        = v[ dimensions[i] ]
            pixel_hash = 0
            bit        = 1
            if isinstance( rgb , str ):
                rgb = rgb.replace( '(' , '' ).replace( ')' , '' ).replace( ' ' , '' ).split( ',' )

            # === Hash the RGB Tuple === #
            for x in rgb[::-1]:  # B --> G --> R
                if int(x) >= thresholds[i]:
                    pixel_hash += bit  # set the "bit" if threshold is passed
                bit *= 2
                continue  # end for x

            # === Add the New Digit as the Least Significant Digit of the Hash Value === #
            res *= 10
            res += pixel_hash
            continue  # end for i

        return res  # f(v)


    # === Return the Locally Defined Function === #
    return f  # create_single_hash_function
