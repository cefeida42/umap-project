"""Script to make cutout for all objects in the object table."""
import pandas as pd
#mport numpy as np
#import imageio
import os, sys, time
from joblib import delayed, Parallel


def make_cutout(objectId, ra, dec, output_dir="."):
    # web api url template
    url = "https://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?"+"ra={}&dec={}&scale=0.4&height=64&width=64".format(ra, dec)
    print(ra)
    print(dec)

    # saving path template
    save_path = f"{output_dir}/{objectId}.png"
    if os.path.exists(save_path):
        print(f"{save_path} already exists.")
    else:
        try:
        	os.system(f'wget -O {save_path} "{url}"')
        except:
        	print(f"Problem downloading image with {objectId}...")
    #print("Problem downloading image with ObjectID = {objectID}")


def main(objectTablePath, output_dir):

    # create directory if not exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # read min object table and reset index (move objectId into cols)
    object_df = pd.read_parquet(objectTablePath, columns=["ra", "dec"])
    object_df_flat = object_df.reset_index()

    ## TEST code
    #object_df_flat = object_df_flat.iloc[:50].copy()
    
    n_core = 8
    Parallel(n_jobs=n_core)(delayed(make_cutout)(
        row[1]["objectId"], row[1]["ra"], row[1]["dec"], output_dir=output_dir
    )
    for row in object_df_flat.iterrows()
)
    
    # for row in object_df_flat.iterrows():
    # 	make_cutout(row[1]["objectId"], row[1]["ra"], row[1]["dec"], output_dir=output_dir)


if __name__ == "__main__":

   #objectTablePath = sys.argv[1]  # Path for 'ObjectTable.parquet'
   #output_dir = sys.argv[2]  # Directory to save cutouts
    objectTablePath = "./data/s82ObjectTable.parquet"
    output_dir = "./data/cutouts"
    main(objectTablePath, output_dir)
