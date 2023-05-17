##
## Import
##
<%! from time import strftime as time %>\
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
## Template
##
${hline()}
${ title | center }
${hline()}

Artist...............: ${album['album_performer']}
Album................: ${album['album']}
% if 'genre' in album:
Genre................:
% endif
Source...............: Web
Year.................: ${album['recorded_date']}
Ripper...............: 
% if album['format'] == "MPEG Audio":
Codec................: ${album['writing_library']}
Version..............: ${album['format']} ${album['format_version']} ${album['format_profile']}
% else:
Codec................: ${album['format_info']} (${album['format']})
Version..............:
% endif
Quality..............: ${album['compression_mode']}
% if 'other_bit_depth' in album:
% if album['channel_s'] == 2:
Channels.............: Stereo / ${album['other_sampling_rate'][0]} / ${album['other_bit_depth'][0]}
% else:
Channels.............: Mono / ${album['other_sampling_rate'][0]} / ${album['other_bit_depth'][0]}
% endif
% else:
% if album['channel_s'] == 2:
Channels.............: Stereo / ${album['other_bit_rate'][0]}
% else:
Channels.............: Mono / ${album['other_bit_rate'][0]}
% endif
% endif
Information..........:

Ripped by............: ${settings['ripper']} on ${"%d/%m/%Y" | time}
Posted by............: ${settings['uploader']} on ${"%d/%m/%Y" | time}

Included.............: NFO
% if 'cover_type' in album:
Cover................: ${album['cover_type']}
% endif

${hline()}
${ "Tracklisting" | center }
${hline()}

% for track in tracklist:
${ '%2s' % track['track_name_position']}. \
${ track['track_name'].ljust(album['track_name_maxlen']+3, ' ') }\
[${track['duration']}]
% endfor

Playing Time.........: ${album['playing_time']}
Total Size...........: ${album['total_size']}

NFO generated on.....: ${"%x %X" | time}


:: Generated by ${settings['nfo_name']} v${settings['nfo_version']} - ${settings['mtcc_link']} ::