# ================================================================================
# Utility.directory_to_dataframe
# ================================================================================
#
# Input:
#   - directory_path: string representing the base directory to iterate through
#                     during dataframe construction
#      * NOTE: this function will only convert png, jpeg, and jpg files
#      * NOTE: this function will not branch into sub directories
# Output:
#   - pandas dataframe in which each row contains an RGB pixel vector representation
#     of a single image (png/jpg/jpeg) in the directory
#   - one .png file will be created for each row of the dataframe of the form
# Task:
#   - iterate over the files in the given directory
#   - if the file is an acceptable image format (png/jpeg/jpg)
#   - call Utility.image_to_dataframe on that image's filepath
#   - append that image's dataframe to a dataframe to be returned
# NOTE:
#   - It is assumed that all images in the directory are uniform in shape
#   - This function has not been tested for, nor assumed to work for directories
#     with differently shaped images
#
# ================================================================================
def directory_to_dataframe( self, directory_path ):

    # === Necessary Imports === #
    from pandas import DataFrame  # DataFrame object
    from os     import fsencode, fsdecode, listdir  # for operating with filesystem

    # === Additional Variables === #
    directory = fsencode( directory_path )  # get file system encoding of given path
    df        = DataFrame( )  # working dataframe to return

    # === Iterate Over Files in Directory === #
    for file in listdir( directory ):
        filename = fsdecode( file ).lower( )  # get name of the file

        # === Only Add to Dataframe if .png/.jpg/.jpeg === #
        if filename.endswith( '.png' ) or filename.endswith( '.jpg' ) or filename.endswith( '.jpeg' ):
            file_path = directory_path + '/' + filename  # make string path to the file
            file_df   = self.image_to_dataframe( file_path )  # convert that image file to a dataframe
            df        = df.append( file_df , ignore_index=True )  # add that dataframe to working dataframe

        continue  # end for file

    return df
