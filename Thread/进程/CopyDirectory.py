import os
import multiprocessing

def copy_file(file_name, old_folder_name, new_folder_name):
    """cooy file"""
    print("from: %s to: %s file: %s " % (old_folder_name, new_folder_name, file_name))
    
    old_file = open(old_folder_name + "/" + file_name, "rb")
    content = old_file.read()
    old_file.close()
    new_file = open(new_folder_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()



def main():
    # 
    old_folder_name = input("input old folder name:")
    new_folder_name = old_folder_name + "_copy"
    try:
        os.mkdir(new_folder_name)
    except:
        pass
    file_names = os.listdir(old_folder_name)

    po = multiprocessing.Pool(5)

    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name,old_folder_name,new_folder_name))
    
    po.close()
    po.join()



if __name__ == "__main__":
    main()
