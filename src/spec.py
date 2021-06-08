"""
 한국 버스 세트(Korean Bus Set)
 * https://github.com/KoreanGRF/KoreanBusSet
"""

# Define a dictionary
vehicleList = {}

#                                                     speed1  cost    running_cost  capacity loading_speed power   weight  introduction
vehicleList['HYUNDAI_SUPER_AEROCITY_LF']            = 100,    10,     10,           65,      10,           231,    12,     (2008, 1, 1)
vehicleList['DAEWOO_NEW_BS110_LF']                  = 100,    10,     10,           65,      10,           228,    12,     (2012, 1, 1)
vehicleList['LEGACY_BUS']                           = 100,    10,     10,           50,      10,           261,    30,     (1980, 1, 1)


# Generates spec.pnml (Do not modified this below!)
content = ""
for _name in vehicleList:
  if vehicleList[_name][0] is not None:
    content += "#define var_" + _name + "_SPEED " + str(vehicleList[_name][0]) + "\n"
  if vehicleList[_name][1] is not None:
    content += "#define var_" + _name + "_COST " + str(vehicleList[_name][1]) + "\n"
  if vehicleList[_name][2] is not None:
    content += "#define var_" + _name + "_RUNNINGCOST " + str(vehicleList[_name][2]) + "\n"
  if vehicleList[_name][3] is not None:
    content += "#define var_" + _name + "_CAPACITY " + str(vehicleList[_name][3]) + "\n"
  if vehicleList[_name][4] is not None:
    content += "#define var_" + _name + "_LOADINGSPEED " + str(vehicleList[_name][4]) + "\n"
  if vehicleList[_name][5] is not None:
    content += "#define var_" + _name + "_POWER " + str(vehicleList[_name][5]) + "\n"
  if vehicleList[_name][6] is not None:
    content += "#define var_" + _name + "_WEIGHT " + str(vehicleList[_name][6]) + "\n"
  if vehicleList[_name][7] is not None:
    content += "#define var_" + _name + "_INTRODUCTION date" + str(vehicleList[_name][7]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
