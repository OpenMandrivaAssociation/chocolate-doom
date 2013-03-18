Name:		chocolate-doom
Version:	1.7.0
Release:	1
Group:		Games/Arcade
Summary:	Historically compatible Doom engine
License:	GPLv2+
URL:		http://chocolate-doom.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(samplerate)

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_datadir}/applications/screensavers/chocolate-doom-screensaver.desktop

#These suck, we don't like them
rm -f %{buildroot}%{_datadir}/applications/chocolate-doom.desktop
rm -f %{buildroot}%{_datadir}/applications/chocolate-setup.desktop

cat > %{buildroot}%{_datadir}/applications/mandriva-chocolate-doom.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom
Comment=Conservative Doom source port
Exec=chocolate-doom
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-chocolate-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Setup
Comment=Setup tool for Chocolate Doom
Exec=chocolate-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
EOF

%files
%doc CMDLINE ChangeLog NEWS NOT-BUGS README README.OPL INSTALL
%{_gamesbindir}/chocolate-doom
%{_gamesbindir}/chocolate-server
%{_gamesbindir}/chocolate-setup
%{_datadir}/applications/mandriva-chocolate-doom.desktop
%{_datadir}/applications/mandriva-chocolate-setup.desktop
%{_iconsdir}/chocolate-doom.png
%{_iconsdir}/chocolate-setup.png
%{_mandir}/man5/chocolate-doom.cfg.5.*
%{_mandir}/man5/default.cfg.5.*
%{_mandir}/man6/chocolate-doom.6.*
%{_mandir}/man6/chocolate-server.6.*
%{_mandir}/man6/chocolate-setup.6.*

