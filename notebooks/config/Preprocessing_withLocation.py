
import os


# Configuration of the parameters for the 1-Preprocessing.ipynb notebook
class Configuration:
    '''
    Configuration for the first notebook.
    Copy the configTemplate folder and define the paths to input and output data. Variables such as raw_WST_image_prefix may also need to be corrected if you are use a different source.
    '''
    def __init__(self):
        # For reading the training areas and polygons
        self.training_base_dir = r'I:\results\SST\landsat\sampleAnnotation5_hard'
        self.training_area_fn = 'area_all.shp'
        self.training_polygon_fn = 'core5_hard.shp'
        self.training_plus1_fn = 'plus1_hard.shp'
        
        # For reading the WST images
        self.bands = [0]
        self.raw_image_base_dir = r'I:\results\SST\landsat\delta'
        self.raw_image_file_type = '.tif'
        self.raw_WST_image_prefix = 'delta'

        # For writing the extracted images and their corresponding annotations file
        self.path_to_write = r'I:\results\SST\landsat\extractWithLocation\extract50_hard_withLocation'
        self.show_boundaries_during_processing = False
        self.extracted_file_type = '.tif'
        self.extracted_WST_filename = 'delta'
        self.extracted_annotation_filename = 'annotation'
        

        # Path to write should be a valid directory
        assert os.path.exists(self.path_to_write)

