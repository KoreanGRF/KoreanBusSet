"""
 한국 버스 세트(Korean Bus Set)
 * https://github.com/KoreanGRF/KoreanBusSet
"""

# Define a dictionary
vehicleList = {}

#                                                     speed1  cost    running_cost  capacity loading_speed power   weight  introduction
vehicleList['HYUNDAI_AEROCITY']                     = 100,    10,     10,           65,      10,           206,    12,     (1991, 1, 1)
vehicleList['HYUNDAI_GREENCITY']                    = 100,    10,     10,           48,      10,           206,    12,     (2002, 1, 1)
vehicleList['HYUNDAI_SUPER_AEROCITY_LF']            = 100,    10,     10,           65,      10,           231,    12,     (2008, 1, 1)
vehicleList['HYUNDAI_UNIVERSE']                     = 150,    10,     10,           48,      10,           517,    15,     (2006, 1, 1)
vehicleList['HYUNDAI_COUNTY_LONG']                  = 104,    10,     10,           21,      5,            125,     5,     (1998, 1, 1)
vehicleList['HYUNDAI_COUNTY_XLONG']                 = 104,    10,     10,           23,      5,            125,     5,     (1998, 1, 1)
vehicleList['HYUNDAI_ELECCITY']                     = 100,    10,     10,           49,      5,            240,    12,     (2017, 1, 1)
vehicleList['HYUNDAI_ELECCITY_ARTICULATED']         =  80,    20,     20,           42,      5,            240,    18,     (2018, 1, 1)
vehicleList['HYUNDAI_ELECCITY_DOUBLE_DECKER']       = 100,    15,     15,           70,      10,           240,    22,     (2019, 1, 1)
vehicleList['DAEWOO_BS090']                         = 100,    10,     10,           48,      10,           220,     9,     (2002, 1, 1)
vehicleList['DAEWOO_NEW_BS106']                     = 100,    10,     10,           55,      10,           228,    12,     (2012, 1, 1)
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
