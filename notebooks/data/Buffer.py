import arcpy

arcpy.env.workspace = r"C:\arcpy1\arcpy1\arcpy1.gdb"

arcpy.env.overwriteOutput = True

arcpy.JoinField_management(in_data=arcpy.GetParameterAsText(0), in_field="KATEGORI", join_table= "BufferDistance", join_field="KATEGORI")

arcpy.Buffer_analysis(in_features=arcpy.GetParameterAsText(0), out_feature_class="RoadBuffers",
                      buffer_distance_or_field="DISTANCE", dissolve_option="ALL")

fcList = arcpy.ListFeatureClasses()

bufferList = [arcpy.GetParameterAsText(1), arcpy.GetParameterAsText(2)]

unionList = []

for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(in_features=fc, out_feature_class=fc + "Buffers",
                              buffer_distance_or_field="1000 meters", dissolve_option="ALL")
        unionList.append(fc + "Buffers")

arcpy.Union_analysis(in_features=unionList, out_feature_class="WaterBuffers")

treatmentList = ["RoadBuffers", "WaterBuffers"]
arcpy.Union_analysis(treatmentList, arcpy.GetParameterAsText(3))