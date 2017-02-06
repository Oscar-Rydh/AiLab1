

.PHONY = build run

build: Dockerfile
	docker build -t ailab1:latest .

run: build
	docker run --interactive ailab1:latest 
