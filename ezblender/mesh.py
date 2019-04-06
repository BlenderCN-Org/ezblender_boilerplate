import bmesh
import bpy

class Mesh:
    """
    Represents a single mesh object in the Blender Scene
    """
    def __init__(self,world,blender_object):
        self.world = world
        self.blender_object = blender_object

    def __begin_edit_mode__(self):
        if(self.world.current_edit_object==self):
            return
        self.world.current_edit_object = self
        bpy.context.scene.objects.active = self.blender_object
        bpy.ops.object.mode_set(mode='EDIT')
        self.bmesh = bmesh.new()
        self.bmesh.from_mesh(self.blender_object.data)

    def __finish_edit_mode__(self):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.bmesh.to_mesh(self.blender_object.data)

    def add_vertex(self,vertex):
        """Adds a new vertex to this mesh

        Args:
            vertex ((float,float,float)): Tuple of x/y/z coordinates
        Returns:
            #TODO BMesh vertex?
        """
        self.__begin_edit_mode__()
        self.__dirty_verts = True
        return self.bmesh.verts.new(vertex)

    def add_face(self,vertices):
        """Adds a new face to this mesh

        Args:
            vertices ([int|TODO vertex ref]): Vertices to use for this face
        """

        # TODO: Is "int" the right type to use here?
        vertices = [
            self.get_vertex(vertex) if isinstance(vertex,int) else vertex for vertex in vertices
        ]
        self.bmesh.faces.new(vertices)


    def add_edges(self,vertices):
        """Adds new edges to this mesh, drawn as a line from the first vertex to the last

        Args:
            vertices ([int|TODO vertex ref]): Vertices to use for the new edges

        """
        vertices = [
            self.get_vertex(vertex) if isinstance(vertex,int) else vertex for vertex in vertices
        ] 

        for i,e in enumerate(vertices):
            if i==0: 
                continue
            self.bmesh.edges.new([vertices[i-1],e])
        self.__dirty_edges = True

    # TODO: Should these be public?
    def get_edge(self,index):
        self.__begin_edit_mode__()
        if(self.__dirty_edges):
            self.bmesh.edges.ensure_lookup_table()
        return self.bmesh.edges[index]

    def get_vertex(self,index):
        self.__begin_edit_mode__()
        if(self.__dirty_verts):
            self.bmesh.verts.ensure_lookup_table()
        return self.bmesh.verts[index]
    
    def get_face(self,face,safe=False):
        self.__begin_edit_mode__()
        if(self.__dirty_faces):
            self.bmes.faces.ensure_lookup_table()