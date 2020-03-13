# ================================================================================
# Utility.image_to_dataframe
# ================================================================================
#
# Input:
#   - filename: string representing name/relative-path to the image file
# Output:
#   - pandas dataframe with one row in which each column is an rgb tuple
#     representation of a single pixel in the image
# Task:
#   - open the image file
#   - extract the pixel data
#   - convert the pixel data into a dataframe
#      * not in desired form: each row having three columns (R,G,B) with each row
#        being a single pixle.
#   - zip the R, G, and B columns together into a tuple
#   - Transpose the dataframe to be a single row
#   - Return this dataframe
#
# ================================================================================
def image_to_dataframe( self , filename ):

    # === Necessary Imports === #
    from PIL    import Image  # for extracting image dagta
    from pandas import DataFrame  # data structure for representing dataframe

    # === Functionality === #
    im    = Image.open( filename )  # Open working image file
    px    = list( im.getdata( ) )  # extract pixel data
    df    = DataFrame( px )  # cast to dataframe
    df[0] = list( zip( df[0] , df[1] , df[2] ) )  # zip R,G,B columns (unnamed) together
    df    = DataFrame( df[0] )  # cast the zipped column to a new dataframe
    df    = df.T  # transpose the dataframe to be a single row

    # === REturn Value === #
    return df
