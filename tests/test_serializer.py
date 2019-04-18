import pytest
import numpy as np
from src.Serializer import NpArraySerializer2D

np.random.seed(42)

NP_ARRAY_ONE = np.random.randint(1,11, (10,10))

SERIALIZED_ARRAY_1 = NpArraySerializer2D(np_array=NP_ARRAY_ONE)


def test_serializer_get_np_array():
	assert np.array_equal(SERIALIZED_ARRAY_1.get_np_array(), NP_ARRAY_ONE)

def test_serializer_get_array_type():
	original_array_type = NP_ARRAY_ONE.dtype.name
	assert SERIALIZED_ARRAY_1.get_array_type() == original_array_type

def test_serializer_get_array_shape():
	original_array_shape = NP_ARRAY_ONE.shape
	assert SERIALIZED_ARRAY_1.get_array_shape() == original_array_shape

def test_serializer_get_array_bytes():
	original_array_bytes = NP_ARRAY_ONE.tobytes()
	assert SERIALIZED_ARRAY_1.get_array_bytes() == original_array_bytes

def test_serializer_bytes_constructor():
	array_type = SERIALIZED_ARRAY_1.get_array_type()
	array_shape = SERIALIZED_ARRAY_1.get_array_shape()
	array_bytes = SERIALIZED_ARRAY_1.get_array_bytes()
	NEW_SERIALIZED_ARRAY = NpArraySerializer2D(array_type=array_type, array_shape=array_shape, array_bytes=array_bytes)
	assert np.array_equal(SERIALIZED_ARRAY_1.get_np_array(), NEW_SERIALIZED_ARRAY.get_np_array())

