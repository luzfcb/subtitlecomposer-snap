
subtitlecomposer snap app

This is an unfinished work, and it does not currently work ...

based on:

https://apachelog.wordpress.com/2016/12/02/snapping-kde-applications/



```bash
sudo apt-get update && sudo apt-get install git snapcraft --yes

```


```bash
git clone https://github.com/luzfcb/subtitlecomposer-snap.git
cd subtitlecomposer-snap


snapcraft build
# waiting for a long time

# after, generate the snap package
snapcraft snap
```

