%define oname mog
%define rev 1548

Summary:	A side-view, flick-screen platform game
Name:		mazeofgalious
Version:	0.63
Release:	3
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.braingames.getput.com/mog/
Source0:	%{oname}-%{version}.%{rev}.tar.bz2
Source1:	thegnu.pcx
Patch0:		mog-0.63-makefile.patch
Patch1:		mog-0.63-datapath.patch
Patch2:		mog-0.63-desktop.patch
Patch3:		mog-0.63-makefile2.patch
Patch4:		mog-0.63-sfmt.patch
BuildRequires:	imagemagick
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
Provides:	%{oname} = %{EVRD}

%description
The Maze of Galious (MoG in short) was originally a Konami game for the MSX
computer system. Its real name is Knightmare II: The Maze of Galious and is
the sequel of another Konami game called Knightmare.

MoG is a very addictive game where you have to kill thousands of enemies,
collect items in order to obtain new powers and defeat some really great demons
at the end of each level. The gameplay of MoG is not the boring linear one.

In MoG you are free to go everywhere you want from the beginning of the game.
You have to be very careful of the order in which you visit all the rooms in
the HUGE map if you want to keep your character alive. The map is structured
in a main map (called the castle) and 10 submaps (called the worlds).
Initially you are in the castle and you have to find the keys that open the
doors to go to each of the worlds. To complete the game you have to defeat
the boss at the end of each one of the 10 worlds. You are free to revisit
each world as often as you want in order to see if you have missed something.

To defeat all 10 demons you control two characters: Popolon and Aphrodite.
Each one has special abilities, i.e. Popolon has a greater ability to jump
and Aphrodite is able to dive.

%files
%doc LICENSE *.txt
%{_gamesbindir}/%{oname}
%{_gamesdatadir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{oname}.png

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}.%{rev}
%patch0 -p1 -b .makefile
%patch1 -p1 -b .datapath
%patch2 -p1 -b .desktop
%patch3 -p1 -b .makefile
%patch4 -p1 -b .sfmt

%build
%make OPTFLAGS="%{optflags}" LFLAGS="%{ldflags}"

%install
%makeinstall_std

# replace Konami logo with GNU
rm -f %{buildroot}%{_gamesdatadir}/%{oname}/graphics/*/konami.pcx
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/alfonso/
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/alternate/
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/boltian/
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/hinox/
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/naramura/
cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/original/


