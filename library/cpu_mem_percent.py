#!/usr/bin/python
# -*- coding: utf-8 -*-

import psutil
import time
from dotmatrix import DotMatrix

## DEFINE START >>>
RENDER_INTERVAL = 0.1
## DEFINE END <<<

if __name__ == "__main__":
	# initialize
	DotMatrix.clear()

	while(True):
		# init
		DotMatrix.clear()

		# render cpu
		cpu_percent = psutil.cpu_percent(interval= None)
		#print("cpu=" + str(cpu_percent) + "%")
		DotMatrix.render_meter(percent = cpu_percent, y_range = range(3), meter_minnum = 1)

		# render memory
		vmem_info = psutil.virtual_memory()
		memory_percent = vmem_info.percent
		#print("mem=" + str(memory_percent) + "%")
		DotMatrix.render_meter(percent = memory_percent, y_range = range(4, 7), meter_minnum = 1)

		# final rendering
		DotMatrix.show()

		# wait to next render
		time.sleep(RENDER_INTERVAL)

