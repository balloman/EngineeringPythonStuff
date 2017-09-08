def plane_ride_cost(city):
  d = {"Charlotte":183, "Tampa":220, "Pittsburgh":222, "Los Angeles": 475}
  return d[city]

print plane_ride_cost("Charlotte")