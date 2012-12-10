%define	oname	mog
%define	rev	1548

Summary:	A side-view, flick-screen platform game
Name:		mazeofgalious
Version:	0.63
Release:	%mkrel 1
License:	GPLv2
Group:		Games/Arcade
URL:		http://www.braingames.getput.com/mog/
Source0:	%{oname}-%{version}.%{rev}.tar.bz2
Source1:	thegnu.pcx
Patch0:		mog-0.63-makefile.patch
Patch1:		mog-0.63-datapath.patch
Patch2:		mog-0.63-desktop.patch
BuildRequires:	imagemagick
BuildRequires:	SDL-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
Provides:	%{oname} = %{version}-%{release}

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

%prep
%setup -q -n %{oname}-%{version}.%{rev}
%patch0 -p1 -b .makefile
%patch1 -p1 -b .datapath
%patch2 -p1 -b .desktop

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# replace Konami logo with GNU
rm -f %{buildroot}%{_gamesdatadir}/%{oname}/graphics/*/konami.pcx
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/alfonso/
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/alternate/
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/boltian/
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/hinox/
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/naramura/
%__cp %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/graphics/original/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE *.txt
%{_gamesbindir}/%{oname}
%{_gamesdatadir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/%{oname}.png



%changelog
* Sun Nov 20 2011 Andrey Bondrov <abondrov@mandriva.org> 0.63-1mdv2011.0
+ Revision: 732040
- imported package mazeofgalious

