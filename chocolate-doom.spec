Name:		chocolate-doom
Version:	3.1.0
Release:	1
Group:		Games/Arcade
Summary:	Historically compatible Doom engine
License:	GPLv2+
URL:		http://chocolate-doom.org/
Source0:      https://github.com/chocolate-doom/chocolate-doom/archive/%{version}/%{name}-%{name}-%{version}.tar.gz
# Looks like this source is no longer updated
#Source0:	http://www.chocolate-doom.org/downloads/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(samplerate)

Recommends:     doom-iwad
Provides:       doom-engine

%description
Chocolate Doom is a game engine that aims to accurately reproduce the
experience of playing vanilla Doom. It is a conservative, historically
accurate Doom source port, which is compatible with the thousands of mods
and levels that were made before the Doom source code was released. Rather
than flashy new graphics, Chocolate Doom's main features are its accurate
reproduction of the game as it was played in the 1990s.

The following games can be played:
-Doom (including the shareware and registered versions,
       and the Ultimate Doom expansion pack)
-Doom II
-Final Doom (TNT:Evilution, and the Plutonia Experiment)
-Chex Quest

It is also possible to play these expansion packs and commercial games, each
of which requires one of the above:
-The Master Levels for Doom II
-Hacx

And also various TCs and WAD files:
http://www.chocolate-doom.org/wiki/index.php/User_guide

Warning! Chocolate Doom needs to know where to find your IWAD file.
To do this, put the file into /usr/share/games/doom or read INSTALL
file in docs for other possibilities.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%%build
%configure --bindir=%{_gamesbindir}
%make_build

%install
%make_install iconsdir="%{_iconsdir}/hicolor/64x64/apps"

rm -f %{buildroot}%{_datadir}/applications/screensavers/%{name}-screensaver.desktop

# These suck, we don't like them
rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_datadir}/applications/chocolate-setup.desktop
rm -f %{buildroot}%{_datadir}/applications/chocolate-heretic.desktop
rm -f %{buildroot}%{_datadir}/applications/chocolate-hexen.desktop
rm -f %{buildroot}%{_datadir}/applications/chocolate-strife.desktop

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom
Comment=Conservative Doom source port
Exec=chocolate-doom
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
Keywords=first;person;shooter;doom;vanilla;
EOF

cat > %{buildroot}%{_datadir}/applications/chocolate-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Setup
Comment=Setup tool for Chocolate Doom
Exec=chocolate-doom-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
Keywords=first;person;shooter;doom;vanilla;
EOF

cat > %{buildroot}%{_datadir}/applications/chocolate-heretic.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Heretic
Comment=Conservative Doom source port
Exec=chocolate-heretic
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
Keywords=first;person;shooter;doom;vanilla;
EOF

cat > %{buildroot}%{_datadir}/applications/chocolate-hexen.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Hexen
Comment=Conservative Doom source port
Exec=chocolate-hexen
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
Keywords=first;person;shooter;doom;vanilla;
EOF

cat > %{buildroot}%{_datadir}/applications/chocolate-strife.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Strife
Comment=Conservative Doom source port
Exec=chocolate-strife
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
Keywords=first;person;shooter;doom;vanilla;
EOF

%files
%doc AUTHORS
%doc %{_docdir}/chocolate-doom
%doc %{_docdir}/chocolate-heretic
%doc %{_docdir}/chocolate-hexen
%doc %{_docdir}/chocolate-strife
%{_gamesbindir}/%{name}
%{_gamesbindir}/chocolate-server
%{_gamesbindir}/chocolate-doom-setup
%{_gamesbindir}/chocolate-heretic
%{_gamesbindir}/chocolate-heretic-setup
%{_gamesbindir}/chocolate-hexen
%{_gamesbindir}/chocolate-hexen-setup
%{_gamesbindir}/chocolate-strife
%{_gamesbindir}/chocolate-strife-setup
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/chocolate-setup.desktop
%{_datadir}/applications/chocolate-heretic.desktop
%{_datadir}/applications/chocolate-hexen.desktop
%{_datadir}/applications/chocolate-strife.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/chocolate-heretic
%{_datadir}/bash-completion/completions/chocolate-hexen
%{_datadir}/bash-completion/completions/chocolate-strife
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/chocolate-setup.png
%{_mandir}/man5/%{name}.cfg.5.*
%{_mandir}/man5/chocolate-heretic.cfg.5.*
%{_mandir}/man5/chocolate-hexen.cfg.5.*
%{_mandir}/man5/chocolate-strife.cfg.5.*
%{_mandir}/man5/default.cfg.5.*
%{_mandir}/man5/heretic.cfg.5.*
%{_mandir}/man5/hexen.cfg.5.*
%{_mandir}/man5/strife.cfg.5.*
%{_mandir}/man6/%{name}.6.*
%{_mandir}/man6/chocolate-server.6.*
%{_mandir}/man6/chocolate-setup.6.*
%{_mandir}/man6/chocolate-doom-setup.6.*
%{_mandir}/man6/chocolate-heretic-setup.6.*
%{_mandir}/man6/chocolate-heretic.6.*
%{_mandir}/man6/chocolate-hexen-setup.6.*
%{_mandir}/man6/chocolate-hexen.6.*
%{_mandir}/man6/chocolate-strife-setup.6.*
%{_mandir}/man6/chocolate-strife.6.*
