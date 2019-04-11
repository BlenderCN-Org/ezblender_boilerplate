
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

    def __get_local_rotation__(self):
        raise Exception("__get_local_rotation__ not implemented!") 
    def __get_global_rotation__(self):
        raise Exception("__get_global_rotation__ not implemented!")
    def __set_global_rotation__(self,rotation):
        raise Exception("__set_global_rotation__ not implemented!")
    def __set_local_rotation__(self,rotation):
        raise Exception("__set_local_rotation__ not implemented!")

    def __get_local_scale__(self):
        raise Exception("__get_local_scale__ not implemented!") 
    def __get_global_scale__(self):
        raise Exception("__get_global_scale__ not implemented!")
    def __set_global_scale__(self,scale):
        raise Exception("__set_global_scale__ not implemented!")
    def __set_local_rotation__(self,scale):
        raise Exception("__set_local_scale__ not implemented!")

    # Default implementations 

    def get_local_location(self):
        return self.__get_local_location__()
    def get_global_location(self):
        return self.__get_global_location__()
    def set_local_location(self,location):
        self.__set_local_location__(location)
    def set_global_location(self,location):
        self.__set_global_location__(location)