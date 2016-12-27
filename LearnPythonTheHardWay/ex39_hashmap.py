﻿# -*- coding: utf-8 -*-

def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap
	
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Giben a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""Return the index, key and the value of a slot found in a bucket."""
	bucket = get_bucket(aMap, key)
	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v

def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if v:
		bucket[i] = (key, value)
	else:
		bucket.append((key, value))
		
def delete(aMap, key):
	"""Deteltes the given key from the map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		