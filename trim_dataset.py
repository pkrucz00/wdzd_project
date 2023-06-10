import os
from random import sample
import shutil

SAMPLES_PER_CLASS=100
OLD_FOLDER="data"
NEW_FOLDER="data-trimmed"


if __name__=="__main__":
    os.mkdir(NEW_FOLDER)
    for folder_name in os.listdir(OLD_FOLDER):
        new_class_folder_name = f"{NEW_FOLDER}/{folder_name}"
        os.mkdir(new_class_folder_name)
        print(f"Creating {new_class_folder_name}")

        list_of_samples = os.listdir(f"{OLD_FOLDER}/{folder_name}")
        trimmed_samples = sample(list_of_samples, SAMPLES_PER_CLASS)
        print(f"Number of samles: {len(trimmed_samples)}")

        for sample_name in trimmed_samples:
            shutil.copyfile(f"{OLD_FOLDER}/{folder_name}/{sample_name}", f"{new_class_folder_name}/{sample_name}")
            print(f"Copying {sample_name} to {new_class_folder_name}")
                

    