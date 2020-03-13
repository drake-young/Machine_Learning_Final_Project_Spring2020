# ================================================================================
# CLASS: Utility
# ================================================================================
#
# Constructor: empty constructor, no input, no attributes
#
# Member Functions:
#   - dataframe_to_image: convert each row of a pandas dataframe to a png and save
#      * (self, df , base_filename , dims=[20,20] , mode='RGB')
#
#   - image_to_dataframe: read an image file and convert to a pandas dataframe
#      * (self, filename)
#
#   - directory_to_dataframe: iterate over a given directory and convert each image
#                             into a single dataframe
#      * (self, directory_path)
#
#   - dataframe_to_csv: store a given pandas dataframe as a CSV
#      * (self, dataframe, filename)
#
# ================================================================================
class Utility:
    # === Constructor === #
    def __init__( self ):
        return

    # === External Functions === #
    from .tasks.dataframe_to_image     import dataframe_to_image
    from .tasks.image_to_dataframe     import image_to_dataframe
    from .tasks.directory_to_dataframe import directory_to_dataframe
    from .tasks.dataframe_to_csv       import dataframe_to_csv
