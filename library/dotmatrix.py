#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from microdotphat import set_pixel, scroll, clear, show, WIDTH, HEIGHT

# Pimonori pHat DotMatrix Class
class DotMatrix:
	# define
	METER_WIDTH = 30
	SKIP_LIST = [5, 6, 7, 13, 14, 15, 21, 22, 23, 29, 30, 31, 37, 38, 39]

	# All clear
	@staticmethod
	def clear():
		clear()

	@staticmethod
	def render_meter(percent, y_range = range(7), meter_minnum = 0):
		# calculate percent
		x_range = int(DotMatrix.METER_WIDTH * (percent / 100.0))
		#print("x_range = " + str(x_range))

		# set_pixel
		render_counter = 0
		for i in range(WIDTH):
			# skip invisible matrix
			if i in DotMatrix.SKIP_LIST:
				continue

			# increment render counter
			render_counter = render_counter + 1

			# meter count check
			if i >= meter_minnum and render_counter > x_range:
				break

			# render up to down
			for k in y_range:
				set_pixel(i, k, 1)
				#print("x = " + str(i))
				#print("y = " + str(k))
	
	# Rendering method
	@staticmethod
	def show():
		show()

# Endpoint - TestLogic
if __name__ == "__main__":
	DotMatrix.clear()
	for i in range(50):
		DotMatrix.render_meter(i * 2)
		DotMatrix.show()
		time.sleep(0.1)

