build:
	@docker build . -t term21-webui

run: build
	@docker run -it -p 8080:8080 term21-webui

bash:
	@docker run -it term21-webui bash

