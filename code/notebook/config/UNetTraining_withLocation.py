import os

# Configuration of the parameters for the 2-UNetTraining.ipynb notebook
class Configuration:
    def __init__(self):
        # Initialize the data related variables used in the notebook
        # For reading the WST and annotated images generated in the Preprocessing step.
        # In most cases, they will take the same value as in the config/Preprocessing_withLocation.py
        self.base_dir = r'I:\results\SST\landsat\extractWithLocation\extract75_withLocation'
        self.image_type = '.tif'
        self.WST_fn = 'delta'
        self.annotation_fn = 'annotation'

        
        # Patch generation; from the training areas (extracted in the last notebook), we generate fixed size patches.
        # random: a random training area is selected and a patch in extracted from a random location inside that training area. Uses a lazy stratergy i.e. batch of patches are extracted on demand.
        # sequential: training areas are selected in the given order and patches extracted from these areas sequential with a given step size. All the possible patches are returned in one call.
        self.patch_generation_stratergy = 'random' # 'random' or 'sequential'
        self.patch_size = (256,256,3) # Height * Width * (Input + Output) channels
        # # When stratergy == sequential, then you need the step_size as well
        # step_size = (128,128)
        
        # The training areas are divided into training, validation and testing set. Note that training area can have different sizes, so it doesn't guarantee that the final generated patches (when using sequential stratergy) will be in the same ratio. 
        self.test_ratio = 0.1
        self.val_ratio = 0.1
        
        # Probability with which the generated patches should be normalized 0 -> don't normalize, 1 -> normalize all
        self.normalize = 0  

    
        # The split of training areas into training, validation and testing set, is cached in patch_dir.
        self.patch_dir = r'I:\Unet\v1\v1\notebooks\patches{}'.format(self.patch_size[0])
        self.frames_json = os.path.join(self.patch_dir,'frames_list.json')


        # Shape of the input data, height*width*channel; Here channels are NVDI and Pan
        self.input_shape = (256,256,2) 
        self.input_image_channel = [0, 1]
        self.input_label_channel = [2]
#         self.input_weight_channel = [3]

        # CNN model related variables used in the notebook
        self.BATCH_SIZE = 16
        self.NB_EPOCHS = 200 #200

        # number of validation images to use
        self.VALID_IMG_COUNT = 25
        # maximum number of steps_per_epoch in training
        self.MAX_TRAIN_STEPS = 250 #1000
        self.model_path = r'I:\Unet\v1\v1\notebooks\saved_models\UNet'

