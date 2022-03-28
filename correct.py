# This file needs correcting since SuttonSignWritingOneD doesn't follow naming conventions.
# The names include whitespaces and those are not welcome in various platforms such as VOLT


import sys, math
import xml.etree.ElementTree as ET


# Todo need to fix this file


class FontCorrector:
    def __init__(self, ttx_font, k=0.09):
        self.k = k  # K is an argument that allows changing the size of the glyphs
        self.ttx = ttx_font

    # This function checks if a given string in a name of number glyph in O(1)
    @staticmethod
    def is_number_glyf(name):
        if 'SW2' in name or 'SW3' in name or 'SW4' in name or 'SW5' in name or 'SW6' in name or 'SW7' in name:
            return True
        else:
            return False

    def create_correct_ttx(self):
        with open(self.ttx, "r") as f:
            txt = f.read()
            # Correcting the names
            txt = txt.replace('"SW ', '"SW')
            # Setting the width of the boxes to 500
            txt = txt.replace('name="SWM" width="0"', 'name="SWM" width="500"')
            m_svg = open("Mbox-svg.txt", "r")
            m_svg_replace = open("Mbox-svg-replace.txt", "r")
            # Making the MBox into a 500x500 svg
            txt = txt.replace(m_svg.read(), m_svg_replace.read())

        # Changing the TTX file by parsing and modifying it
        root = ET.XML(txt)
        head = root.findall('glyf')
        for glyf in head[0].findall('TTGlyph'):
            if self.is_number_glyf(glyf.attrib["name"]):  # If it is a number glyph then we remove all the contours
                for contour in glyf.findall("contour"):
                    glyf.remove(contour)
            elif glyf.attrib["name"] == "SWM" or glyf.attrib["name"] == ".notdef" or glyf.attrib["name"] == ".null" or \
                    glyf.attrib["name"] == "nonmarkingreturn":
                continue
            elif glyf.attrib["name"] == "S33100" or glyf.attrib["name"] == "S20310" or glyf.attrib["name"] == "S26b02":
                xMin = float(glyf.attrib['xMin'])
                xMax = float(glyf.attrib['xMax'])
                yMin = float(glyf.attrib['yMin'])
                yMax = float(glyf.attrib['yMax'])
                dx = float((xMax - xMin) / 2)
                dy = float((yMax - yMin) / 2)
                glyf.attrib['xMin'] = str((xMin - dx) * self.K)
                glyf.attrib['xMax'] = str((xMax - dx) * self.K)
                glyf.attrib['yMin'] = str((yMin - dy) * self.K)
                glyf.attrib['yMax'] = str((yMax - dy) * self.K)
                for contour in glyf.findall("contour"):
                    for point in contour.findall("pt"):
                        point.attrib['x'] = str((float(point.attrib['x']) - dx) * self.K)
                        point.attrib['y'] = str((float(point.attrib['y']) - dy) * self.K)
        # Setting the width of all the glyphs to 0
        for mtx in root.findall('hmtx')[0]:
            if mtx.attrib["name"] == "SWM":
                mtx.attrib['width'] = "500"
            else:
                mtx.attrib['width'] = "0"
        # Correcting the output xml file
        with open("artifacts/SuttonSignWritingTwoD.ttx", "wb") as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(ET.tostring(root))


corrector = FontCorrector(sys.argv[1])
corrector.create_correct_ttx()