# A little dataviz goes a long way.  <img src="https://github.com/threatsimple/chartmoji/blob/master/images/line/chart_ln02012.png?raw=true" width=20 height=20/>

Here's an example being used in a slack message.

<img src="https://github.com/threatsimple/chartmoji/blob/master/contrib/misc/slack_preview.png?raw=true" width=60% />

Chartmoji are small embedded charts that can be used inline in certain tools
like slack to communicate a series of values in a visual way.

These are essentially an emoji implementation of Edward Tufte's sparkline
concept.

Assume you had a series of values and wanted to show the trend. Given the values
`[40, 93, 58, 17, 96]`, you could just include it inline <img src="https://github.com/threatsimple/chartmoji/blob/master/images/line/chart_ln12101.png?raw=true" width=20 height=20/>  instead.
It's much easier to understand the values this way.

There's also a bar chart version: <img src="https://github.com/threatsimple/chartmoji/blob/master/images/bar/chart_bar12101.png?raw=true" width=20 height=20/>.

If you want to see them in action (and play with them) you can join this slack channel.

https://join.slack.com/t/chartmoji/shared_invite/enQtODg1NDg3MDgyMTk3LTM5ZjA2MTI3NWVmNzI1Y2M1MTRjMjcwYWEyNTUxZGRlZDMyNzBlOWQ3YzI0ZGIwNmFiNTBiNTUwMzc4ZDc2YTE

## quickstart

Clone this repo, and the emoji can be found in `images/line` and `images/bar`.
Upload them wherever you see fit to use them.

There's a lot of images though, so if you're adding them to slack, you probably
want to see the uploader section below to help automate that.


## how's it work?

These are pre-generated charts with 5 values plotted in a series, and values of
0,1,2.  To see a chart, you simply request the correct emoji like so:


```
:chart_ABCDE:
```

If A=1,B=2,C=1,D=0,A=1, you'd have `:chart_12101:`.

Since you're adding all the charts as emoji, that image will be inlined when
referenced in your chat client.

## Uses

I don't expect anyone to actually type these in a conversation, but for your
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

For convenience there are builds for 64 bit versions of mac, windows and linux
in the `contrib/` folder.

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
These are just warnings, the client attempts to upload that emoji again.

## customizing the charts

The current chart colors were chosen because they work well with both light and
dark themes in slack.

However, if you want to change the colors of the charts, edit bin/create.py.
You're looking for the lines near the top like:

```
line_color = gray
bg_color = white
transparent_bg = True
```

Change those to one of the predefined colors in the script.

If you've got python3 installed and gnu make, you can run `make build` and
the dependencies will be downloaded and images placed in `out/line/` and
`out/bar/`.

Then just upload the images to slack.

## formatting your data

See the script in `contrib/samples/mojify.py` for some code snippets on
normalizing your data into a series within 0,1,2 range.

example usage:

```python
>>> import mojify
>>> values = [20,35,80,90,1]
>>> mojify.chartmoji(values)
':chart_ln01220:'
>>>
```

