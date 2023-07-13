# Configuration of the parameters for the 3-FinalRasterAnalysis.ipynb notebook
class Configuration:
    '''
    Configuration for the notebook where objects are predicted in the image.
    Copy the configTemplate folder and define the paths to input and output data.
    '''
    def __init__(self):
        
        # Input related variables
        self.input_image_dir = r'I:\results\SST\landsat\extractWithLocation\extract50_withLocation'
        self.input_image_type = '.tif'
        self.WST_fn_st = 'delta_'
        self.label_fn_st = 'annotation_'
        self.trained_model_path =  r'I:\Unet\v1\v1\notebooks\saved_models\UNet\plumes_normalized_20220106-2216_adam_focalTversky_012_256.h5'  

        # Output related variables
        self.output_dir = r'I:\results\SST\landsat\prediction50_normal'
        self.output_image_type = '.tif'
        self.output_prefix = 'pred50_'
        self.output_shapefile_type = '.shp'
        self.overwrite_analysed_files = False
        self.output_dtype='uint8'

        # Variables related to batches and model
        self.BATCH_SIZE = 16 # Depends upon GPU memory and WIDTH and HEIGHT (Note: Batch_size for prediction can be different then for training.
        self.WIDTH=256 # Should be same as the WIDTH used for training the model
        self.HEIGHT=256 # Should be same as the HEIGHT used for training the model
        self.STRIDE=20  # STRIDE = WIDTH means no overlap, STRIDE = WIDTH/2 means 50 % overlap in prediction
