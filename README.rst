========
flipflop
========

FastCGI/WSGI gateway with Microsoft Windows support.

`github.com/lehui99/flipflop <https://github.com/lehui99/flipflop>`_

Forked from: `github.com/Kozea/flipflop <https://github.com/Kozea/flipflop>`_

The original *flipflop* only supports Linux.  I've added Windows support to it.

This module is a simplified fork of flup, written by Allan Saddi. It only has
the FastCGI part of the original module.

.. code-block:: python

    #!/usr/bin/env python
    from myapplication import app
    from flipflop import WSGIServer


    WSGIServer(app).run()


You can specify the *max_connections* and build your own listen socket and do not
set *close-on-exec* if using under Windows.

.. code-block:: python

    import socket
    from myapplication import app
    from flipflop import WSGIServer

    max_connections = 150  # Increase this number to serve more connections simultaneously.

    sock = socket.socket()
    sock.bind(('127.0.0.1', 9000))
    sock.listen(5)

    close_on_exec = False

    WSGIServer(app, max_connections).run(sock, close_on_exec)


Now you've got a FastCGI server listening on 127.0.0.1:9000.  You can also build
your own listen socket in Linux in order to setup distributed FastCGI servers.
Remember to set *close_on_exec = True* if FastCGI process is forked from the web server.

*flipflop* is released under the BSD 2-Clause license.
