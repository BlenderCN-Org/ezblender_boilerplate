import bmesh
import bpy
import importlib
from . import scene_object
from . import vector

try: importlib.reload(vector)
except Exception as e: print("Exception Reloading:",e)

try: importlib.reload(scene_object)
except Exception as e: print("Exception Reloading:",e) # Try/catch to work with Sphinx documentation

Vector = vector.Vector

class Mesh(scene_object.SceneObject):
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
        if(self.world.current_edit_object==self):
            bpy.ops.object.mode_set(mode='OBJECT')
            self.bmesh.to_mesh(self.blender_object.data)
            del self.bmesh
            self.world.current_edit_object = None

    def add_vertex(self,vertex):
        """Adds a new vertex to this mesh

        Args:
            vertex ((float,float,float)): Tuple of x/y/z coordinates
        Returns:
            #TODO BMesh vertex?
        """
        self.__begin_edit_mode__()
        self.__dirty_verts = True
        return self.bmesh.verts.new(Vector(vertex).values)

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

    def set_vertex_groups(self,vertices,groups):
        """Adds new vertex groups to vertices

        Args:
            vertices (int|[int]): Vertex indices to be added
            groups ((string,float)|[(string,float)]): Tuples of groupname and weights to be applied
        """
        if(type(vertices)==int):
            vertices = [vertices]

        self.__finish_edit_mode__()

        for (groupname,weight) in groups:
            if not groupname in self.blender_object.vertex_groups:
                self.blender_object.vertex_groups.new(groupname)
            group = self.blender_object.vertex_groups[groupname]
            group.add(vertices,weight,'ADD')

    def get_groups_for_vertex(self,vertex):
        """Returns all group ids assigned to a vertex

        Args:
            vertex (int): Vertex index to search for

        Returns:
            ([(int,float)]): List of tuples containing group id (left) and weight (right)
        """
        vertex = self.blender_object.data.vertices[vertex]
        return [(group.group,group.weight) for group in vertex.groups]

    def get_vertices_in_group(self,group):
        """Returns all vertices assigned a group
        
        Args:
            group (int|string): Group name or index to search for

        Returns:
            [int]: List of vertex ids assigned this group
        """
        self.__finish_edit_mode__()        
        group = self.blender_object.vertex_groups[group].index
        vgs = []
        for v in self.blender_object.data.vertices:
            fofo = [vg.group for vg in v.groups]

        return [v.index for v in self.blender_object.data.vertices if group in [vg.group for vg in v.groups]]

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
        # TODO Why is this method not even finished?