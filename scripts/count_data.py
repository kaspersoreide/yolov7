# This is a modified version of a script found here:
# https://gist.github.com/wfng92/c77c822dad23b919548049d21d4abbb8

import xml.etree.ElementTree as ET
import glob
import os
import json
from distutils.dir_util import copy_tree


classes = {
    'D00': 0, 
    'D10': 0, 
    'D20': 0, 
    'D40': 0
}
input_dir = "./data/RDD2022/Norway/train/annotations/xmls/"

# identify all the xml files in the annotations folder (input directory)
files = glob.glob(os.path.join(input_dir, '*.xml'))
# loop through each 
for fil in files:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]
    tree = ET.parse(fil)
    root = tree.getroot()
    for obj in root.findall('object'):
        label = obj.find("name").text
        # check for new classes and append to list
        if label not in classes.keys():
            continue # skip unknown classes
        classes[label] += 1

# generate the classes file as reference
with open('classes_occurrences.txt', 'w', encoding='utf8') as f:
    f.write(json.dumps(classes))