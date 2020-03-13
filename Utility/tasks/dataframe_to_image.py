# ================================================================================
# Utility.dataframe_to_image
# ================================================================================
#
# Input:
#   - df: pandas dataframe to be saved as images
#   - base_filename: name of the file or directory where the image(s) will be saved
#      * the csv index and ".png" will be appended to the given base-filename, no need
#        to pass in the caller
#   - dims: array or tuple [x,y,<z>] representing the dimensions of the image
#      * NOTE: this function will not error-handle if dimensions don't match
#              dimensionality of the image vector, it is up to the caller to
#              ensure dimensionality matches. Though not required, it is expected
#              that the resulting image is a square
#      * NOTE: if <z> is included, the image is expected to be RGB, and must be
#              z=3
# Output:
#   - no return
#   - one .png file will be created for each row of the dataframe of the form
#      * "<base_file_name>-<rank>-<index>.png"
#        where:
#           <base_file_name> = base_file_name input parameter
#           <rank> = order in the dataframe (dataframe assumed to be sorted)
#           <index> = index value of the row. may be same as rank if dataframe is
#                     sorted by index
# Task:
#   - iterate over the rows of the given pandas dataframe
#   - extract the row (pixel vector) and use numpy to reshape into a 3 dimension
#     array where the first two dimensions are the pixel location, and the third
#     dimension is the RGB color channels
#   - use pillow (PIL) to create an image object from the reshaped array
#   - save the image object as an RGB .png file with the appropriate name
#
# ================================================================================
def dataframe_to_image( self, df , base_filename , dims=( 20 , 20 , 3 ) ):

    # === Necessary Imports === #
    from PIL   import Image  # image processing
    from numpy import array, uint8  # reshaping the pixel vector
    from ast   import literal_eval

    # === Setup Variables === #
    rank = 1

    # === Iterate the Given Dataframe === #
    for c in df.iterrows( ):
        patch = [ ]  # list to store rgb tuples

        # === Iterate the Pixels in the Vector === #
        for rgb in c[1]:
            if isinstance( rgb , str ):
                rgb = literal_eval( rgb )
            patch.append( rgb )
            continue  # end for rgb

        # === Reshape, Create Image, & Save === #
        patch   = array( patch , dtype=uint8 ).reshape( dims )
        img     = Image.fromarray( patch , 'RGB' )
        outfile = base_filename + '-' + str( rank ) + '-' + str( c[0] ) + '.png'
        img.save( outfile )

        # === Increment Counters === #
        rank += 1
        continue  # end for c
    return
