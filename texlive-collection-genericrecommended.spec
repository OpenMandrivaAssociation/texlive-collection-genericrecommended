# revision 19849
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-genericrecommended
Epoch:		1
Version:	20120224
Release:	2
Summary:	Recommended generic packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-genericrecommended.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-epsf
Requires:	texlive-fontname
Requires:	texlive-genmisc
Requires:	texlive-kastrup
Requires:	texlive-multido
Requires:	texlive-path
Requires:	texlive-tex-ps
Requires:	texlive-ulem
Requires:	texlive-collection-basic

%description
Recommended packages that work with multiple formats.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780327
- Update to latest release.
- Import texlive-collection-genericrecommended
- Import texlive-collection-genericrecommended

