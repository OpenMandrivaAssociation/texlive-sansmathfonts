Name:		texlive-sansmathfonts
Version:	64661
Release:	1
Summary:	Correct placement of accents in sans-serif maths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/sansmathfonts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathfonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sans serifsmall caps and math fonts for use with Computer
Modern.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/sansmathfonts
%{_texmfdistdir}/fonts/source/public/sansmathfonts
%{_texmfdistdir}/fonts/tfm/public/sansmathfonts
%{_texmfdistdir}/fonts/type1/public/sansmathfonts
%{_texmfdistdir}/fonts/vf/public/sansmathfonts
%{_texmfdistdir}/tex/latex/sansmathfonts
%doc %{_texmfdistdir}/doc/fonts/sansmathfonts

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
