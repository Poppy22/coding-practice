import operator


class TimeInterval():
	def __init__(self, start, end):
		self.start = start
		self.end = end


def main():
	time_input = [(1, 4), (8, 9), (5, 6), (2, 6), (2, 3), (3, 4)]
	time_intervals = []
	for time in time_input:
		time_intervals.append(TimeInterval(time[0], time[1]))

	time_intervals = sorted(time_intervals, key=operator.attrgetter("start", "end"))
	
	global_max = 0
	local_max = 0
	last_time = time_intervals[0]
	for i in range(1, len(time_intervals)):
		if time_intervals[i].start < last_time.end:
			local_max += 1
		else:
			global_max = max(global_max, local_max)
			local_max = 1
		last_time = time_intervals[i]

	print('Maximum number of rooms:', global_max)

if __name__ == "__main__":
	main()