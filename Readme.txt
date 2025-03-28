To reproduce analysis:
On docker use andreaphp/datascience:10_05_2023 with GPU access, we used for our analysis an NVIDIA Quadro RTX 5000 

Recreate the conda enviroment with conda create --name <env_name> --file conda/spec_list.txt, after that you will use your conda env as a jupyter kernel.

Download GDC data using the GDC download tool and the provided manifest in the "GDC Data Download" folder

Change the .env file to reflect where you put code and data in the code


