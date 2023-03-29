import pyopencl as cl

for platform in cl.get_platforms():
   print("Platform %s " %platform.name)
   print("  Vendor: %s " %platform.vendor)
   print("  Version: %s " %platform.version)
   for device in platform.get_devices():
      print("     Device %s " %device.name)
      print("       Max Clock Speed: %s MHz " %device.max_clock_frequency)
      print("       Compute Units: %s " %device.max_compute_units)
      print("       Local Memory: %s Kb" %(device.local_mem_size/1024.0))
      print("       Global Memory: %s Gb " %(round(device.global_mem_size/1073741824.0,2)))

