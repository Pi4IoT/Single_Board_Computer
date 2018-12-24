import os, time

pipe_path = "/tmp/mypipe"
if not os.path.exists(pipe_path):
	os.mkfifo(pipe_path)

pipe_fd = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)
with os.fdopen(pipe_fd) as pipe:
	# while True:
		message = pipe.read()
		if message:
			print(message)
		time.sleep(0.5)
