from pyatool import PYAToolkit


# real function should contains an argument named 'toolkit'
def test_b(toolkit):
    return 'i am test_b, running on {}'.format(toolkit.device_id)


# bind adb command
PYAToolkit.bind_cmd(func_name='test_a', command='shell pm list package | grep google')
# or a real function
PYAToolkit.bind_func(real_func=test_b)

# change default configure
PYAToolkit.change_conf('TAG_EXEC_CMD', 'EXEC_COMMAND')

# no log?
PYAToolkit.switch_logger(False)

# init
d = PYAToolkit('123456F')

# and call it
result = d.test_a()
# output (may be different)
# package:com.google.android.webview

# and call it too
result = d.test_b()
# i am test_b, running on 123456F

# show all functions
all_functions = d.current_function()
print(all_functions)

# use build-in function
# test-only
d.hello_world()
# show all packages installed in your phone
d.show_package()
# top activity name
d.get_current_activity()
# install apk from url or path
d.install_from(url=r'https://github.com/williamfzc/simhand2/releases/download/v0.1.2/app-debug.apk')
# check if is installed
target_package_name = 'com.github.williamfzc.simhand2'
is_installed = d.is_installed(package_name=target_package_name)
d.clean_cache(target_package_name)
if is_installed:
    d.uninstall(target_package_name)

d.switch_wifi(False)
d.switch_airplane(True)
d.switch_airplane(False)
d.switch_wifi(True)

local_address = d.get_ip_address()
print(local_address)
