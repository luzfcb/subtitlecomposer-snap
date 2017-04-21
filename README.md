
subtitlecomposer snap app

This is an unfinished work, and it does not currently work ...

based on:

https://apachelog.wordpress.com/2016/12/02/snapping-kde-applications/



### build with docker
Install docker-ce, docker-compose

```bash
export DOCKER_COMPOSE_VERSION=1.12.0

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" --yes
sudo apt-get update -qq
sudo apt-get install -qq docker-ce libnetfilter-queue-dev libpcap-dev iptables-dev realpath
curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
chmod +x docker-compose
sudo mv docker-compose /usr/local/bin

```

Create the snap package

```bash
scripts/build
scripts/up
scripts/compile_snap
```

### build directily on KDE Neon user LTS

https://neon.kde.org/download

```bash
sudo apt-get update && sudo apt-get install git snapcraft realpath --yes
sudo sed -i -e 's/_DEB_BASED_PLATFORM \= \[/_DEB_BASED_PLATFORM = [\"neon\"\,/g' /usr/lib/python3/dist-packages/snapcraft//internal/repo/_platform.py

```

Create the snap package
```bash
git clone https://github.com/luzfcb/subtitlecomposer-snap.git
cd subtitlecomposer-snap

snapcraft
```

