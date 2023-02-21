**Shonit Gangoly** 
[@ShoGan20](https://github.com/ShoGan20)   
 
 *How to Run the project*:

Running Masking.py (Aim of this program is to mask the ground-truth images):  
    
    1. Run 'pip install -r requirements.txt' for all needed libraries
    2. Use the following steps to mask images:
        a. In your testing images set, clone the folder for images and rename it as masks
        b. Copy path of this folder and set as path in 'output_dir' variable
        c. Copy path of you testing ground truth folder and set as path in 'file_dir' variable
    3. Run 'python Masking.py' to mask the testing images

Running Zipper.py (The aim of this program is to zip the images to upload onto google colab):  
    
    1. Copy path of your testing images set
    2. Set as path in line 4
    3. Run 'python Zipper.py' to zip the testing images
    
Running on Colab:  
    
    1. Compress your testing images along with checkpoint.pth(Trained Model used for project)
    2. Import BioTrillion_Challenge_CV to Google Colab.
    3. Run the first block to upload the zipped testing and checkpoint file
    4. Run the second block to unzip the files onto the colab directory.
 
Testing images using ipynb file:  
    
    1. Copy path of checkpoint.pth and set it in the checkpoint_path variable
    2. Copy path of your testing images, ground-truth and masks and set path in the 'Setting dataset paths block'
    3. Run the subsequent blocks along with dataloader block
    4. You can then run the Testing function block to load the model from checkpoint
    
Evaluating results:  
    
    1. Create a folder in colab directory called 'pred_masks'
    2. Copy path of this folder and set path in the 'Visualising results block' in the variable 'file_path'
    3. Run the subsequent blocks to visualise and evaluate testing images

**Please reach out to me in case of any issues while running**
