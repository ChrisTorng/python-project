infra-build:
	podman-compose build

infra-up:
	podman-compose up --build -d

infra-stop:
	podman-compose stop

infra-down:
	podman-compose down