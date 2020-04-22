# v2rayN-pac-adder
![Alt Text](https://github.com/Hyperkopite/v2rayN-pac-adder/blob/master/s1.png)
                                                                                                                        
A tool to conveniently add needed URLs to PAC list of v2rayN (For Windows only currently)</br>
一个帮助你方便地添加网址到v2rayN的PAC列表的小工具（暂时只支持Windows系统）
> **How to use | 如何使用**</br></br>
***.exe：***</br>
[1] For convenience, I also packed the .py script to .exe executable, you can run this without dependency to Python environment. Usage is same as below, just place the exe file under v2rayN directory and run.</br>
[1] 为了方便起见，也在***Release***中提供由py文件打包成的exe，可以不依赖Python环境直接在Windows下运行。使用方法同下，放到v2rayN目录下运行即可。</br></br>
***.py：***</br>
[1] Place the update_pac.py under v2rayN directory (where the v2rayN.exe is located).</br>
[1] 将update_pac.py放到v2rayN目录下，也就是v2rayN.exe所在的地方。</br></br>
[2] Enter v2rayN directory in powershell or cmd **with administrator role**.</br>
[2] 以**管理员身份**运行powershell或者cmd，进入到该目录。</br></br>
[3] Execute "python3 update_pac.py" and minimize the window to keep it running in background.</br>
[3] 执行"python3 update_pac.py"命令，最小化窗口让其在后台运行。</br></br>
[4] When you are browsing any website needs to be added to PAC list, simply copy it from browser address bar and press      "ctrl + alt + insert" hotkey, the address will be added to PAC list of v2rayN and service will be automatically restarted.</br>
[4] 当你在PAC模式下使用v2rayN时，如果觉得某个网址需要使用v2rayN访问，只需从浏览器地址栏复制网址，然后按下"ctrl + alt + insert"组合键，即可自动添加到v2rayN访问列表。</br></br>
[5] Refresh the page to browse via v2rayN.</br>
[5] 刷新页面即可。</br></br>
**IMPORTANT**: Run the script as administrator, or it may not be able to respond normally when running in background!</br>
**重要提示**：请务必以管理员身份运行powershell或者cmd，否则脚本可能无法在后台正常工作！
