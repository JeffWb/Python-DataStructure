"""
_*_ coding:utf-8 _*_
str matching ------naive matching
@auther: JeffWb
@date: 2018.11.23
@version: 3.6
"""

#whether str1 includes str2
def naive_match(str1,str2):
	len_str1 = len(str1)
	len_str2 = len(str2)
	for i in range(len_str1 - len_str2 + 1):
		if str1[i:i + len_str2] == str2
			return True
		return False
		
if __name__ == '__main__':
	str1 = "abcdef"
	str2 = "bcdafe"
	str3 = "ab"
	naive_match(str1,str3)
	naive_match(str2,str3)
