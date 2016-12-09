import base64
from math import floor
import string


def base62(num, b=62):
	if b <= 0 or b > 62:
		return 0
	base = string.digits + string.ascii_lowercase + string.ascii_uppercase
	r = num % b
	res = base[r]
	q = floor(num / b)
	while q:
		r = q % b
		q = floor(q / b)
		res = base[int(r)] + res
	return res


def base10(num, b=62):
	base = string.digits + string.ascii_lowercase + string.ascii_uppercase
	limit = len(num)
	res = 0
	for i in range(limit):
		res = b * res + base.find(num[i])
	return res

####################   Base64   #################
