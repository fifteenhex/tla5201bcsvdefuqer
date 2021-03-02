# Defuq the csv from the TLA5201B

The tektronix TLA5201B is a massive windows based logic
analyzer. The TLA app doesn't have serial protocol decoders
built in...

The TLA app can export CSV so we could load that into sigrok
but sigrok won't parse it so we need to clean it up first.

This expects an export from a data listing that looks like
this:

timestamp (ps, from start time), chan 0, chan 1, chan n...
Make sure the timestamp col is width enough that the whole
timestamp is output in the resulting file.

Export from the TLA app and select you want commas to
separate the fields. Drop the headers. Drop the units.

Then wait an hour for the massive text file to export
to your sane machine (You did the hack to enable 64M
didn't you? You're too lazy to set the right capture
legth right? :p), run ```./defuq /path/to/exported_file /path/to/fileforsigrok.csv```,
then open the csv via pulseviews import menu and set t,*b as the format.

Boom!
