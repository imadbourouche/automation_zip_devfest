
import zipfile
import os
import shutil

# dir of the zip file
path = "."

while True:
    files = os.listdir(path)
    print(files)

    #find and extract the zip file
    zip_path = ""
    for file in files :
        if file.endswith('.zip') :
            zip_path = path + '\\'+ file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            os.remove(zip_path)

    # condition to leave the loop if we dont find any zip file
    if zip_path == "":
        break

    #change the diractory to the result of the extracted file if it is a dir
    files = os.listdir(path)
    for diractory in files:
        folder_essay = path + "\\"+diractory
        if os.path.isdir(folder_essay):
            path = folder_essay
            break




result = os.listdir(path)
print(result)
for file in result :
    file_a_deplacer = path + "\\" + file
    shutil.move(file_a_deplacer , ".")
