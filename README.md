# v2rayN-pac-adder
![Alt Text](https://github.com/Hyperkopite/v2rayN-pac-adder/blob/master/s1.png)
                                                                                                                        
A tool to conveniently add needed URLs to PAC list of v2rayN (For Windows only currently)
一个帮助你方便地添加网址到v2rayN的PAC列表的小工具（暂时只支持Windows系统）
> How to use | 如何使用</br>

[1] Place the update_pac.py under v2rayN directory (where the v2rayN.exe is located).</br>
[1] 将update_pac.py放到v2rayN目录下，也就是v2rayN.exe所在的地方。</br></br>
[2] Enter v2rayN directory in powershell or cmd.</br>
[2] 在powershell或者cmd中进入到该目录。</br></br>
[3] Execute "python3 update_pac.py".</br>
[3] 执行"python3 update_pac.py"命令。</br></br>
[4] When you are browsing any website which you find you need to add it to pac list, simply copy it from browser address bar and press      "ctrl + alt + insert" hotkey, the address will be added to pac list of v2rayN and service will be automatically restarted.</br>
[4] 当你在PAC模式下使用v2rayN浏览某个网站时，如果觉得这个网址需要使用v2rayN访问，只需从浏览器地址栏复制网址，按下"ctrl + alt + insert"，即可自动添加到v2rayN访问列表。</br></br>
[5] Refresh the page to browse via v2rayN.</br>
[5] 刷新页面即可。</br></br>
**IMPORTANT**: Run the script as administrator, or it may not be able to respond normally when running in background!</br>
**重要提示**：请务必以管理员身份运行powershell或者cmd，否则脚本可能无法在后台正常工作！
