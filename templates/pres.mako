##
## Template
##
[center][size=200][color=#351C75][b]${album.title}[/b][/color][/size]
 
[img]${album.cover_big}[/img]
 
 
[img]https://i.imgur.com/QisfJyt.png[/img]
 
[b]Album :[/b] ${album.title}
[b]Genre :[/b] ${album.genres[0].name}
[b]Artiste :[/b] ${album.artist.name}
[b]Date Sortie :[/b] ${album.release_date.strftime('%d/%m/%Y')}
[b]Nombres de pistes :[/b] ${album.nb_tracks}
 
 
[img]https://i.imgur.com/h0SiZO1.png[/img]

% for track in album.tracks:
<%! from datetime import datetime %>\
${track.track_position} - ${track.title} (${datetime.fromtimestamp(track.duration).strftime('%M:%S')})
% endfor
 
 
[img]https://i.imgur.com/9F4aTAH.png[/img]
 
[b]Format :[/b] Digital Media
[b]Codec audio :[/b] ${nfo['format']} (${nfo['other_bit_depth'][0]})
[b]Fréquence :[/b] ${nfo['other_sampling_rate'][0]}
[b]Débit Audio :[/b] ${(nfo['sampling_rate'] * nfo['channel_s'] * nfo['bit_depth']) / 1000} kb/s
 
 
[img]https://i.imgur.com/x69PFW3.png[/img]
 
[b]Nombre de fichier(s) :[/b] ${upload['nb_files']}
[b]Poids Total :[/b] [color=#ff0000]${upload['total_size']} [/color]


[url=https://www3.yggtorrent.do/profile/1026499-guiguirpz][img]https://i.imgur.com/8IbJ7Oh.png[/img][/url]
 
[url=https://github.com/GuiEpi/mtcc][img]https://i.imgur.com/fApXERh.png[/img][/url][/center]
