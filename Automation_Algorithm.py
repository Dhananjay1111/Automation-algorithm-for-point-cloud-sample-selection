# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#                       0=================================0
#                       |      Automation Algorithm       |
#                       0=================================0

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#
#                               Dhananjay Umalkar
#
# ----------------------------------------------------------------------------------------------------------------------
import os
import time
import laspy
import shutil
import random
from datetime import timedelta
import matplotlib.pyplot as plt
# ----------------------------------------------------------------------------------------------------------------------

Method = input(str("Enter the sampling method : "))
start_time = time.monotonic()

# ----------------------------------------------------------------------------------------------------------------------
Time = 1
# ----------------------------------------------------------------------------------------------------------------------
#
#           Semantic Classes
#       \***********************/
#
Water = 9
Other = 26
Ground = 2
Building = 6
Vegetation = 1
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#           0=================================0
#           |             Random              |
#           0=================================0

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

if Method == "Random":
    # Prompting user to enter number of files to select randomly along with directory
    source = input("Enter the Source Directory : ")

    # change to the data directory
    os.chdir(source)

    folder_name = "Random_samples"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    no_of_files = int(input("Enter The Number of Files To Select : "))

    print("%" * 25 + "{ Details Of Transfer }" + "%" * 25)

    # Using for loop to randomly choose multiple files
    for i in range(no_of_files):
        # Variable random_file stores the name of the random file chosen
        random_file = random.choice(os.listdir(source))
        print("%d} %s" % (i + 1, random_file))
        source_file = "%s\%s" % (source, random_file)
        destination = os.path.join(source, folder_name)
        # "shutil.move" function moves file from one directory to another
        shutil.copy(source_file, destination)

    print("\n\n" + "$" * 33 + "[ Files Moved Successfully ]" + "$" * 33)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#           0=================================0
#           |       Statistical sampling      |
#           |         Threshold Filter        |
#           0=================================0

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

elif Method == "Statistical":
    print("Statistical using threshold Filter")

    # ------------------------------------------------------------------------------------------------------------------
    # Source directory
    dataDirectory_las = input("Las files directory : ")

    # change to the data directory
    os.chdir(dataDirectory_las)
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Empty lists
    #       \*****************/
    #
    water = []
    ground = []
    ground_other = []
    ground_water = []
    ground_building = []
    vegetation_ground = []
    All_classes_present = []
    vegetation_ground_other = []
    vegetation_ground_water = []
    vegetation_ground_building = []
    vegetation_ground_water_other = []
    vegetation_ground_building_water = []
    vegetation_ground_building_other = []

    # ------------------------------------------------------------------------------------------------------------------
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".las"):
            # ----------------------------------------------------------------------------------------------------------
            las = laspy.read(file)
            class_label = las.classification
            # ----------------------------------------------------------------------------------------------------------
            frequency = {}
            frequency_class = []
            classes_available = []
            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Calculation
            #       \***************************/
            #
            def CountFrequency(my_list):
                # Creating an empty dictionary
                for item in my_list:
                    if (item in frequency):
                        frequency[item] += 1
                    else:
                        frequency[item] = 1

                for key, value in frequency.items():
                    classes_available.append(key)
                    frequency_class.append(value)
                    print("% d : % d" % (key, value))

            # ----------------------------------------------------------------------------------------------------------

            if __name__ == "__main__":
                class_label = sorted(class_label)
            CountFrequency(class_label)

            # ----------------------------------------------------------------------------------------------------------
            #
            #             Filters
            #       \*****************/
            #
            labels = 0
            if len(classes_available) == 5:
                if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Building] > 6000 and \
                        frequency[Water] > 1000 and frequency[Other] > 1000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_classes_present.append(file)
            if len(classes_available) == 4:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building and classes_available[3] == Water:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Building] > 6000 and\
                            frequency[Water] > 1000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        vegetation_ground_building_water.append(file)
            if len(classes_available) == 4:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building and classes_available[3] == Other:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Building] > 6000 and\
                            frequency[Other] > 1000:
                        labels = ["Vegetation", "Ground", "Building", "other"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#FFDFDD']
                        vegetation_ground_building_other.append(file)
            if len(classes_available) == 4:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Water and classes_available[3] == Other:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Water] > 1000 and\
                            frequency[Other] > 1000:
                        labels = ["Vegetation", "Ground", "Water", "Other"]
                        color = ['#00FF00', '#DC381F','#00FFFF', '#FFDFDD']
                        vegetation_ground_water_other.append(file)
            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Building] > 6000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        vegetation_ground_building.append(file)
            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Other:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Other] > 1000:
                        labels = ["Vegetation", "Ground", "Other"]
                        color = ['#00FF00', '#DC381F', '#FFDFDD']
                        vegetation_ground_other.append(file)
            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Water:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000 and frequency[Water] > 1000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        vegetation_ground_water.append(file)
            if len(classes_available) == 2:
                if classes_available[0] == Vegetation and classes_available[1] == Ground:
                    if frequency[Vegetation] > 6000 and frequency[Ground] > 6000:
                        labels = ["Vegetation", "Ground"]
                        color = ['#00FF00', '#DC381F']
                        vegetation_ground.append(file)
            if len(classes_available) == 2:
                if classes_available[0] == Ground and classes_available[1] == Building:
                    if frequency[Ground] > 6000 and frequency[Building] > 6000:
                        labels = ["Ground", "Building"]
                        color = ['#DC381F', '#504A4B']
                        ground_building.append(file)
            if len(classes_available) == 2:
                if classes_available[0] == Ground and classes_available[1] == Other:
                    if frequency[Ground] > 6000 and frequency[Other] > 1000:
                        labels = ["Ground", "Other"]
                        color = ['#DC381F', '#FFDFDD']
                        ground_other.append(file)
            if len(classes_available) == 2:
                if classes_available[0] == Ground and classes_available[1] == Water:
                    if frequency[Ground] > 6000 and frequency[Water] > 1000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        ground_water.append(file)
            if len(classes_available) == 1:
                if classes_available[0] == Ground:
                    labels = ["Ground"]
                    color = ['#DC381F']
                    ground.append(file)
            if len(classes_available) == 1:
                if classes_available[0] == Water:
                    labels = ["Water"]
                    color = ['#00FFFF']
                    water.append(file)

            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Visaulization
            #       \*****************************/
            #
            if labels == 0:
                pass
            else:
                plt.title(" Bar Graph ")  # add title
                plt.xlabel("classes")  # label for x- axis
                plt.ylabel("Frequency per class")  # label for y- axis
                # Change the bar colors here
                plt.bar(labels, frequency_class,
                        color=color, edgecolor='red')
                plt.legend(loc="upper right")
                plt.show(block=False)
                plt.pause(Time)
                plt.close()

            # ----------------------------------------------------------------------------------------------------------

        print("\n")
    # ------------------------------------------------------------------------------------------------------------------

    print("Ground-", ground)
    print("Water-", water)
    print("Ground Water-", ground_water)
    print("Ground Other-", ground_other)
    print("Ground Building-", ground_building)
    print("Vegetation and ground-", vegetation_ground)
    print("Vegetation Ground Other-", vegetation_ground_other)
    print("Vegetation Ground Water-", vegetation_ground_water)
    print("All the classes are present-", All_classes_present)
    print("Vegetation Ground Building-", vegetation_ground_building)
    print("Vegetation Ground Water Other-", vegetation_ground_water_other)
    print("Vegetation Ground Building Water-", vegetation_ground_building_water)
    print("Vegetation Ground Building Other-", vegetation_ground_building_other)

    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Sorting files into folders
    #       \********************************/
    #
    for file in os.listdir():
        # Check whether file is in Las format or not
        if file.endswith(".las"):
            if file in All_classes_present:
                folder_name = "01_All classes present"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_building_water:
                folder_name = "02_Vegetation_Ground_Building_Water"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_building_other:
                folder_name = "03_Vegetation_Ground_Building_Other"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_water_other:
                folder_name = "04_Vegetation_Ground_Water_Other"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_building:
                folder_name = "05_Vegetation_Ground_Building"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground:
                folder_name = "06_Vegetation_Ground"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in ground_building:
                folder_name = "07_Ground_Building"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_other:
                folder_name = "08_Vegetation_Ground_Other"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in vegetation_ground_water:
                folder_name = "09_Vegetation_Ground_Water"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in ground_other:
                folder_name = "10_Ground_Other"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in ground_water:
                folder_name = "11_Ground_Water"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in ground:
                folder_name = "12_Ground"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)
            elif file in water:
                folder_name = "13_water"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)

    # ------------------------------------------------------------------------------------------------------------------

    print("\n\n" + "*" * 33 + "[ Sample Folders For Training Are Created Successfully ]" + "*" * 33)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#           0=================================0
#           |             Fusion              |
#           0=================================0

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

elif Method == "Fusion":
    # ------------------------------------------------------------------------------------------------------------------
    # Source directory
    dataDirectory_las = input("Las files directory : ")

    Amount = int(input("Number of files required : "))
    #Amount = 200

    # Amount_G_W = input(int("Number of files required :"))
    Amount_G_W = int((40/100)*Amount)

    # change to the data directory
    os.chdir(dataDirectory_las)
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Empty lists
    #       \*****************/
    #
    Master = []

    All_C_01 = []
    All_C_02 = []
    All_C_03 = []
    All_C_04 = []
    All_C_05 = []
    All_C_06 = []
    All_C_07 = []
    All_C_08 = []
    All_C_09 = []
    All_C_10 = []

    V_G_B_W_01 = []
    V_G_B_W_02 = []
    V_G_B_W_03 = []
    V_G_B_W_04 = []
    V_G_B_W_05 = []
    V_G_B_W_06 = []
    V_G_B_W_07 = []
    V_G_B_W_08 = []
    V_G_B_W_09 = []
    V_G_B_W_10 = []
    V_G_B_W_11 = []

    V_G_B_01 = []
    V_G_B_02 = []
    V_G_B_03 = []
    V_G_B_04 = []
    V_G_B_05 = []
    V_G_B_06 = []
    V_G_B_07 = []
    V_G_B_08 = []
    V_G_B_09 = []
    V_G_B_10 = []
    V_G_B_11 = []

    Master_G_W = []

    G_W_01 = []
    G_W_02 = []
    G_W_03 = []
    G_W_04 = []
    G_W_05 = []
    G_W_06 = []
    G_W_07 = []
    G_W_08 = []
    G_W_09 = []
    G_W_10 = []
    G_W_11 = []

    V_G_W_01 = []
    V_G_W_02 = []
    V_G_W_03 = []
    V_G_W_04 = []
    V_G_W_05 = []
    V_G_W_06 = []
    V_G_W_07 = []
    V_G_W_08 = []
    V_G_W_09 = []
    V_G_W_10 = []
    V_G_W_11 = []

    # ------------------------------------------------------------------------------------------------------------------

    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".las"):
            # ----------------------------------------------------------------------------------------------------------
            las = laspy.read(file)
            class_label = las.classification
            # ----------------------------------------------------------------------------------------------------------
            frequency = {}
            frequency_class = []
            classes_available = []
            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Calculation
            #       \***************************/
            #
            def CountFrequency(my_list):
                # Creating an empty dictionary
                for item in my_list:
                    if (item in frequency):
                        frequency[item] += 1
                    else:
                        frequency[item] = 1

                for key, value in frequency.items():
                    classes_available.append(key)
                    frequency_class.append(value)
                    print("% d : % d" % (key, value))

            # ----------------------------------------------------------------------------------------------------------

            if __name__ == "__main__":
                class_label = sorted(class_label)
            CountFrequency(class_label)

            # ----------------------------------------------------------------------------------------------------------
            #
            #             Filters
            #       \*****************/
            #
            labels = 0
            if len(classes_available) == 5:
                if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000 and\
                        frequency[Water] > 35000 and frequency[Other] > 20000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_01.append(file)
                elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000 and\
                        frequency[Water] > 25000 and frequency[Other] > 15000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_02.append(file)
                elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000 and\
                        frequency[Water] > 20000 and frequency[Other] > 12000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_03.append(file)
                elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000 and\
                        frequency[Water] > 15000 and frequency[Other] > 10000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_04.append(file)
                elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000 and\
                        frequency[Water] > 10000 and frequency[Other] > 7000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_05.append(file)
                elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000 and\
                        frequency[Water] > 7000 and frequency[Other] > 5000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_06.append(file)
                elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000 and\
                        frequency[Water] > 5000 and frequency[Other] > 2500:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_07.append(file)
                elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000 and\
                        frequency[Water] > 2000 and frequency[Other] > 1000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_08.append(file)
                elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000 and\
                        frequency[Water] > 1000 and frequency[Other] > 500:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_09.append(file)
                elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000 and\
                        frequency[Water] > 500 and frequency[Other] > 0000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_10.append(file)

            if len(classes_available) == 4:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building and classes_available[3] == Water:
                    if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000 and\
                            frequency[Water] > 35000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_01.append(file)
                    elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000 and\
                            frequency[Water] > 25000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_02.append(file)
                    elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000 and\
                            frequency[Water] > 20000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_03.append(file)
                    elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000 and\
                            frequency[Water] > 15000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_04.append(file)
                    elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000 and\
                            frequency[Water] > 10000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_05.append(file)
                    elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000 and\
                            frequency[Water] > 7000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_06.append(file)
                    elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000 and\
                            frequency[Water] > 5000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_07.append(file)
                    elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000 and\
                            frequency[Water] > 2000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_08.append(file)
                    elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000 and\
                            frequency[Water] > 1000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_09.append(file)
                    elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000 and\
                            frequency[Water] > 500:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_10.append(file)
                    elif frequency[Vegetation] > 1000 and frequency[Ground] > 500 and frequency[Building] > 5000 and\
                            frequency[Water] > 000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_11.append(file)

            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building:
                    if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_01.append(file)
                    elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_02.append(file)
                    elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_03.append(file)
                    elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_04.append(file)
                    elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_05.append(file)
                    elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_06.append(file)
                    elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_07.append(file)
                    elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_08.append(file)
                    elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_09.append(file)
                    elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_10.append(file)
                    elif frequency[Vegetation] > 1000 and frequency[Ground] > 500 and frequency[Building] > 5000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_11.append(file)

            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Water:
                    if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Water] > 35000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_01.append(file)
                    elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Water] > 25000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_02.append(file)
                    elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Water] > 20000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_03.append(file)
                    elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Water] > 15000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_04.append(file)
                    elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Water] > 10000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_05.append(file)
                    elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Water] > 7000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_06.append(file)
                    elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Water] > 5000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_07.append(file)
                    elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Water] > 2000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_08.append(file)
                    elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Water] > 1000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_09.append(file)
                    elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Water] > 500:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_10.append(file)
                    elif frequency[Vegetation] > 1000 and frequency[Ground] > 500 and frequency[Water] > 000:
                        labels = ["Vegetation", "Ground", "Water"]
                        color = ['#00FF00', '#DC381F', '#00FFFF']
                        V_G_W_11.append(file)

            if len(classes_available) == 2:
                if classes_available[0] == Ground and classes_available[1] == Water:
                    if frequency[Water] > 35000 and frequency[Ground] > 70000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_01.append(file)
                    elif frequency[Water] > 25000 and frequency[Ground] > 50000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_02.append(file)
                    elif frequency[Water] > 15000 and frequency[Ground] > 40000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_03.append(file)
                    elif frequency[Water] > 10000 and frequency[Ground] > 30000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_04.append(file)
                    elif frequency[Water] > 7000 and frequency[Ground] > 20000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_05.append(file)
                    elif frequency[Water] > 5000 and frequency[Ground] > 10000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_06.append(file)
                    elif frequency[Water] > 2500 and frequency[Ground] > 7000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_07.append(file)
                    elif frequency[Water] > 1500 and frequency[Ground] > 5000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_08.append(file)
                    elif frequency[Water] > 1000 and frequency[Ground] > 2500:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_09.append(file)
                    elif frequency[Water] > 500 and frequency[Ground] > 1000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_10.append(file)
                    elif frequency[Water] > 000 and frequency[Ground] > 0000:
                        labels = ["Ground", "Water"]
                        color = ['#DC381F', '#00FFFF']
                        G_W_11.append(file)

            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Visualization
            #       \*****************************/
            #
            if labels == 0:
                pass
            else:
                plt.title(" Bar Graph ")  # add title
                plt.xlabel("classes")  # label for x- axis
                plt.ylabel("Frequency per class")  # label for y- axis
                # Change the bar colors here
                plt.bar(labels, frequency_class,
                        color=color, edgecolor='red')
                plt.legend(loc="upper right")
                plt.show(block=False)
                plt.pause(Time)
                plt.close()

            # ----------------------------------------------------------------------------------------------------------

        print("\n")
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Cascade Filter for Master Folder
    #       \**************************************/
    #
    if len(Master) < Amount:
        for i in range(len(All_C_01)):
            Master.append(All_C_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_02)):
            Master.append(All_C_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_03)):
            Master.append(All_C_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_04)):
            Master.append(All_C_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_05)):
            Master.append(All_C_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_06)):
            Master.append(All_C_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_07)):
            Master.append(All_C_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_08)):
            Master.append(All_C_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_09)):
            Master.append(All_C_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_10)):
            Master.append(All_C_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_01)):
            Master.append(V_G_B_W_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_02)):
            Master.append(V_G_B_W_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_03)):
            Master.append(V_G_B_W_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_04)):
            Master.append(V_G_B_W_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_05)):
            Master.append(V_G_B_W_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_06)):
            Master.append(V_G_B_W_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_07)):
            Master.append(V_G_B_W_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_08)):
            Master.append(V_G_B_W_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_09)):
            Master.append(V_G_B_W_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_10)):
            Master.append(V_G_B_W_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_11)):
            Master.append(V_G_B_W_11[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_01)):
            Master.append(V_G_B_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_02)):
            Master.append(V_G_B_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_03)):
            Master.append(V_G_B_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_04)):
            Master.append(V_G_B_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_05)):
            Master.append(V_G_B_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_06)):
            Master.append(V_G_B_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_07)):
            Master.append(V_G_B_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_08)):
            Master.append(V_G_B_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_09)):
            Master.append(V_G_B_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_10)):
            Master.append(V_G_B_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_11)):
            Master.append(V_G_B_11[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_01)):
            Master_G_W.append(V_G_W_01[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_02)):
            Master_G_W.append(V_G_W_02[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_03)):
            Master_G_W.append(V_G_W_03[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_04)):
            Master_G_W.append(V_G_W_04[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_05)):
            Master_G_W.append(V_G_W_05[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_06)):
            Master_G_W.append(V_G_W_06[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_07)):
            Master_G_W.append(V_G_W_07[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_08)):
            Master_G_W.append(V_G_W_08[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_09)):
            Master_G_W.append(V_G_W_09[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_10)):
            Master_G_W.append(V_G_W_10[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(V_G_W_11)):
            Master_G_W.append(V_G_W_11[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_01)):
            Master_G_W.append(G_W_01[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_02)):
            Master_G_W.append(G_W_02[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_03)):
            Master_G_W.append(G_W_03[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_04)):
            Master_G_W.append(G_W_04[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_05)):
            Master_G_W.append(G_W_05[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_06)):
            Master_G_W.append(G_W_06[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_07)):
            Master_G_W.append(G_W_07[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_08)):
            Master_G_W.append(G_W_08[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_09)):
            Master_G_W.append(G_W_09[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_10)):
            Master_G_W.append(G_W_10[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    if len(Master_G_W) < Amount_G_W:
        for i in range(len(G_W_11)):
            Master_G_W.append(G_W_11[i])
            if len(Master_G_W) == Amount_G_W:
                break
            else:
                continue

    # ------------------------------------------------------------------------------------------------------------------
    print(Master)
    print(Master_G_W)
    Master_00 = Master + Master_G_W
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Sorting files into folders
    #       \********************************/
    #
    for file in os.listdir():
        # Check whether file is in Las format or not
        if file.endswith(".las"):
            if file in Master_00:
                folder_name = "00_Master"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)

    # ------------------------------------------------------------------------------------------------------------------

    print("\n\n" + "*" * 33 + "[ Sample Folder For Training Is Created Successfully ]" + "*" * 33)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#           0=================================0
#           |             Cascade             |
#           0=================================0

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

elif Method == "Cascade":
    # ------------------------------------------------------------------------------------------------------------------
    # Source directory
    dataDirectory_las = input("Las files directory : ")

    Amount = int(input("Number of files required :"))
    #Amount = 200

    # change to the data directory
    os.chdir(dataDirectory_las)
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Empty lists
    #       \*****************/
    #
    Master = []

    All_C_01 = []
    All_C_02 = []
    All_C_03 = []
    All_C_04 = []
    All_C_05 = []
    All_C_06 = []
    All_C_07 = []
    All_C_08 = []
    All_C_09 = []
    All_C_10 = []

    V_G_B_W_01 = []
    V_G_B_W_02 = []
    V_G_B_W_03 = []
    V_G_B_W_04 = []
    V_G_B_W_05 = []
    V_G_B_W_06 = []
    V_G_B_W_07 = []
    V_G_B_W_08 = []
    V_G_B_W_09 = []
    V_G_B_W_10 = []
    V_G_B_W_11 = []

    V_G_B_01 = []
    V_G_B_02 = []
    V_G_B_03 = []
    V_G_B_04 = []
    V_G_B_05 = []
    V_G_B_06 = []
    V_G_B_07 = []
    V_G_B_08 = []
    V_G_B_09 = []
    V_G_B_10 = []
    V_G_B_11 = []

    # ------------------------------------------------------------------------------------------------------------------

    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".las"):
            # ----------------------------------------------------------------------------------------------------------
            las = laspy.read(file)
            class_label = las.classification
            # ----------------------------------------------------------------------------------------------------------
            frequency = {}
            frequency_class = []
            classes_available = []
            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Calculation
            #       \***************************/
            #
            def CountFrequency(my_list):
                # Creating an empty dictionary
                for item in my_list:
                    if (item in frequency):
                        frequency[item] += 1
                    else:
                        frequency[item] = 1

                for key, value in frequency.items():
                    classes_available.append(key)
                    frequency_class.append(value)
                    print("% d : % d" % (key, value))

            # ----------------------------------------------------------------------------------------------------------

            if __name__ == "__main__":
                class_label = sorted(class_label)
            CountFrequency(class_label)

            # ----------------------------------------------------------------------------------------------------------
            #
            #             Filters
            #       \*****************/
            #
            labels = 0
            if len(classes_available) == 5:
                if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000 and \
                        frequency[Water] > 35000 and frequency[Other] > 20000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_01.append(file)
                elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000 and \
                        frequency[Water] > 25000 and frequency[Other] > 15000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_02.append(file)
                elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000 and \
                        frequency[Water] > 20000 and frequency[Other] > 12000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_03.append(file)
                elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000 and \
                        frequency[Water] > 15000 and frequency[Other] > 10000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_04.append(file)
                elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000 and \
                        frequency[Water] > 10000 and frequency[Other] > 7000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_05.append(file)
                elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000 and \
                        frequency[Water] > 7000 and frequency[Other] > 5000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_06.append(file)
                elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000 and \
                        frequency[Water] > 5000 and frequency[Other] > 2500:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_07.append(file)
                elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000 and \
                        frequency[Water] > 2000 and frequency[Other] > 1000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_08.append(file)
                elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000 and \
                        frequency[Water] > 1000 and frequency[Other] > 500:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_09.append(file)
                elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000 and \
                        frequency[Water] > 500 and frequency[Other] > 0000:
                    labels = ["Vegetation", "Ground", "Building", "Water", "Other"]
                    color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF', '#FFDFDD']
                    All_C_10.append(file)

            if len(classes_available) == 4:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building and classes_available[3] == Water:
                    if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000 and \
                            frequency[Water] > 35000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_01.append(file)
                    elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000 and \
                            frequency[Water] > 25000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_02.append(file)
                    elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000 and \
                            frequency[Water] > 20000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_03.append(file)
                    elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000 and \
                            frequency[Water] > 15000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_04.append(file)
                    elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000 and \
                            frequency[Water] > 10000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_05.append(file)
                    elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000 and \
                            frequency[Water] > 7000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_06.append(file)
                    elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000 and \
                            frequency[Water] > 5000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_07.append(file)
                    elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000 and \
                            frequency[Water] > 2000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_08.append(file)
                    elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000 and \
                            frequency[Water] > 1000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_09.append(file)
                    elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000 and \
                            frequency[Water] > 500:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_10.append(file)
                    elif frequency[Vegetation] > 1000 and frequency[Ground] > 500 and frequency[Building] > 5000 and \
                            frequency[Water] > 000:
                        labels = ["Vegetation", "Ground", "Building", "Water"]
                        color = ['#00FF00', '#DC381F', '#504A4B', '#00FFFF']
                        V_G_B_W_11.append(file)

            if len(classes_available) == 3:
                if classes_available[0] == Vegetation and classes_available[1] == Ground \
                        and classes_available[2] == Building:
                    if frequency[Vegetation] > 50000 and frequency[Ground] > 70000 and frequency[Building] > 70000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_01.append(file)
                    elif frequency[Vegetation] > 40000 and frequency[Ground] > 50000 and frequency[Building] > 50000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_02.append(file)
                    elif frequency[Vegetation] > 35000 and frequency[Ground] > 40000 and frequency[Building] > 30000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_03.append(file)
                    elif frequency[Vegetation] > 30000 and frequency[Ground] > 30000 and frequency[Building] > 20000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_04.append(file)
                    elif frequency[Vegetation] > 25000 and frequency[Ground] > 20000 and frequency[Building] > 15000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_05.append(file)
                    elif frequency[Vegetation] > 15000 and frequency[Ground] > 10000 and frequency[Building] > 10000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_06.append(file)
                    elif frequency[Vegetation] > 10000 and frequency[Ground] > 7000 and frequency[Building] > 7000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_07.append(file)
                    elif frequency[Vegetation] > 7000 and frequency[Ground] > 5000 and frequency[Building] > 5000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_08.append(file)
                    elif frequency[Vegetation] > 5000 and frequency[Ground] > 2500 and frequency[Building] > 2000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_09.append(file)
                    elif frequency[Vegetation] > 3000 and frequency[Ground] > 1000 and frequency[Building] > 1000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_10.append(file)
                    elif frequency[Vegetation] > 1000 and frequency[Ground] > 500 and frequency[Building] > 5000:
                        labels = ["Vegetation", "Ground", "Building"]
                        color = ['#00FF00', '#DC381F', '#504A4B']
                        V_G_B_11.append(file)

            # ----------------------------------------------------------------------------------------------------------
            #
            #           Frequency Visaulization
            #       \*****************************/
            #
            if labels == 0:
                pass
            else:
                plt.title(" Bar Graph ")  # add title
                plt.xlabel("classes")  # label for x- axis
                plt.ylabel("Frequency per class")  # label for y- axis
                # Change the bar colors here
                plt.bar(labels, frequency_class,
                        color=color, edgecolor='red')
                plt.legend(loc="upper right")
                plt.show(block=False)
                plt.pause(Time)
                plt.close()

            # ----------------------------------------------------------------------------------------------------------

        print("\n")
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Cascade Filter for Master Folder
    #       \**************************************/
    #
    if len(Master) < Amount:
        for i in range(len(All_C_01)):
            Master.append(All_C_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_02)):
            Master.append(All_C_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_03)):
            Master.append(All_C_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_04)):
            Master.append(All_C_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_05)):
            Master.append(All_C_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_06)):
            Master.append(All_C_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_07)):
            Master.append(All_C_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_08)):
            Master.append(All_C_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_09)):
            Master.append(All_C_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(All_C_10)):
            Master.append(All_C_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_01)):
            Master.append(V_G_B_W_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_02)):
            Master.append(V_G_B_W_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_03)):
            Master.append(V_G_B_W_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_04)):
            Master.append(V_G_B_W_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_05)):
            Master.append(V_G_B_W_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_06)):
            Master.append(V_G_B_W_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_07)):
            Master.append(V_G_B_W_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_08)):
            Master.append(V_G_B_W_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_09)):
            Master.append(V_G_B_W_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_10)):
            Master.append(V_G_B_W_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_W_11)):
            Master.append(V_G_B_W_11[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_01)):
            Master.append(V_G_B_01[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_02)):
            Master.append(V_G_B_02[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_03)):
            Master.append(V_G_B_03[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_04)):
            Master.append(V_G_B_04[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_05)):
            Master.append(V_G_B_05[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_06)):
            Master.append(V_G_B_06[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_07)):
            Master.append(V_G_B_07[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_08)):
            Master.append(V_G_B_08[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_09)):
            Master.append(V_G_B_09[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_10)):
            Master.append(V_G_B_10[i])
            if len(Master) == Amount:
                break
            else:
                continue

    if len(Master) < Amount:
        for i in range(len(V_G_B_11)):
            Master.append(V_G_B_11[i])
            if len(Master) == Amount:
                break
            else:
                continue

    # ------------------------------------------------------------------------------------------------------------------
    print(Master)
    # ------------------------------------------------------------------------------------------------------------------
    #
    #           Sorting files into folders
    #       \********************************/
    #
    for file in os.listdir():
        # Check whether file is in Las format or not
        if file.endswith(".las"):
            if file in Master:
                folder_name = "00_Master"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                source_file = "%s\%s" % (dataDirectory_las, file)
                destination = os.path.join(dataDirectory_las, folder_name)
                shutil.copy(source_file, destination)

    # ------------------------------------------------------------------------------------------------------------------

    print("\n\n" + "*" * 33 + "[ Sample Folder For Training is Created Successfully ]" + "*" * 33)

    # ------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
end_time = time.monotonic()
print("\n\n")
print("Time taken for sample selection-", timedelta(seconds=end_time - start_time))
# ----------------------------------------------------------------------------------------------------------------------