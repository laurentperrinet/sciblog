
You may have a bunch of files that you want to convert from one format to another: images, videos, music, text, ... How do you convert them *while using ZSH as your shell language* in a single line?

I will take the example of music files which I wish totransform from FLAC to [OPUS](https://mf4.xiph.org/jenkins/view/opus/job/opus-tools/ws/man/opusenc.html).

<!-- TEASER_END -->

# listing files

```

$ f flac

```

# converting files

Encoding in 128kB/s :

```

$ f flac -exec  sh -c 'opusenc --bitrate 128 "$0" "${0%.flac}.opus"' {} \;

```

Note that this will work also while exploring the folder hierarchy (that is if you have a bunch of folders with those files).

# deleting files

```

$ f flac -delete

```
