import os
from pathlib import Path 
import logging

project_name = "finance_complaint"
list_of_files = [ 
    ".github/workflow/.gitkeep",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/prediction/__init__.py",
    f"{project_name}/components/training/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/pippeline/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/database/__init__.py",
    f"{project_name}/constant/environment/__init__.py",
    f"{project_name}/constant/model/__init__.py",
    f"{project_name}/constant/prediction_pipeline_config/__init__.py",
    f"{project_name}/constant/training_pipeline_config/__init__.py",

    f"{project_name}/data_access/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/metadata_entity.py",
    f"{project_name}/entity/schema.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/feature.py",

    f"{project_name}/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    "main.py",
    "setup.py",
    "Dockerfile",
    "requirements.txt",
    f"{project_name}/research/trials.ipynb",


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass 