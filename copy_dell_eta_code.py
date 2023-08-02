def get_file_by_scp(ipaddr, username, password, src_dir, fname, local_dir):
    """ copy file from remote server to local """
    max_retry_cnt = 3
    cur_cnt = 0;
    cmd_str1 = ("/usr/bin/scp")
    src_dir_fname = (src_dir + '/' + fname)
    cmd_str2 = (username + '@' + ipaddr + ':' + src_dir_fname)
    cmd = (cmd_str1 + " " + cmd_str2 + " " + local_dir)

    rtn_code = 1
    for cur_cnt in range(max_retry_cnt):
        try:
            proc = pexpect.spawn(cmd)
            result = proc.expect(
                ['^.*100\%', 'password:', '(yes/no)', 'ssh.*refused$', '.*denied', ], 60)
            if result == 0:
                print("downloaded successfully")
                break

            if result == 1:
                proc.sendline(password)
                print("password sent")
            if result == 2:  #
                proc.sendline("yes")
                print("yes sent")
                result = proc.expect(['^.*100\%', 'password:'])
                if result == 0:
                    print("downloaded successfully")
                    break
                proc.sendline(password)
                print("password sent")
            proc.expect('^.*100\%', 60)
            print("downloaded successfully")
            break

        except Exception as e:
            print("Unknown error [%s]: " % e)

        proc.close()
        cur_cnt += 1

    if cur_cnt == max_retry_cnt:
        print("Error downloading file[" + fname + "] from server !\n")
        return 1
    else:
        return 0
