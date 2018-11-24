"""
_*_ coding: utf-8 _*_
@auther: JeffWb
@date: 2018.11.23
@version: 3.6

KMP mathcing
"""

def KMP(str1,str2):
	"""
	first char is not matched, move 1;
	others is not matched, next_table[]
	"""
	len_str1 = len(str1)
	len_str2 = len(str2)
	table = next_table(str2)
	cur = 0                 #cur of str1
	while cur < len_str1 - len_str2 + 1:
		if str1[cur,cur + len_str2] == str2:
			return True
		else:
			for j in range(len_str2):
				if str1[cur+j] != str2[j]:
					if j == 0:
						cur += 1       #first is not matched, move 1
					else:
						cur += table[j - 1]
					break
	return False
	
#next_table
def next_table(str2):
	"""
	seconde char is not matched, move 1------->table = [1]
	others: equal, longest substr of pre_str and post_str------get it's length l_s
		has been matched str in str2 with str1 --------get it's length l_m
		move step = l_m -l_s
	"""	
	table = [1]      #save mive steps intable,   1 means only str2's first char matched, move 1
	pre = []         #save prefix
	post = []	 #save postfix
	for i in range(len(str2) - 1):
		pre_c = pre.copy()
		post_c = post.copy()
		for j in range(i):
			pre_c.append(p[:j+1])
			pre_c.reverse()                  #reverse pre_c
		for k in range(1,i+1):
			post_c.append(p[k:i+1])
		step = 0                                 #initialize step = 0
		for h in range(len(pre_c)):
			if pre_c[h] = post_c[h]:         #find longest son str of str2 matched 
				step = i + 1 - len(pre_c[h])        #step = len(str) - longest matched str length
				break
			step = 1                         # no equal pre_str and post_str,   move 1
		table.append(step)
	return table

if __name__ == '__main__':
	print(naive_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
	print(next_table("ABCDABD"))
	print(KMP("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
			
			
			
			
