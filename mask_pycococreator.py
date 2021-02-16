import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools


ROOT_DIR = './'
IMAGE_DIR = os.path.join(ROOT_DIR, "shapes_train")
ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations")

INFO = {
    "description": "Cell Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2021,
    "contributor": "Zhe Liu",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]


CATEGORIES = [
    {
        'id': 1,
        'name': 'cell',
        'supercategory': 'cell',
    }
]


def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    print(file_types)
    files = [os.path.join(root, f) for f in files]
    print(files)
    #files = [f for f in files if re.match(file_types, f)]
    print(files)
    
    return files
 
def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    print(file_name_prefix)
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]
 
    return files
 
def main():
 
    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }
 
    image_id = 1
    segmentation_id = 1
    
    #print(2)
    
    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        print(root)
        print(files)
        print(IMAGE_DIR)
        image_files = filter_for_jpeg(root, files)
        print(image_files)
 
        # go through each image
        for image_filename in image_files:
            print(image_filename)
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)
            print(4)
 
            # filter for associated png annotations
            for root, _, files in os.walk(ANNOTATION_DIR):
                print(5)
                annotation_files = filter_for_annotations(root, files, image_filename)
 
                # go through each associated annotation
                for annotation_filename in annotation_files:
                    
                    print(annotation_filename)
                    class_id = [x['id'] for x in CATEGORIES if x['name'] in annotation_filename][0]
 
                    category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}
                    binary_mask = np.asarray(Image.open(annotation_filename)
                        .convert('1')).astype(np.uint8)
                    
                    annotation_info = pycococreatortools.create_annotation_info(
                        segmentation_id, image_id, category_info, binary_mask,
                        image.size, tolerance=2)
 
                    if annotation_info is not None:
                        coco_output["annotations"].append(annotation_info)
 
                    segmentation_id = segmentation_id + 1
 
            image_id = image_id + 1
 
    with open('{}/instances_cell_shape_train.json'.format(ROOT_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file, indent=4)
 
 
if __name__ == "__main__":
    main()