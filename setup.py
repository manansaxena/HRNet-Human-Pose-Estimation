import os
from shutil import copyfile,copytree
from distutils.dir_util import copy_tree


base_data_path = "/content/drive/My Drive/Trinity/data/"
zip_data_path = base_data_path + "OCHuman.zip"
model_data_path = base_data_path + "HRNet_trained/pytorch"
# clone the github repo
# os.system("git clone https://github.com/manansaxena/HRNet-Human-Pose-Estimation.git")

# change directory
# os.chdir("./HRNet-Human-Pose-Estimation/")

# install requirements
os.system("pip install -r requirements.txt")

# change directory
os.chdir("./lib")

# make
os.system("make")

# change directory
os.chdir("../../")

# install COCOAPI
COCOAPI = "./COCOAPI"
os.system("git clone https://github.com/cocodataset/cocoapi.git $COCOAPI")
os.chdir("./cocoapi/PythonAPI")
os.system("make install")

# change directory
os.chdir("../../")

# Install OCHUMANAPI
os.system("git clone https://github.com/liruilong940607/OCHumanApi")
os.chdir("./OCHumanApi")
os.system("make install")
copyfile(zip_data_path,"./OCHuman.zip")
os.system("unzip OCHuman.zip")
os.system("rm OCHuman.zip")
os.system("unzip ./OCHuman/images.zip")
os.system("rm ./OCHuman/images.zip")

# changing directory
os.chdir("../HRNet-Human-Pose-Estimation/")
os.mkdir("./output")
os.mkdir("./log")
os.mkdir("./data")
os.mkdir("./models")
copy_tree(model_data_path,"./models/")
os.mkdir("./data/oc")
os.mkdir("./data/oc/person_detection_results")
os.mkdir("./data/oc/person_detection_results/OCHuman")
os.mkdir("./data/oc/images")

# Transferring OC data to HRNet pose repo
copy_tree('../OCHumanApi/images','./data/oc/images')
copy_tree('../OCHumanApi/OCHuman','./data/oc/person_detection_results/OCHuman')



