A two-part middleware which modifies request.COOKIES and adds a set and delete method.

* ``set`` matches ``django.http.HttpResponse.set_cookie``
* ``delete`` matches ``django.http.HttpResponse.delete_cookie``

Installation
------------

Just modify your ``MIDDLEWARE_CLASSES`` setting, order is important here!

:
	MIDDLEWARE_CLASSES = (
	    'djcookies.CookiePreHandlerMiddleware',
	    ...
	    'djcookies.CookiePostHandlerMiddleware',
	)

Usage
-----

	def my_view(request):
	    request.COOKIES.set([args])
	    ...
	    return response