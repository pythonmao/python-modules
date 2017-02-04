import struct
import ctypes

mm = struct.pack("hhl", 1, 2, 3)
#mm = struct.pack("hhl01", 1,2,3) //padding
nn = struct.unpack('hhl', mm)
print mm, nn

mm = struct.calcsize('ci') 
nn = struct.calcsize('ic')
print mm, nn

mm = ctypes.create_string_buffer(100)
struct.pack_into('hhl', mm, 0, 1, 2, 3)
print struct.unpack_from('hhl', mm, 0)
