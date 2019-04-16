import mathutils

class Transformable:
    """
    Represents an object that can be transformed, such as meshes, armatures, bones, vertices, faces
    """

    # Interface

    def __get_global_location__(self):
        raise Exception("__get_global_location__ not implemented!")
    def __get_local_location__(self):
        raise Exception("__get_local_location__ not implemented!")
    def __set_global_location__(self,location):
        raise Exception("__set_global_location__ not implemented!")
    def __set_local_location__(self,location):
        raise Exception("__set_local_location__ not implemented!")

    def __get_local_rotation__(self,mode="XYZ"):
        raise Exception("__get_local_rotation__ not implemented!") 
    def __get_global_rotation__(self,mode="XYZ"):
        raise Exception("__get_global_rotation__ not implemented!")
    def __set_global_rotation__(self,rotation,mode="XYZ"):
        raise Exception("__set_global_rotation__ not implemented!")
    def __set_local_rotation__(self,rotation,mode="XYZ"):
        raise Exception("__set_local_rotation__ not implemented!")

    def __get_local_scale__(self):
        raise Exception("__get_local_scale__ not implemented!") 
    def __get_global_scale__(self):
        raise Exception("__get_global_scale__ not implemented!")
    def __set_global_scale__(self,scale):
        raise Exception("__set_global_scale__ not implemented!")
    def __set_local_rotation__(self,scale):
        raise Exception("__set_local_scale__ not implemented!")

    def __set_parent__(self,parent):
        raise Exception("__set_parent__ not implemented!")
    def __get_parent__(self):
        raise Exception("__get_parent__ not implemented!")

    # Default implementations 

    def get_local_location(self):
        return self.__get_local_location__()
    def get_global_location(self):
        return self.__get_global_location__()
    def set_local_location(self,location):
        self.__set_local_location__(location)
    def set_global_location(self,location):
        self.__set_global_location__(location)


    def get_local_rotation(self,mode="XYZ"):
        return self.__get_local_rotation__(mode)
    def set_local_rotation(self,value,mode="XYZ"):
        self.__set_local_rotation__(value,mode)

    def set_parent(self,parent):
        self.__set_parent__(parent)
    def get_parent(self):
        return self.__get_parent__()

    def get_local_scale(self):
        return self.__get_local_scale__()

    def set_local_scale(self,scale):
        self.__set_local_scale__(scale)