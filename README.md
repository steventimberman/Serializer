# Serializer (For 2D Numpy Arrays)

## NpArraySerializer2D: Serializes a 2-dimensional numpy array using the necessary data. Can be used to send the array across a network (ie. via remote procedure call or api call).

### CAN BE USED WITH TWO CONSTRUCTORS, WITH DIFFERENT KEYWORD ARGUMENTS AS INPUTS. BE EXACT!:
  Inputs:
    np_array: the 2D numpy array you wish to serialize
   
   OR
   
   array_type: type of the numpy array
   array_shape: shape of the array
   array_bytes (bytes): 2D numpy array's data as bytes
   
### EXAMPLE (Where we assume NP_ARRAY_1 is a numpy array object, array_type is a defined type of the numpy array, array_shape is a tuple of 2 values, and array_bytes are a byte type format of the data):
  - serialized_array_1 = NpArraySerializer2D(array_type=array_type, array_shape=array_shape, array_bytes=array_bytes)
  - serialized_array_2 = NpArraySerializer2D(np_array=NP_ARRAY_1)
  
### Both of these examples return an object with the same capabilities, where you can retreive the numpy array itself, along with the type, shape, and byte data of the array.
