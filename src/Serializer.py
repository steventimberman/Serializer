import numpy as np

class NpArraySerializer2D:
	""" Object that represents a 2D numpy array as a serialized object,
		by storing its type, shape, and data as bytes.

		*** CAN TAKE IN EITHER A NUMPY ARRAY AS INPUT, OR
			INFORMATION REPRESENTING A NUMPY ARRAY.
			YOU MUST MAKE SURE TO USE KEYWORDS FOR INPUTS
			SPECIFIED BELOW IN ORDER TO BUILD ARRAY
		***

		Input (to initialize):
			np_array: the 2D numpy array you wish to serialize

			OR

			array_type: type of the numpy array
			array_shape: shape of the 
			array_bytes (bytes): 2D numpy array's data as bytes

	"""	

	def __init__(self, *args, **kwargs):

		if 'np_array' in kwargs:
			self.np_array=kwargs.get('np_array')
			self.array_type = self.np_array.dtype.name
			self.array_shape = self.np_array.shape
			self.array_bytes = self.np_array.tobytes()

		elif 'array_type' in kwargs and 'array_shape' in kwargs and 'array_bytes' in kwargs:
			self.array_type = kwargs.get('array_type')
			self.array_shape = kwargs.get('array_shape')
			self.array_bytes = kwargs.get('array_bytes')
			self.np_array = np.frombuffer(self.array_bytes, dtype = self.array_type).reshape(self.array_shape)
		else:
			raise Exception("Must use keyword arguments as inputs! Options are\nSerialized_2D_np_array(np_array=some_2d_np_array)\nSerialized_2D_np_array(array_type='int64', array_shape=(3,3), array_bytes=b'\\x01\\x00')")

	def get_array_type(self):
		""" Returns the string name of the 2d numpy array type """
		return self.array_type

	def get_array_shape(self):
		""" Returns the 2d numpy array size as tuple """
		return self.array_shape

	def get_array_bytes(self):
		""" Returns the 2d numpy array object as bytes """
		return self.array_bytes

	def get_np_array(self):
		""" Returns the 2d numpy array object represented """
		return self.np_array

	def __eq__(self, other):
		 return (self.get_array_type() == other.get_array_type()) and (self.get_array_shape() == other.get_array_shape()) and (self.get_array_bytes() == other.get_array_bytes())












