def longest_consec(str_arr, k):
    long_str = ''
    if len(str_arr) == 0 or k <= 0 or k > len(str_arr):
        return ''
    
    while k > 0:
        tmp_str = str_arr[0]
        
        # Find the longest str in str_arr
        for each in str_arr:
            if len(each) > len(tmp_str):
                tmp_str = each
        # Remove the same element in str_arr
        for i in str_arr:
            if i == tmp_str:
                str_arr.remove(i)

        long_str = long_str + tmp_str
        k = k - 1
    print '******the answer is: *******', long_str
            