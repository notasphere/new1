import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


"""
def main():
    image_path = os.path.join(os.getcwd(), 'annotations')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('raccoon_labels.csv', index=None)
    print('Successfully converted xml to csv.')
"""

def main():

    d1 = os.listdir("/home/david/Desktop/dhOBJ/aQ")
    print(d1)
    d2 = 'bfile.txt' in d1
    print(d2)
    d2 = 'a1.txt' in d1
    print(d2)



    # for directory in ['a*.*']:
    #     print(directory)

"""
    #for directory in ['aQ', 'bQ']:
        #
        # #image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory))
        # image_path = os.path.join(os.getcwd(), '{}/*.txt'.format(directory))
        #
        # #xml_df = xml_to_csv(image_path)
        # #xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        # print('directory ', directory)
        # print('image_path ', image_path)
"""


main()

