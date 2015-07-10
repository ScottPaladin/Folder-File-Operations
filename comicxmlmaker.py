import os, shutil, sys
from xml.etree.ElementTree import Element, SubElement, Comment, tostring


WORKDIR = "Pathname"
XMLFILENAME = "ComicInfo.xml"


def xmlindir(PATH):
    print("Working on directory: %s" % PATH)
    list = [ name for name in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, name)) ]
    print(len(list))
    print("Path Listed")
    for FILE in list:
##        FILE = FILE.decode('utf-8').encode('utf-8')
        temp_string = os.path.splitext(os.path.basename(FILE))[0]
        if "-" in temp_string:
            print("Filename: %s" % temp_string)
            temp_list = temp_string.split('-', 1)
            seg1 = temp_list[0]
            seg1 = seg1.rstrip()
            print("seg1: %s" % seg1)
            seg2 = temp_list[1]
            seg2 = seg2.lstrip()
            print("seg2: %s" % seg2)
            makexml(seg1, seg2, os.path.join(PATH,FILE))
        else:
            print("CANNOT SPLIT STRING FOR %s" % temp_string)

def makexml(artist, title, DIR):
    temp_string = title.rsplit(' ', 1)
    print(temp_string)
    if temp_string[-1].isdigit():
            print("Tempstring last is digit")
            title = temp_string[0].rstrip('0123456789=, ')
            top = Element('ComicInfo')
            series = SubElement(top, 'Series')
            series.text = title
            number = SubElement(top, 'Number')
            number.text = temp_string[-1]
            pencil = SubElement(top, 'Penciller')
            pencil.text = artist
            writer = SubElement(top, 'Writer')
            writer.text = artist
            xml = tostring(top)
            print(xml)
            print(DIR)
            XMLFILE = os.path.join(DIR, XMLFILENAME)
            f = open(XMLFILE, 'wb')
            f.write(xml)
    if not temp_string[-1].isdigit():
            print("Tempstring last is not digit")
            top = Element('ComicInfo')
            series = SubElement(top, 'Series')
            series.text = title
            pencil = SubElement(top, 'Penciller')
            pencil.text = artist
            writer = SubElement(top, 'Writer')
            writer.text = artist
            xml = tostring(top)
            print(xml)
            print(DIR)
            XMLFILE = os.path.join(DIR, XMLFILENAME)
            f = open(XMLFILE, 'wb')
            f.write(xml)
    

xmlindir(WORKDIR)

