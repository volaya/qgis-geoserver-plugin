# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#

from bridgestyle.qgis import layerStyleAsSld

def getGsCompatibleSld(layer):
    sld, icons, warnings = layerStyleAsSld(layer)
    return sld, icons

def getGeomTypeFromSld(sld):
    if "PointSymbolizer" in sld:
        return "Point"
    elif "LineSymbolizer" in sld:
        return "LineString"
    else:
        return "Polygon"
