新发现：对于flask.request.files，
若传输的图片太大，会引发传输崩溃。
8M图就无法传输成功.
未来，传输图片可考虑用ftp