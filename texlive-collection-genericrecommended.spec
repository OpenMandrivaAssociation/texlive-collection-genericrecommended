# revision 30396
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-genericrecommended
Epoch:		1
Version:	20131013
Release:	5
Summary:	Generic recommended packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-genericrecommended.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-epsf
Requires:	texlive-fontname
Requires:	texlive-genmisc
Requires:	texlive-kastrup
Requires:	texlive-multido
Requires:	texlive-path
Requires:	texlive-tex-ps
Requires:	texlive-ulem

%description
Recommended packages that work with multiple formats.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
