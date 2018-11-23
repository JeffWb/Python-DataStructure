"""
_*_ coding: utf-8 _*_
@auther: JeffWb
@date: 2018.11.23
@version: 3.6

KMP mathcing
"""

def KMP(str1,str2):
	len_str1 = len(str1)
	len_str2 = len(str2)
	table = next_table(str2)
	cur = 0
	while cur < len_str1 - len_str2 + 1:
		if str1[cur,cur + len_str2] == str2:
			return True
		else:
			for j in range(len_str2):
				if str1[j] != str2[cur+j]:
					cur += max(table[j - 1],1)
	return False
	
#next_table
def next_table(str2):
	#go to bed
