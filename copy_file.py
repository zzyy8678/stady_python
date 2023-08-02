import sys
import os
import pexpect


def main():
    """ copy file to remote server to local """

    max_retry_cnt = 3
    arg_length = len(sys.argv)
    if arg_length == 6:
        remote_ip = sys.argv[1]
        uname = sys.argv[2]
        passwd = sys.argv[3]
        loc_dir = sys.argv[4]
        remote_dir = sys.argv[5]
        cmd = 'scp -r ' + loc_dir + ' ' + uname + '@' + remote_ip + ':' + remote_dir
        print(cmd)
    else:
        remote_ip = sys.argv[1]
        uname = sys.argv[2]
        passwd = sys.argv[3]
        loc_dir = sys.argv[4]
        remote_dir = sys.argv[5]
        fw_name = sys.argv[6]
        cmd = 'scp ' + loc_dir + fw_name + ' ' + uname + '@' + remote_ip + ':' + remote_dir
        print(cmd)

    for loop_cunt in range(max_retry_cnt):
        loop_cunt += 1
        proc = pexpect.spawn(cmd)
        try:
            result = proc.expect(
                ['^.*100\%', 'password:', '(yes/no)', 'ssh.*refused$', '.*denied', pexpect.EOF, pexpect.TIMEOUT], 60)
            if result == 0:
                print("downloaded successfully")
                break

            if result == 1:
                proc.sendline(passwd)
                print("password sent")

            if result == 2:
                proc.sendline("yes")
                print("yes sent")
                result = proc.expect(['^.*100\%', 'password:'])
                if result == 0:
                    print("downloaded successfully")
                    break
                proc.sendline(passwd)
                print("password sent")

                proc.expect('^.*100\%', 60)
                print("downloaded successfully")
            break
        except Exception as e:
            print("Unknown error [%s]: " % e)

        proc.close()

        if loop_cunt == max_retry_cnt:
            print("Error downloading file\n")
        return 1
    else:
        return 0
