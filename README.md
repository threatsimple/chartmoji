
```
      _                _                   _ _
  ___| |__   __ _ _ __| |_ _ __ ___   ___ (_|_)
 / __| '_ \ / _` | '__| __| '_ ` _ \ / _ \| | |
| (__| | | | (_| | |  | |_| | | | | | (_) | | |
 \___|_| |_|\__,_|_|   \__|_| |_| |_|\___// |_|
                                        |__/

```


# chartmoji

A little dataviz can go a long way.

Chartmoji are little embedded charts that can be used inline in certain tools
like slack to communicate a series of values in a visual way.

Assume you had a series of values from some system and wanted to show the trend,
with the values  `[100, 50, 100, 0]`, you could show :chart_ln2101: instead.
It's much easier to understand the values this way.

Or perhaps you wanted to show it as a bar chart, :chart_bar2101:.


## how's it work?

These are pre-generated charts with 5 values plotted in a series, and values of
0,1,2.  To see a chart, you simply request the correct emoji like so:


```
:chart_ABCDE:
```

If A=1,B=2,C=1,D=0,A=1,you'd have `:chart_12101:`.

Since you're adding all the charts as emoji, that image will be inlined.

## Uses

We don't expect anyone to actually type these in a conversation, but for your
integrations they make things much more interesting while still allowing you to
communicate numerical trends in a pleasing way.

# usage

This repo comes with prebuilt images that can be used to displays simple charts.

If you don't want to rebuild them with custom colors, you can just upload the
included images.  See the next section to help you with that.

## slack emoji uploader

If you don't want to add all 216 chartmoji manually, you can use an included
tool.

There is an excellent tool available at
https://github.com/sgreben/slack-emoji-upload.

For convenience there a builds for 64 bit versions of mac, windows and linux in
the `contrib/` folder.

Example usage to upload all the line chartmoji:

```
./contrib/macos-slack-emoji-uploader \
  -email some@example.org \
  -password $SECRET \
  -team your-team \
  out/line/*.png
```

The options are as folows:

```
./macos-slack-emoji-uploader -h

Usage of ./macos-slack-emoji-uploader:
  -email string
    	user email
  -notify-channel string
    	Notify this channel on successful uploads
  -password string
    	user password
  -quiet
    	suppress log output
  -team string
    	Slack team (only needed when using email/password auth)
  -token string
    	Slack API token
```

*note* you may see errors about slack rate limiting you during the upload.
These are just warnings and not a problem.  The client waits then attempts to
upload that emoji again.

## customizing the charts

If you want to change the colors of the charts, edit bin/create.py.  You're
looking for the lines near the top like:

```
line_color = gray
bg_color = white
transparent_bg = True
```

Change those to one of the predefined colors.

Then, if you've got python3 installed and gnu make, you can run `make build` and
the dependencies will be downloaded and images placed in `out/line/` and
`out/bar/`.

Then just upload the images to slack.

## formatting your data

See the script in `bin/sample.py` for some code snippets on normalizing your
data into a series within 0,1,2 range.

