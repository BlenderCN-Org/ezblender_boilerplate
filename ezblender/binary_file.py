import struct

class BinaryFile:
    def __init__(self,mode,path,endian='SMALL'):
        self.file = open(path,mode)
        if endian is 'BIG':
            self.endian = '>'
        else:
            self.endian = '<'
        self.seek_stack = []
    def tell(self):
        """Returns the current read/write pointer in the file

            Returns:
                int: Current read position
        """
        return self.file.tell()
    def seek(self,index):
        """Sets the current read/write pointer in the file

            Args:
                index (int) : New pointer position
        """
        return self.file.seek(index)
    def push_seek(self,index):
        """Pushes the current read/write pointer in the file, then sets it to something else

            Args:
                index (int) : New pointer position
        """
        self.seek_stack.append(self.tell())
        self.seek(index)
    def pop_seek(self):
        """Pops the last read/write pointer pushed by BinaryFile#push_seek""" 
        self.seek(self.seek_stack.pop())
    def close(self):
        """Closes the file"""
        self.file.close()

class BinaryFileReader(BinaryFile):
    def __init__(self,path,endian='SMALL'):
        super(BinaryFileReader,self).__init__('rb',path,endian)
    def _read_int(self,letter,size):
        return struct.unpack(self.endian+letter,self.file.read(size))[0]
    def read_int8(self):
        """Reads a signed integer of size 8
            Returns:
                int: Signed integer of size 8
        """
        return self._read_int('b',1)
    def read_int16(self):
        """Reads a signed integer of size 16
            Returns:
                int: Signed integer of size 16
        """
        return self._read_int('h',2)
    def read_int32(self):
        """Reads a signed integer of size 32
            Returns:
                int: Signed integer of size 32
        """
        return self._read_int('i',4)
    def read_int64(self):
        """Reads a signed integer of size 64
            Returns:
                int: Signed integer of size 64
        """
        return self._read_int('q',8)
    def read_uint8(self):
        """Reads an unsigned integer of size 8
            Returns:
                int: Unsigned integer of size 8
        """
        return self._read_int('B',1)
    def read_uint16(self):
        """Reads an unsigned integer of size 16
            Returns:
                int: Unsigned integer of size 16
        """
        return self._read_int('H',2)
    def read_uint32(self):
        """Reads an unsigned integer of size 32
            Returns:
                int: Unsigned integer of size 32
        """
        return self._read_int('I',4)
    def read_uint64(self):
        """Reads an unsigned integer of size 64
            Returns:
                int: Unsigned integer of size 64
        """
        return self._read_int('Q',8)
    def read_string(self,size,encoding='ASCII'):
        """Reads a string
            Returns:
                string: Decoded string
        """
        return self.file.read(size).decode(encoding)
    def read_terminated_string(self,encoding='ASCII'):
        """Reads a null-terminated string
            Returns:
                string: Null-terminated decoded string
        """
        buf = b""
        while True:
            b = self.file.read(1)
            if b == None or b == b'' or b == b'\x00':
                return buf.decode(encoding)
            else:
                buf+=b

class BinaryFileWriter(BinaryFile):
    def __init__(self,path,endian='SMALL'):
        super(BinaryFileWriter,self).__init__('wb+',path,endian)
    def _write_int(self,letter,size,value):
        self.file.write(struct.pack(self.endian+letter,value))
    def write_int8(self,value):
        """Writes a signed integer of size 8
            
            Args:
                value (int) : Value to be written as an int8
        """
        self._write_int('b',1,value)
    def write_int16(self,value):
        """Writes a signed integer of size 16
            
            Args:
                value (int) : Value to be written as an int16
        """
        self._write_int('h',2,value)
    def write_int32(self,value):
        """Writes a signed integer of size 32
            
            Args:
                value (int) : Value to be written as an int32
        """
        self._write_int('i',4,value)
    def write_int64(self,value):
        """Writes a signed integer of size 64
            
            Args:
                value (int) : Value to be written as an int64
        """
        self._write_int('q',8,value)
    def write_uint8(self,value):
        """Writes an unsigned integer of size 8
            
            Args:
                value (int) : Value to be written as a uint8
        """
        self._write_int('B',1,value)
    def write_uint16(self,value):
        """Writes an unsigned integer of size 16
            
            Args:
                value (int) : Value to be written as a uint16
        """
        self._write_int('H',2,value)
    def write_uint32(self,value):
        """Writes an unsigned integer of size 32
            
            Args:
                value (int) : Value to be written as a uint32
        """
        self._write_int('I',4,value)
    def write_uint64(self,value):
        """Writes an unsigned integer of size 64
            
            Args:
                value (int) : Value to be written as a uint64
        """
        self._write_int('Q',8,value)
    def write_string(self,string,encoding='ASCII'):
        self.file.write(string.encode(encoding))