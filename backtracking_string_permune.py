def permune(orignal, chosen):
	if not orignal:
		print(chosen)
	else:
		for i in range(len(orignal)):
			c=orignal[i]
			chosen+=c
			lt=list(orignal)
			lt.pop(i)
			orignal=''.join(lt)
			permune(orignal,chosen)
			orignal=orignal[:i]+c+orignal[i:]
			chosen=chosen[:len(chosen)-1]

permune('lit','')