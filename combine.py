class combine(object):
	def combine(self, n, M):
		result = []
		if(M > 0):
			for i in range(M-1, n):
				returnlist = self.combine(i, M-1)
				if not returnlist:
					result.append([i])
				else:
					for r in returnlist:
						r.append(i)
						result.append(r)
		return result
c = combine();
for l in c.combine(4, 3):
	print l