import os

#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\The Big Bang Theory"
#fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\TBBT"
fullpath = "D:\\RESPALDO\\Desktop\\SERIES VIENDO AHORA\\The Big Bang Theory copia"


def make_directory(full_path):

    if os.path.exists(full_path):
        array = os.listdir(full_path)

        for j in array:
            for i in range(1, 25):
                if "S01" in j:
                    if i > 17:
                        break
                if "S02" in j or "S03" in j:
                    if i > 23:
                        break

                if i < 10:
                    new_path = os.path.join(full_path, j, "0"+str(i))
                else:
                    new_path = os.path.join(full_path, j, str(i))

                os.makedirs(new_path, exist_ok=True)

            if "S12" in j:
                new_path = os.path.join(full_path, j, str(25))
                os.makedirs(new_path, exist_ok=True)


def move_files_to_directory(full_path):
    array = os.listdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        newpath = os.listdir(pathh)

        for element in newpath:
            if os.path.isfile(os.path.join(pathh, element)):
                for j in range(1, 26):
                    if "E"+str(j).zfill(2) in element:
                        directory = os.path.join(pathh, str(j).zfill(2))
                        os.replace(os.path.join(pathh, element),
                                   os.path.join(directory, element))


def rename_files(full_path):
    array = os.listdir(full_path)

    for seasion in array:
        pathh = os.path.join(full_path, seasion)
        newpath = os.listdir(pathh)

        for element in newpath:
            if os.path.isdir(os.path.join(pathh, element)):
                pathhh = os.path.join(pathh, element)
                directorys = os.listdir(os.path.join(pathh, element))

                for file in directorys:
                    if file.endswith("mkv") or file.endswith("mp4"):
                        file_name = file
                        name, extmkvmp4 = os.path.splitext(file_name)

                    if file.endswith("srt"):
                        os.rename(os.path.join(pathhh, file),
                                  os.path.join(pathhh, 'zzzz.srt'))

                        os.rename(os.path.join(pathhh, 'zzzz.srt'),
                                  os.path.join(pathhh, name+'.srt'))


# make_directory(fullpath)
# move_files_to_directory(fullpath)
# rename_files(fullpath)
