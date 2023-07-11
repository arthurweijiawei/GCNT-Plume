# GCNT-Plume: Long-term observation of global nuclear power plants thermal plumes using Landsat images and deep learning
This repository contains the neural network model (UNet) and other essential codes for segmenting nuclear power plants along global coasts and the Great Lakes. The code was written by Ankit Kariryaa (Kariryaa AT uni-bremen DOT de) in 2018, and some modifications were made by Jiawei Wei in 2022. Please contact Wei if you have any question.(email: 11930291@mail.sustech.edu.cn)

## Setup and Installation
See [INSTALL](./INSTALL.md).

## Structure
The code is structured in Jupyter notebooks available in the noteooks/ folder. Each notebook contains a considerable part of the pipeline and they are supported with core libraries available in the notebooks/core directory. Input, output paths and other configurations for each notebook must be declared in the notebooks/config/ directory. Please follow these four steps for training a UNet model and for mapping surface thermal plumes using the trained UNet model.


### Step 1: Data preparation - [Preprocessing-test_withLocation.ipynb](notebooks/1-Preprocessing-test_withLocation.ipynb)
There are two main data, the satellite images and the label of lakes in those images. The WST increment images (delta/delta_StationName_ImageName.tif; e.g., delta_Angra_LC08_218076_20130606.tif) which are used to train the model should be annotated with the plumes, while the areas that are annotated should be separately marked and stored as shapefiles. We trained two separate deep learning models (referred to as “Core50” and “Core75”, respectively) to compare their performance based on different ways to generate the training dataset. In this study, the object polygons were generated through a series of rules followed by manual inspection. (see the Methods of this article). 

The required shapefiles is available in the sampleAnnotation5/sampleAnnotation5_hard and sampleAnnotation75/sampleAnnotation75_hard, including the labelled areas (e.g., area_all.shp), the core plume polygons (e.g., core5_all.shp) and the mixed plume polygons (e.g., plus1_all.shp). Note that those Datasets and Polygons's named with "hard" did not participate in the training, validation and testing of the models.

Then, declare the input paths and other relevant configurations in notebooks/config/Preprocessing_withLocation.py file. After declaring the required paths, run the first notebook notebooks/1-Preprocessing-test_withLocation.ipynb to extract these areas with the contained object polygons as image files. Finally, write the extracted images (extractWithLocation\extract50_withLocation\delta_index_StationName_ImageName.tif; e.g., delta_0_Angra_LC08_218076_20130708.tif) and their corresponding annotations file (extractWithLocation\extract50_withLocation\annotation_index_StationName_ImageName.tif; e.g., annotation_0_Angra_LC08_218076_20130708.tif)

### Step 2: Model training - [UNetTraining.ipynb](notebooks/2-UNetTraining-test_withLocation.ipynb)
Train the UNet model with the extracted images using the UNetTraining_withLocation.ipynb notebook. Declare the relevant configuration in notebooks/config/UNetTraining_withLocation.py. In case you use an independent test set, you can use Auxiliary-1-UNetEvaluation-test_withLocation.ipynb to evaluate the performance of the model. Step-1 data preparation can also be used to extract the test set. In order to alleviate the imbalance among different Landsat missions, you can use SamplingByLandsatSeries.ipynb notebook to generate frame_list.json for train/validation/test dataset dividing. The trained models will be saved in notebooks\saved_models\UNet

### Step 3: Analyzing images - [RasterAnalysis.ipynb](notebooks/3-RasterAnalysis-test_withLocation.ipynb)
Next, use the trained model to analyze images (generate binary masks of the core plumes) using RasterAnalysis.ipynb notebook. The path to the trained model and satellite images should be declared in the notebooks/config/RasterAnalysis_withLocation.py. The model-predicted core plumes will be saved in prediction50_normal/prediction50_hard/prediction75_normal/prediction75_hard (naming format: pred50_index_StationName_ImageName.tif; e.g., pred50_0_Angra_LC08_218076_20130708.tif)
   
The occurrence_all file include the historical frequency (>0.01) of core plumes for 74 nuclear power plant outlets (naming format: StationName_occurrence99.tif; e.g., Angra_occurrence99.tif), manual screening were conducted to exclude 18 images that are hard to recognize the core plume areas (mostly in "hard" group) before occurrence calculation.

## A note on processdures and the data source
This code relies on satellite images with two channels (WST increment band and Euclidean distance band). In case your data is available in multiple channels, then the notebooks and core libraries need to be adapted accordingly. 