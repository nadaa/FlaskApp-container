from flask import Flask

app=Flask(__name__)

@app.route('/')
def Home():
	return "<h1>Welcome to the world of containers</h1>"

if(__name__=='__main__'):
	# as we run flask from the container, which is another domain, to tell falsk to accept any comming requests from different ip (host='0.0.0.0') is used.
	app.run(host='0.0.0.0')

