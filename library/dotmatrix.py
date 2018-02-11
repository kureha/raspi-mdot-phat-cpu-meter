#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from microdotphat import set_pixel, write_string, scroll, clear, show, WIDTH, HEIGHT

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
			# skip list check
			if i in DotMatrix.SKIP_LIST:
				continue

			# increment render counter
			render_counter = render_counter + 1

			# real meter check
			if i >= meter_minnum and render_counter > x_range:
				break

			# render left ro right
			for k in y_range:
				set_pixel(i, k, 1)
				#print("x = " + str(i))
				#print("y = " + str(k))
	
	# Rendering method
	@staticmethod
	def show():
		show()

	# Write string and scrolling to last
	@staticmethod
	def render_string(s, scroll_x = 8, scroll_y = 0, scroll_sleep = 1, kerning_flag = False):
		# init view
		clear()

		# render string
		write_string(s, kerning = kerning_flag)
		show()
		time.sleep(scroll_sleep)

		# render to end
		for i in range(len(s)):
			# scroll -> render
			scroll(scroll_x, scroll_y)
			show()
			time.sleep(scroll_sleep)

# Endpoint - TestLogic
if __name__ == "__main__":
	DotMatrix.clear()
	for i in range(50):
		DotMatrix.render_meter(i * 2)
		DotMatrix.show()
		time.sleep(0.1)

