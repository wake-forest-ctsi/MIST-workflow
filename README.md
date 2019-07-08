# MIST-workflow for creating and using the model 

Steps 1-4 can be run in a linux environment 

1. To Create the model we need to train on a certain directory. This training can also be done on specific files as well. This model will be saved: /tasks/AMIA/default_model
Can use --model_file <file> instead of --save_as_default_model since this will overwrite
  
  bin/MATModelBuilder --task "AMIA Deidentification" --save_as_default_model --input_dir ~/data/annotated/train/train76/

2. To apply the model and autotag raw ascii data we need to specify the output directory where the autotagged docs need to go, the input directory which contains the raw data and the specific model which we created in step 1.

  bin/MATEngine --task 'AMIA Deidentification' --workflow Demo --steps 'zone,tag' --input_dir ~/data/raw/test/ --input_file_type raw --output_dir ~/data/MISToutput/ --output_file_type mat-json --tagger_local --tagger_model ../tasks/AMIA/default_model
 
3. To test how the autotagged data did we need to have a scoring metric which can be run but the names of the files being tested against need to have the same name. Therefore a simple python script was created to change the name of the files created by MIST. This renames all the files in the cuurent directory (~/data/MISToutput/)

  python rename.py
 
4. Finally the scoring metric can be run. We need to specify where the MIST generated values are and the handtagged values. 

  bin/MATScore --dir ~/data/MISToutput/ --ref_dir ~/data/annotated/test/ --task "AMIA Deidentification"
