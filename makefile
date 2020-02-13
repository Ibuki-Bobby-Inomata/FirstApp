DOCKER := sudo docker
CONTAINER_NAME := first_step
IMAGE_NAME := comer

run:
	@$(DOCKER) run -it --rm --name $(CONTAINER_NAME) -v $(PWD)/app:/app -p 5000:5000 $(IMAGE_NAME) python app/run.py

clear_cont:
	@$(DOCKER) rm $(CONTAINER_NAME)

create_images:
	@$(DOCKER) build -t $(IMAGE_NAME) ./docker
