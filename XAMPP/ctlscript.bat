@echo off
rem START or STOP Services
rem ----------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\server\hsql-sample-database\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\ingres\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\ingres\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\mysql\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\mysql\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\postgresql\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\openoffice\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache-tomcat\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache-tomcat\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\resin\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\resin\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\jetty\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\jetty\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\subversion\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\subversion\scripts\ctl.bat START)
rem RUBY_APPLICATION_START
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\lucene\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\lucene\scripts\ctl.bat START)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\third_application\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\third_application\scripts\ctl.bat START)
goto end

:stop
echo "Stopping services ..."
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\third_application\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\third_application\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\lucene\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\lucene\scripts\ctl.bat STOP)
rem RUBY_APPLICATION_STOP
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\subversion\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\subversion\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\jetty\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\jetty\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\server\hsql-sample-database\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\resin\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\resin\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache-tomcat\scripts\ctl.bat (start /MIN /B /WAIT C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache-tomcat\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\openoffice\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\apache\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\ingres\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\ingres\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\mysql\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\mysql\scripts\ctl.bat STOP)
if exist C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\noa73\OneDrive\Bureaublad\necuiendcn\postgresql\scripts\ctl.bat STOP)

:end

