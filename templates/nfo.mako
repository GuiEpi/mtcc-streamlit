##
## Variables
##
<% pagewidth = 60 %>\
<% title = album['album_performer'] + ' - ' + album['album'] %>\
##
## Functions
##
<%def name="hline()">${'-' * pagewidth}</%def>\
##
## Expression filterings
## http://docs.makotemplates.org/en/latest/filtering.html
##
<%!
    def center(word):
        return str.center(str(word), 60, ' ')
%>\
##
## THE template
##
${hline()}
${ title | center }
${hline()}
Artist:   ${album['album_performer']}
Album:    ${album['album']}
Genre:    
Date:     ${album['recorded_date']}
Codec:    ${album['format_info']} (${album['format']})
Ripper:   EAC (Secure mode) / LAME 3.92 & Asus CD-S520
Quality:  ${album['compression_mode']}
% if album['channel_s'] == 2:
Channels: Stereo / ${album['other_sampling_rate']} / ${album['other_bit_depth']}
% else:
Channels: Mono / ${album['other_sampling_rate'][0]} / ${album['other_bit_depth'][0]}
% endif

Tracklist:
${hline()}
% for track in tracklist:
${ '%2s' % track['track_name_position']}. \
${ track['track_name'].ljust(album['track_name_maxlen']+3, ' ') }\
(${track['other_duration'][0]})
% endfor
${hline()}

<%! from time import strftime as time %>\
:: Generated on ${"%x %X" | time} with KK Nfo Builder ::