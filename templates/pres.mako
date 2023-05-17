##
## Import
##
<%! from datetime import datetime %>\
##
## Template
##
[center][size=200][color=#351C75][b]${album.title}[/b][/color][/size]
 
[img]${album.cover_big}[/img]
 
 
[img]${settings['banner_theme']}/informations.png[/img]
 
[b]Album :[/b] ${album.title}
[b]Genre :[/b] ${album.genres[0].name}
[b]Artiste :[/b] ${album.artist.name}
[b]Date Sortie :[/b] ${album.release_date.strftime('%d/%m/%Y')}
[b]Nombres de pistes :[/b] ${album.nb_tracks}
 
 
[img]${settings['banner_theme']}/track_details.png[/img]

% for track in album.tracks:
${track.track_position} - ${track.title} (${datetime.fromtimestamp(track.duration).strftime('%M:%S')})
% endfor
 
 
[img]${settings['banner_theme']}/technical_details.png[/img]
 
[b]Format :[/b] Digital Media
% if nfo['format'] == "MPEG Audio":
[b]Codec audio :[/b] MP3
% else:
[b]Codec audio :[/b] ${nfo['format']} (${nfo['other_bit_depth'][0]})
% endif
% if nfo['other_sampling_rate']:
[b]Fréquence :[/b] ${nfo['other_sampling_rate'][0]}
%endif
% if 'audio_bitrate' in nfo:
[b]Débit Audio :[/b] ${(nfo['audio_bitrate'])} kb/s
% elif 'bit_depth' in nfo:
[b]Débit Audio :[/b] ${(nfo['sampling_rate'] * nfo['channel_s'] * nfo['bit_depth']) / 1000} kb/s
% else:
[b]Débit Audio :[/b] ${nfo['other_bit_rate'][0]}
% endif
 
[img]${settings['banner_theme']}/download.png[/img]
 
[b]Nombre de fichier(s) :[/b] ${upload['nb_files']}
[b]Poids Total :[/b] [color=#ff0000]${upload['total_size']} [/color]


[url=${settings['ygg_link']}][img]${settings['banner_theme']}/my_torrents.png[/img][/url]
 
[url=${settings['mtcc_link']}][img]${settings['banner_theme']}/mtcc_pres.png[/img][/url][/center]
